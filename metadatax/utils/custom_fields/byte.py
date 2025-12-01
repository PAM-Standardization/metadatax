from typing import Optional

from django import forms
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.postgres.utils import prefix_validation_error
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import MultiWidget, NumberInput, Select
from django.utils.translation import gettext_lazy as _

from metadatax.common.models import ByteUnit, Byte


class ByteField(ArrayField):
    invalid_error_message = _("%(property)s did not validate:")

    def __init__(self, **kwargs):
        kwargs.pop("base_field", None)
        kwargs.pop("size", None)
        super().__init__(base_field=models.CharField(max_length=4), size=2, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                **kwargs,
                "form_class": ByteFormField,
                "widget": ByteWidget,
                "required": False,
            }
        )

    def get_db_converters(self, connection):
        def converter(value, expression, connection):
            if value is None:
                return None
            if len(value) == 1:
                return Byte(*value[0].split(" "))
            return Byte(*value)

        return [converter] + super().get_db_converters(connection)

    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, (Byte)):
            return super().get_db_prep_value([*value], connection, prepared)
        return super().get_db_prep_value(value, connection, prepared)

    def get_validate_data(self, value: [str]) -> (Optional[int], str):
        value, unit = value
        return (int(value) if value else value, unit)

    def validate(self, value: [str], model_instance):
        errors = []
        value, unit = self.get_validate_data(value)
        try:
            models.IntegerField(null=self.null, blank=self.blank).validate(
                value, model_instance
            )
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "value"},
                )
            )
        try:
            models.TextField(
                null=self.null, blank=self.blank, choices=ByteUnit.choices
            ).validate(unit, model_instance)
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "unit"},
                )
            )
        if errors:
            raise ValidationError(errors)

    def run_validators(self, value: [str]):
        errors = []
        value, unit = self.get_validate_data(value)
        try:
            models.IntegerField(null=self.null, blank=self.blank).run_validators(value)
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "value"},
                )
            )
        try:
            models.TextField(
                null=self.null, blank=self.blank, choices=ByteUnit.choices
            ).run_validators(unit)
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "unit"},
                )
            )
        if errors:
            raise ValidationError(errors)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if not value[0]:
            return None
        return Byte(*value)


class ByteFormField(SimpleArrayField):
    invalid_error_message = _("%(property)s did not validate:")

    def __init__(
        self, base_field, *, delimiter=",", max_length=None, min_length=None, **kwargs
    ):
        super().__init__(
            base_field,
            delimiter=delimiter,
            max_length=max_length,
            min_length=min_length,
            **kwargs
        )
        self.base_field.required = False

    def clean(self, value):
        value, unit = value
        if value is None or value == '':
            return None
        return [int(value), unit]

    def validate(self, value):
        errors = []
        if value in self.empty_values:
            if self.required:
                raise ValidationError(self.error_messages['required'], code='required')
            return

        value, unit = value
        try:
            forms.IntegerField(
                required=self.required, min_value=1, max_value=999
            ).validate(value)
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "value"},
                )
            )
        try:
            forms.ChoiceField(required=True, choices=ByteUnit.choices).validate(unit)
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "unit"},
                )
            )
        if errors:
            raise ValidationError(errors)

    def run_validators(self, value: [str]):
        errors = []
        if value in self.empty_values:
            if self.required:
                raise ValidationError(self.error_messages['required'], code='required')
            return

        value, unit = value
        try:
            forms.IntegerField(
                required=self.required, min_value=1, max_value=999
            ).run_validators(value)
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "value"},
                )
            )
        try:
            forms.ChoiceField(required=True, choices=ByteUnit.choices).run_validators(
                unit
            )
        except ValidationError as error:
            errors.append(
                prefix_validation_error(
                    error,
                    prefix=self.invalid_error_message,
                    code="item_invalid",
                    params={"property": "unit"},
                )
            )
        if errors:
            raise ValidationError(errors)



class ByteWidget(MultiWidget):
    def __init__(self, attrs=None):
        _widgets = []
        _widgets.append(NumberInput(attrs={"min": 1, "max": 999, "name": "value"}))
        _widgets.append(
            Select(
                choices=ByteUnit.choices,
                attrs={"name": "unit"},
            )
        )
        super().__init__(_widgets, attrs)

    def decompress(self, value: Optional[Byte]):
        if value:
            return [*value]
        else:
            return []

    def format_value(self, value: Optional[Byte]):
        return self.decompress(value)
