from django_extended.models import ExtendedEnum


class Financing(ExtendedEnum):
    PUBLIC = ("PU", "Public")
    PRIVATE = ("PR", "Private")
    MIXTE = ("MI", "Mixte")
    NOT_FINANCED = ("NF", "Not Financed")
