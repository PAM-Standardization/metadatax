from django.contrib import admin
from django_extended.admin import HiddenModelAdmin

from metadatax.acquisition.models import Site


@admin.register(Site)
class SiteAdmin(HiddenModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
        "project__name",
    ]
