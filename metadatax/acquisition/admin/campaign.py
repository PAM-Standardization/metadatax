from django.contrib import admin
from django.contrib.admin import TabularInline

from metadatax.acquisition.models import Campaign


class CampaignInline(TabularInline):
    model = Campaign
    classes = ["collapse"]


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
