from django.contrib import admin

from django_extension.admin import ExtendedModelAdmin

from metadatax.acquisition.models import Campaign


@admin.register(Campaign)
class CampaignAdmin(ExtendedModelAdmin):
    hidden = True

    list_display = [
        "name",
    ]
    search_fields = [
        "name",
        "project__name",
    ]
