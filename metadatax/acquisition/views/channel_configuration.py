"""Acquisition models for metadata app"""

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from metadatax.acquisition.models import ChannelConfiguration
from metadatax.acquisition.serializers import ChannelConfigurationSerializer


class ChannelConfigurationViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = ChannelConfiguration.objects.select_related(
        "recorder_specification",
        "detector_specification",
    ).prefetch_related(
        "other_equipments",
        "other_equipments__owner",
        "other_equipments__provider",
        "other_equipments__storage_specification",
        "other_equipments__recorder_specification",
        "other_equipments__hydrophone_specification",
        "other_equipments__acoustic_detector_specification",
        "other_equipments__acoustic_detector_specification__detected_labels",
        "other_equipments__acoustic_detector_specification__detected_labels__source",
        "other_equipments__acoustic_detector_specification__detected_labels__sound",
        "other_equipments__acoustic_detector_specification__detected_labels__physical_descriptor",
        "recorder_specification",
        "recorder_specification__recorder",
        "recorder_specification__recorder__recorder_specification",
        "recorder_specification__hydrophone",
        "recorder_specification__hydrophone__hydrophone_specification",
        "recorder_specification__recording_formats",
        "detector_specification",
        "detector_specification__detector",
        "detector_specification__detector__acoustic_detector_specification",
        "detector_specification__detector__acoustic_detector_specification__detected_labels",
        "detector_specification__detector__acoustic_detector_specification__detected_labels__source",
        "detector_specification__detector__acoustic_detector_specification__detected_labels__sound",
        "detector_specification__detector__acoustic_detector_specification__detected_labels__physical_descriptor",
        "detector_specification__output_formats",
        "detector_specification__labels",
        "detector_specification__labels__source",
        "detector_specification__labels__sound",
        "detector_specification__labels__physical_descriptor",
    )
    serializer_class = ChannelConfigurationSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    search_fields = [
        "deployment_name",
        "deployment_project__name",
        "deployment_project__accessibility",
        "deployment_site__name",
        "deployment_campaign__name",
        "deployment_platform__name",
        "deployment_platform__type__name",
    ]
