from django.db import models

from metadatax.models import ChannelConfiguration, File


class ChannelConfigurationFiles(models.Model):
    class Meta:
        unique_together = ["channel_configuration", "file"]

    channel_configuration = models.ForeignKey(
        ChannelConfiguration, on_delete=models.CASCADE
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE)
