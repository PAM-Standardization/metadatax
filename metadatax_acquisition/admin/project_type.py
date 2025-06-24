from django.contrib import admin

from metadatax_acquisition.models import ProjectType


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
