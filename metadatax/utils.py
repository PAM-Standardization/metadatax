from django.db.models import QuerySet, Model
from django.http import JsonResponse
from rest_framework.serializers import ModelSerializer

from metadatax.serializers.utils import SimpleSerializer


def export(
    filename: str,
    queryset: QuerySet,
    model: Model,
    depth: int = 0,
    serializer: ModelSerializer.__class__ = None,
):
    """Export JSON file containing serialized queryset"""
    serialized_data: ModelSerializer
    if serializer is None:
        SimpleSerializer.Meta.model = model
        SimpleSerializer.Meta.depth = depth
        serialized_data = SimpleSerializer(data=queryset, many=True)
    else:
        serialized_data = serializer(data=queryset, many=True)
    serialized_data.is_valid()
    response = JsonResponse(
        data=serialized_data.data, safe=False, json_dumps_params={"ensure_ascii": False}
    )
    response["Content-Disposition"] = f'attachment; filename="{filename}.json"'
    return response
