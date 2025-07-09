from django.contrib import admin

from metadatax.bibliography.models import Bibliography
from .author import AuthorInline
from ...utils.admin import get_many_to_many


@admin.register(Bibliography)
class BibliographyAdmin(admin.ModelAdmin):
    """Collaborator presentation in DjangoAdmin"""

    list_display = ["title", "doi", "publication", "type", "show_tags"]
    search_fields = [
        "title",
        "doi",
    ]
    filter_horizontal = ("tags",)
    inlines = [
        AuthorInline,
    ]

    @admin.display(description="Tags")
    def show_tags(self, obj: Bibliography):
        """show_tags"""
        return get_many_to_many(obj, "tags", "name")
