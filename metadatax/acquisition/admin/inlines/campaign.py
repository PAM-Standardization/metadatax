from django.contrib import admin

from metadatax.acquisition.models import Campaign


class CampaignInline(admin.TabularInline):
    model = Campaign
    extra = 0
