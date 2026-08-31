from django_extension.schema.types import ExtendedEnumType

from metadatax.equipment.models import HydrophoneDirectivity

__all__ = [
    'HydrophoneDirectivityEnum',
]


class HydrophoneDirectivityEnum(ExtendedEnumType):
    class Meta:
        enum = HydrophoneDirectivity

    def __str__(self):
        return self.value
        return super().__str__()

    OmniDirectional = 'OMNI'
    BiDirectional = 'BI'
    UniDirectional = 'UNI'
    Cardioid = 'CAR'
    Supercardioid = 'SCAR'
