from django.contrib import admin

from metadatax_equipment.models import SDCardSpecification


@admin.register(SDCardSpecification)
class SDCardSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "capacity",
    ]
