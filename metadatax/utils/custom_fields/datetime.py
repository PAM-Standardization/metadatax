from datetime import datetime

from django.db import models
from django.forms import widgets
from django.forms.utils import to_current_timezone

from .date import DateWidget


class DateTimeField(models.DateTimeField):
    def formfield(self, **kwargs):
        return super().formfield(**{**kwargs, "widget": DateTimeWidget})


class DateTimeWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        _widgets = []
        _widgets.append(DateWidget(attrs={"name": "date"}))
        _widgets.append(widgets.TimeInput(attrs={"name": "time", "type": "time"}))
        super().__init__(_widgets, attrs)

    def decompress(self, value: datetime):
        if value:
            value = to_current_timezone(value)
            return [value.date(), value.time()]
        return [None, None]
