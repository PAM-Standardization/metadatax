from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Model, QuerySet

from rest_framework.serializers import ModelSerializer

from metadatax.utils import export


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


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
