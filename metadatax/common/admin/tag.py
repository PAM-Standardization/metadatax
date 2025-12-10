from django.contrib import admin
from django_extended.admin import ExtendedModelAdmin

from metadatax.common.models import Tag


@admin.register(Tag)
class TagAdmin(ExtendedModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
