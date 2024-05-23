"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.acquisition import (
    Project,
    Institution,
    Deployment,
    ChannelConfiguration,
    ProjectType,
    PlatformType,
    Platform,
    Campaign, Site
)
from .__util__ import custom_titled_filter


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


class ProjectTypeAdmin(admin.ModelAdmin):
    """Project type presentation in DjangoAdmin"""

    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]


class ProjectAdmin(admin.ModelAdmin):
    """Project presentation in DjangoAdmin"""

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
    list_display = [
        "name",
        "list_responsible_parties",
        "accessibility",
        "project_type",
        "project_goal",
        "doi",
    ]


class DeploymentAdmin(admin.ModelAdmin):
    """Deployment presentation in DjangoAdmin"""

    search_fields = [
        "name",
        "project__name",
        "provider__name",
    ]
    list_filter = [
        "project__accessibility",
        "platform__type__name",
        "provider",
    ]
    list_display = [
        "name",
        "project",
        "provider",
        "campaign",
        "deployment_date",
        "deployment_vessel",
        "recovery_date",
        "recovery_vessel",
        "platform",
        "site",
        "longitude",
        "latitude",
        "bathymetric_depth",
    ]


class ChannelConfigurationAdmin(admin.ModelAdmin):
    """ChannelConfiguration presentation in DjangoAdmin"""

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
    list_display = [
        "id",
        "channel_name",
        "hydrophone",
        "recorder",
        "gain",
        "duty_cycle",
        "sampling_frequency",
        "recording_format",
        "sample_depth",
    ]


class PlatformTypeAdmin(admin.ModelAdmin):
    """Platform type presentation in DjangoAdmin"""

    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]


class PlatformAdmin(admin.ModelAdmin):
    """Platform presentation in DjangoAdmin"""

    list_display = [
        "name",
        "type",
        "description"
    ]
    search_fields = [
        "name",
    ]
    list_filter = [
        "type",
    ]


class CampaignAdmin(admin.ModelAdmin):
    """Campaign presentation in DjangoAdmin"""

    list_display = [
        "name",
        "project",
    ]
    search_fields = [
        "name",
        "project",
    ]


class SiteAdmin(admin.ModelAdmin):
    """Campaign presentation in DjangoAdmin"""

    list_display = [
        "name",
        "project",
    ]
    search_fields = [
        "name",
        "project",
    ]


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(ChannelConfiguration, ChannelConfigurationAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(PlatformType, PlatformTypeAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Site, SiteAdmin)
