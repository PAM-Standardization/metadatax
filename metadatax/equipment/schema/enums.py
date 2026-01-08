import graphene

from metadatax.equipment.models import HydrophoneDirectivity

__all__ = [
    'HydrophoneDirectivityEnum',
]


class HydrophoneDirectivityEnum(graphene.Enum):
    class Meta:
        enum = HydrophoneDirectivity
