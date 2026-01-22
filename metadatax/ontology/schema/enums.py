import graphene
from django_extension.schema.types import ExtendedEnumType

from metadatax.ontology.models import SignalShape, SignalPlurality

__all__ = [
    'SignalPluralityEnum',
    'SignalShapeEnum',
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
