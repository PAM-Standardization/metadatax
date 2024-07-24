# Generated by Django 3.2.25 on 2024-05-23 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("metadatax", "0014_auto_20240523_1634"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="equipmentprovider",
            options={"ordering": ["name"], "verbose_name": "Equipment - Provider"},
        ),
        migrations.AlterModelOptions(
            name="hydrophone",
            options={"ordering": ["model"], "verbose_name": "Equipment - Hydrophone"},
        ),
        migrations.AlterModelOptions(
            name="recorder",
            options={"ordering": ["model"], "verbose_name": "Equipment - Recorder"},
        ),
    ]
