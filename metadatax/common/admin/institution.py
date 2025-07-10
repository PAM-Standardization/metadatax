from django.contrib import admin

from metadatax.common.models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "location",
        "mail",
        "website",
    ]
    search_fields = [
        "name",
        "city",
        "country",
        "mail",
        "website",
    ]
