# Generated by Django 3.2.25 on 2024-05-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metadatax", "0007_auto_20240517_1137"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
    ]
