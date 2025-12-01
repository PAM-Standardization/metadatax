from django.contrib import admin

from metadatax.bibliography.models import Author


class AuthorInline(admin.TabularInline):

    extra = 0
    model = Author

    autocomplete_fields = ["contact"]
    filter_vertical = [
        "institutions",
    ]
