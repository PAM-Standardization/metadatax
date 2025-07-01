from django.db import models

from metadatax.data.models import File
from .channel_configuration import ChannelConfiguration


class ChannelConfigurationFiles(models.Model):
    class Meta:
        unique_together = ["channel_configuration", "file"]
        db_table = "metadatax_acquisition_channelconfigurationfiles"

    channel_configuration = models.ForeignKey(
        ChannelConfiguration, on_delete=models.CASCADE
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE)
