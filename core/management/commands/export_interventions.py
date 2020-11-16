import json, tqdm

from django.core.management.base import BaseCommand, CommandError
from core.models import Intervention
from django.core.serializers import serialize


class Command(BaseCommand):
    def handle(self, *args, **options):
        interventions = Intervention.objects.all().order_by('date')
        f = open('result.jsonl', 'w')
        for i in tqdm.tqdm(interventions):
            f.write(serialize('json', [i]) + '\n')
