from django_extension.models import ExtendedEnum


class Financing(ExtendedEnum):
    PUBLIC = ("PU", "Public")
    PRIVATE = ("PR", "Private")
    MIXTE = ("MI", "Mixte")
    NOT_FINANCED = ("NF", "Not Financed")


class ChannelConfigurationStatus(ExtendedEnum):
    ACTIVE = ("A", "Active")
    FAILED = ("F", "Failed")
    LOST = ("L", "Lost")
