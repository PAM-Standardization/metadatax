# Generated by Django 3.2.25 on 2025-03-25 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("metadatax", "0023_mobileplatform"),
    ]

    operations = [
        migrations.AddField(
            model_name="channelconfiguration",
            name="harvest_ending_date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=utc),
                help_text="Harvest stop date at which the channel configuration finished to record in (in UTC).",
                null=True,
                verbose_name="Harvest stop date (UTC)",
            ),
        ),
        migrations.AddField(
            model_name="channelconfiguration",
            name="harvest_starting_date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2020, 1, 1, 12, 0, tzinfo=utc),
                help_text="Harvest start date at which the channel configuration was idle to record (in UTC).",
                null=True,
                verbose_name="Harvest start date (UTC)",
            ),
        ),
    ]
