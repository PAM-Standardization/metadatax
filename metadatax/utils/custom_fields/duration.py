from datetime import timedelta
from typing import Optional

from django.db import models
from django.forms import MultiWidget
from django.utils.dateparse import parse_duration
from django.utils.translation import ugettext_lazy
from durationwidget.widgets import LabeledNumberInput


def duration_to_year_month_day(duration: Optional[timedelta]) -> (int, int, int):
    if duration is None:
        return 0, 0, 0
    years = duration.days // 30 // 12
    months = duration.days // 30 - (12 * years)
    days = duration.days - (30 * months + 12 * 30 * years)
    return years, months, days


def duration_to_readable_year_month_day(duration: Optional[timedelta]) -> str:
    if duration is None:
        return "-"
    years, months, days = duration_to_year_month_day(duration)
    i = []
    if years > 0:
        i.append(f"{years} year")
    if months > 0:
        i.append(f"{months} months")
    if days > 0:
        i.append(f"{days} days")
    return f"{', '.join(i)}"


def year_month_day_to_duration(years: int, months: int, days: int) -> timedelta:
    return timedelta(days=int(days + 30 * (months + 12 * years)))


class DurationField(models.DurationField):
    def formfield(self, **kwargs):
        return super().formfield(**{**kwargs, "widget": DurationWidget})


class DurationWidget(MultiWidget):
    def __init__(self, attrs=None):
        self.show_years = True
        self.show_months = True
        self.show_days = True
        _widgets = []
        _widgets.append(LabeledNumberInput(label=ugettext_lazy("Years"), type="years")),
        _widgets.append(
            LabeledNumberInput(label=ugettext_lazy("Months"), type="months")
        ),
        _widgets.append(LabeledNumberInput(label=ugettext_lazy("Days"), type="days")),
        super().__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            parsed_value: timedelta = parse_duration(value)
            return duration_to_year_month_day(parsed_value)
        else:
            return []

    def value_from_datadict(self, data, files, name):
        data_list = {
            widget.type: widget.value_from_datadict(
                data, files, name + "_{0}".format(i)
            )
            for i, widget in enumerate(self.widgets)
        }
        for key, val in data_list.items():
            try:
                data_list[key] = int(val)
            except ValueError:
                data_list[key] = 0

        years = int(data_list.get("years"))
        months = int(data_list.get("months"))
        days = int(data_list.get("days"))

        if self.is_required and days == 0 and years == 0 and months == 0:
            return ""

        return str(year_month_day_to_duration(years, months, days))
