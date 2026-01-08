from django.contrib import admin
from django_extended.admin import HiddenModelAdmin

from metadatax.acquisition.models import Campaign


@admin.register(Campaign)
class CampaignAdmin(HiddenModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
        "project__name",
    ]
