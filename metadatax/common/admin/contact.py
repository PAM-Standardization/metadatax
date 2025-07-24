from django.contrib import admin

from metadatax.common.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact administration"""

    list_display = [
        "initial_names",
        "first_name",
        "last_name",
        "mail",
        "website",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "mail",
        "website",
    ]
    filter_horizontal = [
        "current_institutions",
    ]
