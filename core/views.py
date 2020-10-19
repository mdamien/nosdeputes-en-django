import json
from itertools import groupby

from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Count

import phpserialize

from .models import Intervention, Tag, Tagging, Seance, Section, \
    Organisme, Personnalite, Parlementaire, Amendement


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


def api_seance(request, seance_id, loi_id):
    interventions = Intervention.objects.filter(seance_id=seance_id).order_by('timestamp')
    taggings = Tagging.objects.filter(taggable_model="Intervention", taggable_id__in=interventions)
    tags = Tag.objects.filter(id__in=taggings.values('tag_id'), triple_namespace='loi', triple_key='numero')
    seances = Seance.objects.filter(id__in=interventions.values('seance_id'))
    sections = Section.objects.filter(id__in=interventions.values('section_id'))
    sections_parentes = Section.objects.filter(id__in=sections.values('section_id'))
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
    sections_parentes = jsonify(sections_parentes)

    # add tag infos to taggings
    for section in sections:
        if section['section_id']:
            section['section'] = find_by_id(sections_parentes, section['section_id'])

    # add tag infos to taggings
    for tagging in taggings:
        tagging['tag'] = find_by_id(tags, tagging['tag_id'])

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
        lois_id = [tagging['tag']['triple_value'] for tagging in intervention['taggings']]
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

        lois = []
        for tagging in intervention['taggings']:
            lois.append({
                'loi': tagging['tag']['triple_value']
            })

        section = ""
        soussection = ""
        if intervention["section_id"]:
            section = intervention["section"]
            if section["section_id"]:
                section, soussection = section["section"], section
                soussection = soussection["titre"]
            section = section["titre"]

        interventions_reformated.append({
            "seance_id": intervention["seance_id"],
            # à fignoler voir Seance php class getTitre
            "seance_titre": f"réunion du {intervention['date']} à {intervention['seance']['moment']}",
            "seance_lieu": seance_lieu,
            "date": intervention["date"],
            "heure": intervention["seance"]["moment"],
            "type": intervention["type"],
            "timestamp": intervention["timestamp"],
            "section": section,
            "soussection": soussection,
            "intervenant_nom": intervenant_nom,
            "intervenant_fonction": intervention["fonction"],
            "intervenant_slug": intervenant_slug,
            "intervenant_groupe": intervenant_groupe,
            "nbmots": intervention["nb_mots"],
            "contenu": intervention["intervention"],
            # "tags": [],
            # "amendements": [],
            "lois": lois,
            "source": intervention["source"],
            "url_nosdeputes": f"https://2007-2012.nosdeputes.fr/seance/{intervention['seance_id']}#inter_{intervention['md5']}",
            "url_nosdeputes_api": f"https://2007-2012.nosdeputes.fr/api/document/Intervention/{intervention['id']}/json",
            "id": intervention["id"],
            # "_intervention": intervention,
        })

    interventions = interventions_reformated

    data = {'seance': interventions}

    return JsonResponse(data)


def api_deputes(request):
    parlementaires = Parlementaire.objects.all()

    parlementaires = jsonify(parlementaires)

    parlementaires_reformatted = []
    for parlementaire in parlementaires:
        sites_web = []
        if parlementaire["sites_web"]:
            sites_web = phpserialize.loads(parlementaire["sites_web"].encode('utf-8')).values()
            sites_web = [{"site": site.decode('utf-8')} for site in sites_web if site]

        emails = []
        if parlementaire["mails"]:
            emails = phpserialize.loads(parlementaire["mails"].encode('utf-8')).values()
            emails = [{"email": email.decode('utf-8')} for email in emails if email]

        adresses = []
        if parlementaire["adresses"]:
            adresses = phpserialize.loads(parlementaire["adresses"].encode('utf-8')).values()
            print(adresses)
            adresses = [{"adresse": adresse.decode('utf-8')} for adresse in adresses if adresse]

        parlementaires_reformatted.append({
            "id": parlementaire["id"],
            "nom": parlementaire["nom"],
            "nom_de_famille": parlementaire["nom_de_famille"],
            "prenom": parlementaire["nom"].split(' ')[0],
            "sexe": parlementaire["sexe"],
            "date_naissance": parlementaire["date_naissance"],
            "lieu_naissance": parlementaire["lieu_naissance"],
            # "num_deptmt": parlementaire["num_deptmt"],
            "nom_circo": parlementaire["nom_circo"],
            "num_circo": parlementaire["num_circo"],
            "mandat_debut": parlementaire["debut_mandat"],
            "groupe_sigle": parlementaire["groupe_acronyme"],
            # "parti_ratt_financier": parlementaire["parti"],
            "sites_web": sites_web,
            "emails": emails,
            "adresses": adresses,
            # "collaborateurs": [
            #   {
            #     "collaborateur": "Mme Julie Phan-Pérain"
            #   },
            #   {
            #     "collaborateur": "M. Jules Plat"
            #   },
            #   {
            #     "collaborateur": "Mme Caroline Puisségur-Ripet"
            #   }
            # ],
            # "autres_mandats": [],
            # "anciens_autres_mandats": [],
            # "anciens_mandats": [
            #   {
            #     "mandat": "21/06/2017 /  / "
            #   }
            # ],
            # "profession": "Conseiller en gestion de patrimoine indépendant",
            # "place_en_hemicycle": "309",
            # "url_an": "http://www2.assemblee-nationale.fr/deputes/fiche/OMC_PA718902",
            # "id_an": "718902",
            # "slug": "cedric-roussel",
            # "url_nosdeputes": "https://www.nosdeputes.fr/cedric-roussel",
            # "url_nosdeputes_api": "https://www.nosdeputes.fr/cedric-roussel/json",
            # "nb_mandats": 1,
            # "twitter": "CedricRoussel06",
            "_parlementaire": parlementaire,
          })
    parlementaires = parlementaires_reformatted

    data = {'deputes': [parlementaires]}
    return JsonResponse(data)



def api_surprise(request):
    duplicates = list(Amendement.objects.all().values('content_md5').annotate(total=Count('content_md5')).filter(total__gt=1))
    duplicates = [amdt['content_md5'] for amdt in duplicates] # TODO: duplicate in LREM

    amendements = Amendement.objects.filter(sort="adopté") \
        .exclude(auteur_groupe_acronyme="LREM") \
        .exclude(auteur_groupe_acronyme=None) \
        .exclude(content_md5__in=duplicates)

    amendements = jsonify(amendements)

    for amdt in amendements:
        amdt["url_nosdeputes"] = f"https://www.nosdeputes.fr/{amdt['legislature']}/amendement/{amdt['texteloi_id']}/{amdt['numero']}"

    amendements.sort(key=lambda amdt:amdt['auteur_groupe_acronyme'])
    amendements = {k: list(v) for k, v in groupby(amendements, lambda amdt: amdt['auteur_groupe_acronyme'])}

    return JsonResponse(amendements, safe=False)