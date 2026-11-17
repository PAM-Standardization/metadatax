from django_extension.schema.types import ExtendedEnumType

from metadatax.ontology.models import SignalShape, SignalPlurality, LabelDisplay

__all__ = [
    'SignalPluralityEnum',
    'SignalShapeEnum',
    'LabelDisplayEnum',
]


class SignalShapeEnum(ExtendedEnumType):
    class Meta:
        enum = SignalShape

    Stationary = 'S'
    Pulse = 'P'
    FrequencyModulation = 'FM'


class SignalPluralityEnum(ExtendedEnumType):
    class Meta:
        enum = SignalPlurality

    One = 'O'
    Set = 'S'
    RepetitiveSet = 'RS'


class LabelDisplayEnum(ExtendedEnumType):
    class Meta:
        enum = LabelDisplay

    English = "E"
    French = "F"
    Code = "C"
