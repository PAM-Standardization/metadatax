from django.contrib import admin

from metadatax.common.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact administration"""

    list_display = [
        "name",
        "mail",
        "website",
    ]
    search_fields = [
        "name",
        "mail",
        "website",
    ]
