"""Acquisition metadata administration"""
from django.contrib import admin
from django.contrib.admin import TabularInline

from metadatax.models.acquisition import (
    Institution,
    Campaign,
    ProjectType, Site, Project, PlatformType, Deployment, ChannelConfiguration, Platform,
)
from .__util__ import custom_titled_filter


@admin.register(ProjectType, PlatformType, Site, Campaign, Platform)
class CommonAcquisitionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    """Institution presentation in DjangoAdmin"""

    list_display = [
        "name",
        "contact",
        "website",
    ]
    search_fields = [
        "name",
        "contact",
        "website",
    ]


class CampaignInline(TabularInline):
    model = Campaign
    classes = ['collapse']


class SiteInline(TabularInline):
    model = Site
    classes = ['collapse']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project presentation in DjangoAdmin"""

    list_display = [
        "name",
        "list_responsible_parties",
        "accessibility",
        "project_type",
        "project_goal",
        "doi",
        "campaigns",
        "sites",
    ]
    search_fields = [
        "name",
        "project_goal",
        "doi",
    ]
    list_filter = [
        "accessibility",
        "project_type",
        "responsible_parties",
    ]
    inlines = [
        CampaignInline,
        SiteInline,
    ]

    @admin.display(description="Responsible parties")
    def list_responsible_parties(self, obj) -> str:
        """Display readable list of responsible_parties"""
        return ", ".join([p.name for p in obj.responsible_parties.all()])

    def campaigns(self, obj) -> str:
        return ", ".join([c.name for c in sorted(obj.campaigns.all(), key=lambda x: x.name)])

    def sites(self, obj) -> str:
        return ", ".join([s.name for s in sorted(obj.sites.all(), key=lambda x: x.name)])


@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):
    """Deployment presentation in DjangoAdmin"""

    list_display = [
        "__str__",
        "name",
        "project",
        "provider",
        "campaign_name",
        "site_name",
        "deployment_date",
        "deployment_vessel",
        "recovery_date",
        "recovery_vessel",
        "platform",
        "longitude",
        "latitude",
        "bathymetric_depth",
    ]
    search_fields = [
        "name",
        "project__name",
        "provider__name",
    ]
    list_filter = [
        "project__accessibility",
        ("platform__type__name", custom_titled_filter("platform type")),
        "provider",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "project",
                    "provider",
                ]
            }
        ),
        (
            "Location",
            {
                "classes": ["wide", ],
                "fields": [
                    "site",
                    "platform",
                    "latitude",
                    "longitude",
                    "bathymetric_depth",
                ]
            }
        ),
        (
            "Deployment & Recovery",
            {
                "classes": ["collapse", ],
                "fields": [
                    "campaign",
                    ("deployment_date", "deployment_vessel"),
                    ("recovery_date", "recovery_vessel"),
                    "description"
                ]
            }
        )
    ]

    @admin.display(description="Campaign")
    def campaign_name(self, obj) -> str:
        return obj.campaign.name if obj.campaign else None

    @admin.display(description="Site")
    def site_name(self, obj) -> str:
        return obj.site.name if obj.site else None


@admin.register(ChannelConfiguration)
class ChannelConfigurationAdmin(admin.ModelAdmin):
    """ChannelConfiguration presentation in DjangoAdmin"""

    list_display = [
        "__str__",
        "channel_name",
        "hydrophone",
        "recorder",
        "deployment",
        "gain",
        "hydrophone_depth",
        "duty_cycle",
        "sampling_frequency",
        "recording_format",
        "sample_depth",
    ]
    search_fields = [
        "channel_name",
    ]
    list_filter = [
        "deployment__project__accessibility",
        ("deployment__project__name", custom_titled_filter("project")),
        "continuous",
        "recording_format",
        ("hydrophone__model", custom_titled_filter("hydrophone model")),
        ("recorder__model", custom_titled_filter("recorder model")),
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "deployment",
                ]
            }
        ), (
            "Recorder",
            {
                "fields": [
                    "recorder",
                    "channel_name",
                    "recording_format",
                    "sample_depth",
                    "gain",
                ]
            }
        ), (
            "Hydrophone",
            {
                "fields": [
                    "hydrophone",
                    "hydrophone_depth",
                    "sampling_frequency",
                ]
            }
        ), (
            "Duty cycle",
            {
                "classes": ["collapse",],
                "fields": [
                    "continuous",
                    "duty_cycle_on",
                    "duty_cycle_off",
                ]
            }
        )
    ]
