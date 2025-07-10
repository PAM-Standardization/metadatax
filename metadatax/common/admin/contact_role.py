from django.contrib import admin

from metadatax.common.models import ContactRole


@admin.register(ContactRole)
class ContactRoleAdmin(admin.ModelAdmin):
    """Contact role administration"""

    list_display = [
        "id",
        "contact",
        "institution",
        "role",
    ]
    search_fields = [
        "contact__first_name",
        "contact__last_name",
        "contact__mail",
        "contact__website",
        "institution__name",
        "institution__mail",
        "institution__website",
    ]
    list_filter = [
        "role",
    ]
