from django.contrib import admin
from django.contrib.admin import TabularInline

from metadatax.acquisition.models import Site


class SiteInline(TabularInline):
    model = Site
    classes = ["collapse"]


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
