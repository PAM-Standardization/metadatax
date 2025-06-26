from rest_framework import serializers

from metadatax_equipment.models import AcousticDetectorSpecification
from metadatax_ontology.serializers import LabelSerializer


class AcousticDetectorSpecificationSerializer(serializers.ModelSerializer):
    detected_labels = LabelSerializer(many=True)

    class Meta:
        model = AcousticDetectorSpecification
        fields = '__all__'
