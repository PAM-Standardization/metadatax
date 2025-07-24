from django.db import models
from django.forms import widgets


class DateField(models.DateField):
    def formfield(self, **kwargs):
        return super().formfield(**{**kwargs, "widget": DateWidget})


class DateWidget(widgets.DateInput):
    def __init__(self, attrs=None, format=None):
        _attrs = {}
        if attrs is not None:
            _attrs = {**attrs}
        _attrs["type"] = "date"
        super().__init__(_attrs, format)
