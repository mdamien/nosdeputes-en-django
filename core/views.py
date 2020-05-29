import json

from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Intervention

def api_seance(request):
    seance_id = 103
    loiid = 820
    interventions = Intervention.objects.filter(seance_id=seance_id)
    interventions = json.loads(serialize('json', interventions))
    interventions = [inter['fields'] for inter in interventions]
    # section_id -> id_dossier_an -> texteloi.id !
    data = {'seance': interventions}

    return JsonResponse(data)