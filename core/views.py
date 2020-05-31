import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Intervention, Tag, Tagging, Seance, Section, \
    Organisme, Personnalite, Parlementaire


def jsonify(queryset):
    objs = json.loads(serialize('json', queryset))
    for obj in objs:
        for k, v in obj['fields'].items():
            obj[k] = v
        obj['id'] = obj['pk']
        del obj['pk']
        del obj['fields']
        del obj['model']
    return objs


def find_by_id(objs, id):
    return [obj for obj in objs if obj['id'] == id][0]


def api_seance(request):
    seance_id = 1050
    loi_id = 820

    interventions = Intervention.objects.filter(seance_id=seance_id).order_by('timestamp')
    taggings = Tagging.objects.filter(taggable_model="Intervention", taggable_id__in=interventions)
    tags = Tag.objects.filter(id__in=taggings.values('tag_id'), triple_namespace='loi', triple_key='numero')
    seances = Seance.objects.filter(id__in=interventions.values('seance_id'))
    sections = Section.objects.filter(id__in=interventions.values('section_id'))
    organismes = Organisme.objects.filter(id__in=seances.values('organisme_id'))
    parlementaires = Parlementaire.objects.filter(id__in=interventions.values('parlementaire_id'))
    personnalites = Personnalite.objects.filter(id__in=interventions.values('personnalite_id'))

    interventions = jsonify(interventions)
    taggings = jsonify(taggings)
    tags = jsonify(tags)
    seances = jsonify(seances)
    sections = jsonify(sections)
    organismes = jsonify(organismes)
    parlementaires = jsonify(parlementaires)
    personnalites = jsonify(personnalites)

    # add tag infos to taggings
    for tagging in taggings:
        tagging['tags'] = [tag for tag in tags if tagging['tag_id'] == tag['id']]

    # add organisme infos to seance
    for seance in seances:
        if seance['organisme_id']:
            seance['organisme'] = find_by_id(organismes, seance['organisme_id'])

    # add seance/tagging/sections infos to intervention
    for intervention in interventions:
        intervention['seance'] = find_by_id(seances, intervention['seance_id'])
        if intervention['section_id']:
            intervention['section'] = find_by_id(sections, intervention['section_id'])
        if intervention['parlementaire_id']:
            intervention['parlementaire'] = find_by_id(parlementaires, intervention['parlementaire_id'])
        if intervention['personnalite_id']:
            intervention['personnalite'] = find_by_id(personnalites, intervention['personnalite_id'])
        intervention['taggings'] = [
            tagging for tagging in taggings
            if intervention['id'] == tagging['taggable_id']
        ]

    # keep only intervention about this law
    interventions_about_law = []
    for intervention in interventions:
        lois_id = [tag['triple_value'] for tagging in intervention['taggings'] for tag in tagging['tags']]
        if str(loi_id) in lois_id or str(loi_id).rjust(4, '0') in lois_id:
            interventions_about_law.append(intervention)
    interventions = interventions_about_law

    # reformat to ND format
    interventions_reformated = []
    for intervention in interventions:
        seance_lieu = ""
        if 'organisme' in intervention['seance']:
            seance_lieu = intervention['seance']['organisme']['nom']

        intervenant_nom = ""
        intervenant_groupe = ""
        intervenant_slug = ""
        if intervention["parlementaire_id"]:
            intervenant_nom = intervention['parlementaire']['nom']
            intervenant_groupe = intervention['parlementaire']['groupe_acronyme']
            intervenant_slug = intervention['parlementaire']['slug']
        elif intervention["personnalite_id"]:
            intervenant_nom = intervention['personnalite']['nom']

        interventions_reformated.append({
            "seance_id": intervention["seance_id"],
            # "seance_titre": intervention["seance"], voir Seance php class getTitre
            "seance_lieu": seance_lieu,
            "date": intervention["date"],
            "heure": intervention["seance"]["moment"],
            "type": intervention["type"],
            "timestamp": intervention["timestamp"],
            # "section": "",
            # "soussection": "",
            "intervenant_nom": intervenant_nom,
            "intervenant_fonction": intervention["fonction"],
            "intervenant_slug": intervenant_slug,
            "intervenant_groupe": intervenant_groupe,
            "nbmots": intervention["nb_mots"],
            "contenu": intervention["intervention"],
            # "tags": [],
            # "amendements": [],
            # "lois": [
            #  {
            #    "loi": "0820"
            #  }
            # ],
            "source": intervention["source"],
            # "url_nosdeputes": "https://2007-2012.nosdeputes.fr/seance/1050#inter_4a6b51d620cdecafad94e3de0f662986",
            # "url_nosdeputes_api": "https://2007-2012.nosdeputes.fr/api/document/Intervention/723667/json",
            "id": intervention["id"],
            "_intervention": intervention,
        })

    interventions = interventions_reformated

    data = {'seance': interventions}

    return JsonResponse(data)