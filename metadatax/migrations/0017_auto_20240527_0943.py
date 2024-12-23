# Generated by Django 3.2.25 on 2024-05-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metadatax", "0016_auto_20240524_1119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fileformat",
            name="name",
            field=models.CharField(help_text="Format of the audio file", max_length=20),
        ),
        migrations.AlterField(
            model_name="platformtype",
            name="name",
            field=models.CharField(
                help_text="Generic name of the support of the deployed instruments",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="projecttype",
            name="name",
            field=models.CharField(
                help_text="Description of the type of the project",
                max_length=255,
                unique=True,
            ),
        ),
    ]
