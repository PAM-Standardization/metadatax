from django.contrib import admin

from metadatax.common.models import ContactRole


@admin.register(ContactRole)
class ContactRoleAdmin(admin.ModelAdmin):
    """Contact role administration"""

    list_display = [
        "id",
        "contact",
        "role",
    ]
    search_fields = [
        "contact__name",
        "contact__mail",
        "contact__website",
    ]
    list_filter = [
        "role",
    ]
