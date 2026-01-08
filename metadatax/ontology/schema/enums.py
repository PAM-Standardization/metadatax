import graphene

from metadatax.ontology.models import SignalShape, SignalPlurality

__all__ = [
    'SignalPluralityEnum',
    'SignalShapeEnum',
]


class SignalShapeEnum(graphene.Enum):
    class Meta:
        enum = SignalShape


class SignalPluralityEnum(graphene.Enum):
    class Meta:
        enum = SignalPlurality
