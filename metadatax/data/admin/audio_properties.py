from django.contrib import admin

from metadatax.data.models import AudioProperties


@admin.register(AudioProperties)
class AudioPropertiesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sampling_frequency",
        "initial_timestamp",
        "duration",
        "sample_depth",
    ]
