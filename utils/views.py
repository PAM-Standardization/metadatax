import json

from django.core.exceptions import FieldError
from rest_framework import filters
from rest_framework.request import Request


class ModelFilter(filters.BaseFilterBackend):
    """Common filter for model viewsets"""

    def filter_queryset(self, request: Request, queryset, view):
        _queryset = queryset
        for param in request.query_params:
            try:
                value = request.query_params[param]
                try:
                    _queryset = _queryset.filter(**{param: json.loads(value)})
                except (json.JSONDecodeError, TypeError):
                    _queryset = _queryset.filter(**{param: value})
            except FieldError:
                continue
        return _queryset.distinct()
