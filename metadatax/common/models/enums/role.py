from django.db import models


class Role(models.TextChoices):
    MAIN_CONTACT = ("MC", "Main Contact")
    FUNDER = ("F", "Funder")
    PROJECT_OWNER = ("PO", "Project Owner")
    PROJECT_MANAGER = ("PM", "Project Manager")
    DATASET_SUPPLIER = ("DS", "Dataset Supplier")
    DATASET_PRODUCER = ("DP", "Dataset Producer")
    PRODUCTION_DATABASE = ("PD", "Production Database")
    CONTACT_POINT = ("CP", "Contact Point")