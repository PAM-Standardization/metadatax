from django.contrib import admin

from metadatax_equipment.models import Equipment
from metadatax_equipment.serializers import EquipmentSerializer
from utils.admin import JSONExportModelAdmin


@admin.register(Equipment)
class EquipmentAdmin(JSONExportModelAdmin):
    model = Equipment
    serializer = EquipmentSerializer
    list_display = [
        "serial_number",
        "model",
        "owner",
        "provider",
        "sd_card_specification",
        "recorder_specification",
        "hydrophone_specification",
        "acoustic_detector_specification",
        "purchase_date",
        "name",
        "battery_slots_count",
        "battery_type",
        "cables",
    ]
    search_fields = [
        "serial_number",
        "model",
        "owner__name",
        "owner__mail",
        "provider__name",
        "provider__mail",
        "name",
        "acoustic_detector_specification__detected_labels__nickname",
        "acoustic_detector_specification__detected_labels__source__english_name",
        "acoustic_detector_specification__detected_labels__sound__english_name",
        "acoustic_detector_specification__algorithm_name",
    ]
    list_filter = [
        "hydrophone_specification__directivity",
    ]
