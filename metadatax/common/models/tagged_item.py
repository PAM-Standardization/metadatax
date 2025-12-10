from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from metadatax.common.models import Tag


class TaggedItem(models.Model):
    class Meta:
        db_table = "mx_common_taggeditem"
        ordering = ("tag",)
        unique_together = ('tag', 'item_type', 'item_id')

    def __str__(self):
        return f"{self.tag}: {self.item}"

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tagged_items")

    item_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    item_id = models.PositiveBigIntegerField()
    item = GenericForeignKey("item_type", "item_id")
