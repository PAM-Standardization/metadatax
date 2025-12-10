from django.contrib import admin
from django_extended.admin import ExtendedModelAdmin

from metadatax.common.models import Institution


@admin.register(Institution)
class InstitutionAdmin(ExtendedModelAdmin):
    list_display = [
        "name",
        "location",
        "mail",
        "website",
    ]
    search_fields = [
        "name",
        "city",
        "country",
        "mail",
        "website",
    ]
