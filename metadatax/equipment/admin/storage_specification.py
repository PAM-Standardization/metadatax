from django.contrib import admin

from metadatax.equipment.models import StorageSpecification


@admin.register(StorageSpecification)
class StorageSpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "capacity",
    ]
    search_fields = [
        "capacity",
        "type",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "capacity",
                    "type",
                ]
            },
        ),
    ]
