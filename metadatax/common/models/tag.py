from django.db import models


class Tag(models.Model):
    """Tag"""

    class Meta:
        db_table = 'mx_common_tag'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)
