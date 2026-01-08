from django_extended.models import ExtendedEnum


class HydrophoneDirectivity(ExtendedEnum):
    """Hydrophone directivity"""

    OMNI_DIRECTIONAL = ("OMNI", "Omni-directional")
    BI_DIRECTIONAL = ("BI", "Bi-directional")
    UNI_DIRECTIONAL = ("UNI", "Uni-directional")
    CARDIOID = ("CAR", "Cardioid")
    SUPERCARDIOID = ("SCAR", "Supercardioid")
