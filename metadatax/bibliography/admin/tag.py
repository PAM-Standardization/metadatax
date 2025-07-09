from django.contrib import admin

from metadatax.bibliography.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = [
        "name",
    ]
    search_fields = [
        "name",
    ]
