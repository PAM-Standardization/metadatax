from django.contrib import admin
from django_extended.admin import HiddenModelAdmin

from metadatax.acquisition.models import ProjectType


@admin.register(ProjectType)
class ProjectTypeAdmin(HiddenModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
