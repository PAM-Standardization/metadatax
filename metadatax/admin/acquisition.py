"""Acquisition metadata administration"""
import csv
import io

from django import forms
from django.contrib import admin
from django.contrib.admin import TabularInline
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile

from meta_auth.admin import JSONExportModelAdmin
from metadatax.models.acquisition import (
    Institution,
    Campaign,
    ProjectType,
    Site,
    Project,
    PlatformType,
    Deployment,
    ChannelConfiguration,
    Platform,
)
from .__util__ import custom_titled_filter
from metadatax.models.data import FileFormat, File
from ..serializers.acquisition import ProjectFullSerializer


@admin.register(ProjectType, PlatformType, Site, Campaign, Platform, FileFormat)
class CommonAcquisitionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]


@admin.register(Institution)
class InstitutionModelAdmin(JSONExportModelAdmin):
    """Institution presentation in DjangoAdmin"""

    model = Institution
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
    classes = ["collapse"]


class SiteInline(TabularInline):
    model = Site
    classes = ["collapse"]


@admin.register(Project)
class ProjectModelAdmin(JSONExportModelAdmin):
    """Project presentation in DjangoAdmin"""

    serializer = ProjectFullSerializer
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
        return ", ".join(
            [c.name for c in sorted(obj.campaigns.all(), key=lambda x: x.name)]
        )

    def sites(self, obj) -> str:
        return ", ".join(
            [s.name for s in sorted(obj.sites.all(), key=lambda x: x.name)]
        )


@admin.register(Deployment)
class DeploymentModelAdmin(JSONExportModelAdmin):
    """Deployment presentation in DjangoAdmin"""

    model = Deployment
    depth = 2
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
            },
        ),
        (
            "Location",
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "site",
                    "platform",
                    "latitude",
                    "longitude",
                    "bathymetric_depth",
                ],
            },
        ),
        (
            "Deployment & Recovery",
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "campaign",
                    ("deployment_date", "deployment_vessel"),
                    ("recovery_date", "recovery_vessel"),
                    "description",
                ],
            },
        ),
    ]

    @admin.display(description="Campaign")
    def campaign_name(self, obj) -> str:
        return obj.campaign.name if obj.campaign else None

    @admin.display(description="Site")
    def site_name(self, obj) -> str:
        return obj.site.name if obj.site else None


class ChannelConfigurationForm(forms.ModelForm):
    csv_file = forms.FileField(validators=[validators.FileExtensionValidator(["csv"])])

    class Meta:
        model = ChannelConfiguration
        fields = "__all__"

    def save(self, commit=True):
        instance: ChannelConfiguration = super().save(commit=commit)
        csv_file: InMemoryUploadedFile = self.cleaned_data.get("csv_file", None)
        content = csv_file.read().decode("utf-8")
        files: list[File] = []
        file: dict
        for file in csv.DictReader(io.StringIO(content)):
            _format, _ = FileFormat.objects.get_or_create(
                name=str(file["format"]).upper()
            )
            files.append(
                File(
                    channel_configuration=instance,
                    name=file["name"],
                    format=_format,
                    initial_timestamp=file["initial_timestamp"],
                    duration=file["duration"],
                    sampling_frequency=file["sampling_frequency"],
                    sample_depth=file["sample_depth"],
                    storage_location=file["storage_location"],
                    file_size=file["file_size"],
                    accessibility=file["accessibility"],
                )
            )
        File.objects.bulk_create(files)
        return instance


@admin.register(ChannelConfiguration)
class ChannelConfigurationModelAdmin(JSONExportModelAdmin):
    """ChannelConfiguration presentation in DjangoAdmin"""

    model = ChannelConfiguration
    depth = 3
    form = ChannelConfigurationForm
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
        "recorder__model__name",
        "recorder__model__provider__name",
        "hydrophone__model__name",
        "hydrophone__model__provider__name",
        "deployment__name",
        "deployment__project__name",
        "deployment__campaign__name",
        "deployment__site__name",
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
            },
        ),
        (
            "Recorder",
            {
                "fields": [
                    "recorder",
                    "channel_name",
                    "recording_format",
                    "sample_depth",
                    "sampling_frequency",
                    "gain",
                ]
            },
        ),
        (
            "Hydrophone",
            {
                "fields": [
                    "hydrophone",
                    "hydrophone_depth",
                ]
            },
        ),
        (
            "Duty cycle",
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "continuous",
                    "duty_cycle_on",
                    "duty_cycle_off",
                ],
            },
        ),
        (
            "Import files",
            {
                "classes": [
                    "wide",
                ],
                "fields": [
                    "csv_file",
                ],
            },
        ),
    ]
