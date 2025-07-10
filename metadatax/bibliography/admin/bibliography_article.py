from django.contrib import admin

from metadatax.bibliography.models import BibliographyArticle


@admin.register(BibliographyArticle)
class BibliographyArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "journal",
        "volumes",
        "pages_from",
        "pages_to",
        "issue_nb",
        "article_nb",
    ]
    search_fields = ["journal"]
