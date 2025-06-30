from django.contrib import admin

from metadatax.data.models import DetectionProperties


@admin.register(DetectionProperties)
class DetectionPropertiesAdmin(admin.ModelAdmin):
    list_display = ["start", "end"]
