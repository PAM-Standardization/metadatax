from django.contrib import admin

from metadatax.acquisition.models import DeploymentMobilePosition


@admin.register(DeploymentMobilePosition)
class DeploymentMobilePositionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "deployment",
        "datetime",
        "longitude",
        "latitude",
        "depth",
        "heading",
        "pitch",
        "roll",
    ]
    search_fields = [
        "deployment__name",
    ]
    autocomplete_fields = [
        "deployment",
    ]
