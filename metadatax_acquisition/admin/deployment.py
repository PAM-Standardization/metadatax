"""Acquisition metadata administration"""
import csv
import io
from datetime import datetime
from typing import Optional

from django import forms
from django.contrib import admin
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from django.utils.safestring import mark_safe

from metadatax_acquisition.models import Deployment, DeploymentMobilePosition
from metadatax_acquisition.serializers import DeploymentExportSerializer
from utils.admin import JSONExportModelAdmin


class DeploymentForm(forms.ModelForm):
    """Deployment presentation in DjangoAdmin"""

    csv_file = forms.FileField(
        required=False,
        help_text="Only for mobile platform such as glider. Csv headers must contains Datetime in %Y-%m-%dT%H:%M:%S format, longitude, latitude, depth, heading, pitch and roll",
        validators=[validators.FileExtensionValidator(["csv"])],
    )

    class Meta:
        model = Deployment
        fields = "__all__"

    def save(self, commit=True):
        instance: Deployment = super().save(commit=commit)
        instance.save()
        csv_file: Optional[InMemoryUploadedFile] = self.cleaned_data.get(
            "csv_file", None
        )
        if csv_file is None:
            return instance
        content = csv_file.read().decode("utf-8")
        mobile: list[DeploymentMobilePosition] = []
        for file in csv.DictReader(io.StringIO(content)):
            headers = [k for k in file.keys()]
            new_mobile_platform = self.create_mobile_platform(instance, file, headers)
            mobile.append(new_mobile_platform)
        DeploymentMobilePosition.objects.bulk_create(mobile, ignore_conflicts=True)
        return instance

    def get_value(self, file, headers, index):
        try:
            return float(file.get(headers[index]))
        except:
            return 0

    def create_mobile_platform(
        self, instance, file, headers
    ) -> DeploymentMobilePosition:
        tz = timezone.get_current_timezone()
        return DeploymentMobilePosition(
            deployment=instance,
            datetime=timezone.make_aware(
                datetime.strptime(file.get(headers[0]), "%Y-%m-%dT%H:%M:%S"), tz, True
            ),
            longitude=self.get_value(file, headers, 1),
            latitude=self.get_value(file, headers, 2),
            depth=self.get_value(file, headers, 3),
            heading=self.get_value(file, headers, 4),
            pitch=self.get_value(file, headers, 5),
            roll=self.get_value(file, headers, 6),
        )


@admin.register(Deployment)
class DeploymentAdmin(JSONExportModelAdmin):
    """Deployment presentation in DjangoAdmin"""

    model = Deployment
    serializer = DeploymentExportSerializer
    form = DeploymentForm
    list_display = [
        "__str__",
        "name",
        "project",
        "list_contacts",
        "campaign_name",
        "site_name",
        "deployment_date",
        "deployment_vessel",
        "recovery_date",
        "recovery_vessel",
        "platform",
        "mobile_platforms",
        "longitude",
        "latitude",
        "bathymetric_depth",
    ]
    search_fields = [
        "name",
        "project__name",
        "contacts__contact__name",
        "contacts__contact__mail",
    ]
    list_filter = [
        "project__accessibility",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "project",
                    "contacts",
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
                    "csv_file",
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
    filter_horizontal = [
        "contacts",
    ]

    @admin.display(description="Contacts")
    def list_contacts(self, obj: Deployment) -> str:
        """Display readable list of responsible_parties"""
        return mark_safe("<br/>".join([str(role) for role in obj.contacts.all()]))

    @admin.display(description="Campaign")
    def campaign_name(self, obj: Deployment) -> str:
        return obj.campaign.name if obj.campaign else None

    @admin.display(description="Site")
    def site_name(self, obj: Deployment) -> str:
        return obj.site.name if obj.site else None

    @admin.display(description="Mobile platforms")
    def mobile_platforms(self, obj: Deployment) -> str:
        return mark_safe("<br/>".join([str(p) for p in obj.mobile_positions.all()]))
