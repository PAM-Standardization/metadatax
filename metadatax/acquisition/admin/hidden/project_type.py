from django.contrib import admin
from django_extension.admin import ExtendedModelAdmin

from metadatax.acquisition.models import ProjectType


@admin.register(ProjectType)
class ProjectTypeAdmin(ExtendedModelAdmin):
    hidden = True

    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
