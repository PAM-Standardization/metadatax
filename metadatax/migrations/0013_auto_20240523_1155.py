# Generated by Django 3.2.25 on 2024-05-23 09:55

from django.db import migrations, models
import django.db.models.deletion


def forward_migrate_format(apps, _):
    file_format_model = apps.get_model("metadatax", "FileFormat")
    file_model = apps.get_model("metadatax", "File")
    channel_configuration_model = apps.get_model("metadatax", "ChannelConfiguration")

    for file in file_model.objects.all():
        rec_format, _ = file_format_model.objects.get_or_create(name=file.format)
        file.format_class = rec_format
        file.save()

    for config in channel_configuration_model.objects.all():
        rec_format, _ = file_format_model.objects.get_or_create(
            name=config.recording_format
        )
        config.recording_format_class = rec_format
        config.save()


def reverse_migrate_format(apps, _):
    file_model = apps.get_model("metadatax", "File")
    channel_configuration_model = apps.get_model("metadatax", "ChannelConfiguration")

    for file in file_model.objects.all():
        file.format = file.format_class.name

    for config in channel_configuration_model.objects.all():
        config.recording_format = config.recording_format_class.name


class Migration(migrations.Migration):
    dependencies = [
        ("metadatax", "0012_auto_20240523_1144"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileFormat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="channelconfiguration",
            name="recording_format_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="metadatax.fileformat",
            ),
        ),
        migrations.AddField(
            model_name="file",
            name="format_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="metadatax.fileformat",
            ),
        ),
        migrations.RunPython(
            code=forward_migrate_format, reverse_code=reverse_migrate_format
        ),
        migrations.RemoveField(
            model_name="channelconfiguration",
            name="recording_format",
        ),
        migrations.RenameField(
            model_name="channelconfiguration",
            old_name="recording_format_class",
            new_name="recording_format",
        ),
        migrations.RemoveField(
            model_name="file",
            name="format",
        ),
        migrations.RenameField(
            model_name="file",
            old_name="format_class",
            new_name="format",
        ),
    ]
