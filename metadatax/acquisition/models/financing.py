from django.db import models


class Financing(models.TextChoices):
    PUBLIC = ("PU", "Public")
    PRIVATE = ("PR", "Private")
    MIXTE = ("MI", "Mixte")
    NOT_FINANCED = ("NF", "Not Financed")
