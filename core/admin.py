from django.contrib import admin
from django.apps import apps
from django.conf import settings

from .models import Intervention

admin.site.site_header = 'Nos députés'


@admin.register(Intervention)
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('id', 'seance_id')


# auto-register all models
app = apps.get_app_config('core')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass