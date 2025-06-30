from rest_framework import serializers

from metadatax.acquisition.models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"
