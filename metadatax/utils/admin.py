from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Model, QuerySet
from django.http import JsonResponse
from rest_framework.serializers import ModelSerializer

from .serializers import SimpleSerializer


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


class JSONExportModelAdmin(admin.ModelAdmin):
    serializer: ModelSerializer.__class__ = None
    model: Model.__class__ = None
    depth: int = 0

    actions = [
        "export",
    ]

    @admin.action(description="Download data as JSON")
    def export(self, request: WSGIRequest, queryset: QuerySet):
        """Export JSON file containing serialized queryset"""
        path = request.path.split("/")
        path.pop()
        filename = path.pop()
        return export(
            filename=filename,
            queryset=queryset,
            model=self.model,
            depth=self.depth,
            serializer=self.serializer,
        )


def get_many_to_many(obj, field_name, related_field_name="name"):
    """List all related custom_fields

    Args:
        obj (object): _description_
        field_name (string): _description_
        related_field_name (str, optional): _description_. Defaults to "name".

    Returns:
        string: _description_
    """
    field_name_attr = getattr(obj, field_name)
    many_to_many_attributs = ""
    for one_name_attr in field_name_attr.all().distinct():
        name_field = getattr(one_name_attr, related_field_name)
        many_to_many_attributs += f"{name_field}, "

    return many_to_many_attributs[:-2]
