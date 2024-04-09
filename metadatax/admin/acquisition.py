"""Acquisition metadata administration"""
from django.contrib import admin

from metadatax.models.acquisition import (
    Project,
    Institution,
    Deployment,
    ChannelConfiguration
)


class InstitutionAdmin(admin.ModelAdmin):
    """Institution presentation in DjangoAdmin"""

    search_fields = [
        "name",
        "contact"
    ]


class ProjectAdmin(admin.ModelAdmin):
    """Project presentation in DjangoAdmin"""

    search_fields = [
        "name",
        "responsible_parties"
    ]
    list_filter = [
        "accessibility",
        "responsible_parties",
        "project_type",
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
        "hydrophone",
        "recorder",
    ]


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(ChannelConfiguration, ChannelConfigurationAdmin)
