from django.contrib import admin

from metadatax.common.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
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
