from django.db import models


class Accessibility(models.TextChoices):
    """Accessibility level of the data. Multiple choices are offered : open access, upon request, confidential."""

    CONFIDENTIAL = ("C", "Confidential")
    REQUEST = ("R", "Upon request")
    OPEN = ("O", "Open access")
