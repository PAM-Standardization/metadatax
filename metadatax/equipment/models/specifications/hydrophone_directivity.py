from django.db import models


class HydrophoneDirectivity(models.TextChoices):
    """Hydrophone directivity"""

    OMNI_DIRECTIONAL = ("OMNI", "Omni-directional")
    BI_DIRECTIONAL = ("BI", "Bi-directional")
    UNI_DIRECTIONAL = ("UNI", "Uni-directional")
    CARDIOID = ("CAR", "Cardioid")
    SUPERCARDIOID = ("SCAR", "Supercardioid")
