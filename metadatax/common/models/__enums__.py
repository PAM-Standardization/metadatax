from django_extension.models import ExtendedEnum


class Accessibility(ExtendedEnum):
    """Accessibility level of the data. Multiple choices are offered : open access, upon request, confidential."""

    CONFIDENTIAL = ("C", "Confidential")
    REQUEST = ("R", "Upon request")
    OPEN = ("O", "Open access")


class Role(ExtendedEnum):
    MAIN_CONTACT = ("MC", "Main Contact")
    FUNDER = ("F", "Funder")
    PROJECT_OWNER = ("PO", "Project Owner")
    PROJECT_MANAGER = ("PM", "Project Manager")
    DATASET_SUPPLIER = ("DS", "Dataset Supplier")
    DATASET_PRODUCER = ("DP", "Dataset Producer")
    PRODUCTION_DATABASE = ("PD", "Production Database")
    CONTACT_POINT = ("CP", "Contact Point")
