from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.common.models import Team


@admin.register(Team)
class TeamAdmin(ExtendedModelAdmin):
    """Team administration"""

    list_display = [
        "name",
        "institution",
        "mail",
        "website",
    ]
    search_fields = [
        "name",
        "institution__name",
        "mail",
        "website",
    ]
    list_filter = [
        "institution"
    ]
