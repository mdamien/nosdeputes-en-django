import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Intervention, Tag, Tagging


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


def api_seance(request):
    seance_id = 103
    loi_id = 820

    interventions = Intervention.objects.filter(seance_id=seance_id)
    taggings = Tagging.objects.filter(taggable_model="Intervention", taggable_id__in=interventions)
    tags = Tag.objects.filter(id__in=taggings.values('tag_id'), triple_key='numero')

    interventions = jsonify(interventions)
    taggings = jsonify(taggings)
    tags = jsonify(tags)

    # add tag infos to taggings
    for tagging in taggings:
        tagging['tags'] = [tag for tag in tags if tagging['tag_id'] == tag['id']]

    # add tagging infos to interventions
    for intervention in interventions:
        intervention['taggings'] = [
            tagging for tagging in taggings
            if intervention['id'] == tagging['taggable_id']
        ]

    # keep only intervention about this law
    interventions = [intervention for intervention in interventions if intervention['taggings']]

    data = {'seance': interventions}

    return JsonResponse(data)