from rest_framework import serializers

from metadatax.equipment.models import AcousticDetectorSpecification
from metadatax.ontology.serializers import LabelSerializer


class AcousticDetectorSpecificationSerializer(serializers.ModelSerializer):
    detected_labels = LabelSerializer(many=True)

    class Meta:
        model = AcousticDetectorSpecification
        fields = "__all__"
