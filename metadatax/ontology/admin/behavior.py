from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.ontology.models import Behavior


@admin.register(Behavior)
class BehaviorAdmin(ExtendedModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
