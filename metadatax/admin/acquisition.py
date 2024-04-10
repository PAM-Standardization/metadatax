"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.acquisition import (
    Project,
    Institution,
    Deployment,
    ChannelConfiguration
)
from .__util__ import custom_titled_filter


class InstitutionAdmin(admin.ModelAdmin):
    """Institution presentation in DjangoAdmin"""

    list_display = [
        "name",
        "contact"
    ]
    search_fields = [
        "name",
        "contact"
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
        "responsible_parties",
        "project_type",
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
        "project",
        "provider",
        "name"
    ]
    list_filter = [
        "project__accessibility",
        "platform_type",
        "provider"
    ]
    list_display = [
        "name",
        "provider",
        "campaign",
        "deployment_date",
        "deployment_vessel",
        "recovery_date",
        "recovery_vessel",
        "platform_type",
        "platform_name",
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


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(ChannelConfiguration, ChannelConfigurationAdmin)
