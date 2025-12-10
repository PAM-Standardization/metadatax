from django.contrib import admin
from django_extended.admin import ExtendedModelAdmin

from metadatax.common.models import Team


@admin.register(Team)
class TeamAdmin(ExtendedModelAdmin):
    """Team administration"""

    list_display = [
        "name",
        "institution",
    ]
    search_fields = [
        "name",
        "institution__name",
    ]
    list_filter = [
        "institution"
    ]
