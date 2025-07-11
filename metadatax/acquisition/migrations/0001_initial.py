# Generated by Django 3.2.25 on 2025-06-25 09:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Campaign",
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
                (
                    "name",
                    models.CharField(
                        help_text="Name of the campaign during which the instrument was deployed.",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "ordering": ["project", "name"],
                "db_table": "metadatax_acquisition_campaign",
            },
        ),
        migrations.CreateModel(
            name="ChannelConfiguration",
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
                (
                    "continuous",
                    models.BooleanField(
                        blank=True,
                        help_text="Boolean indicating if the record is continuous (1) or has a duty cycle (0).",
                        null=True,
                    ),
                ),
                (
                    "duty_cycle_on",
                    models.IntegerField(
                        blank=True,
                        help_text="If it's not Continuous, time length (in second) during which the recorder is on.",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "duty_cycle_off",
                    models.IntegerField(
                        blank=True,
                        help_text="If it's not Continuous, time length (in second) during which the recorder is off.",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "instrument_depth",
                    models.IntegerField(
                        blank=True,
                        help_text="Immersion depth of instrument (in positive meters).",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("timezone", models.CharField(blank=True, max_length=50, null=True)),
                ("extra_information", models.TextField(blank=True, null=True)),
                (
                    "harvest_starting_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Harvest start date at which the channel configuration was idle to record (in UTC).",
                        null=True,
                        verbose_name="Harvest start date (UTC)",
                    ),
                ),
                (
                    "harvest_ending_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Harvest stop date at which the channel configuration finished to record in (in UTC).",
                        null=True,
                        verbose_name="Harvest stop date (UTC)",
                    ),
                ),
            ],
            options={
                "ordering": ["deployment"],
                "db_table": "metadatax_acquisition_channelconfiguration",
            },
        ),
        migrations.CreateModel(
            name="ChannelConfigurationDetectorSpecification",
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
                (
                    "min_frequency",
                    models.IntegerField(
                        blank=True,
                        help_text="Minimum frequency (in Hertz).",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "max_frequency",
                    models.IntegerField(
                        blank=True,
                        help_text="Maximum frequency (in Hertz).",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("filter", models.TextField(blank=True, null=True)),
                ("configuration", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "metadatax_acquisition_channelconfigurationdetectorspecification",
            },
        ),
        migrations.CreateModel(
            name="ChannelConfigurationFiles",
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
            ],
            options={
                "db_table": "metadatax_acquisition_channelconfigurationfiles",
            },
        ),
        migrations.CreateModel(
            name="ChannelConfigurationRecorderSpecification",
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
                (
                    "sampling_frequency",
                    models.IntegerField(
                        help_text="Sampling frequency of the recording channel (in Hertz).",
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "sample_depth",
                    models.IntegerField(
                        help_text="Number of quantization bits used to represent each sample by the recorder channel (in bits).",
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "gain",
                    models.FloatField(
                        help_text="Gain of the channel (recorder), with correction factors if applicable, without hydrophone sensibility (in dB). If end-to-end calibration with hydrophone sensibility, set it in Sensitivity and set Gain to 0 dB.<br>Gain G of the channel such that : data(uPa) = data(volt)*10^((-Sh-G)/20). See Sensitivity for Sh definition."
                    ),
                ),
                (
                    "channel_name",
                    models.CharField(
                        blank=True,
                        default="A",
                        help_text="Name of the channel used for recording.",
                        max_length=5,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "metadatax_acquisition_channelconfigurationrecorderspecification",
            },
        ),
        migrations.CreateModel(
            name="Deployment",
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
                (
                    "longitude",
                    models.FloatField(
                        help_text="Longitude of the platform position (WGS84 decimal degree)."
                    ),
                ),
                (
                    "latitude",
                    models.FloatField(
                        help_text="Latitude of the platform position (WGS84 decimal degrees)."
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the deployment.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "bathymetric_depth",
                    models.IntegerField(
                        blank=True,
                        help_text="Underwater depth of ocean floor at the platform position (in positive meters).",
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "deployment_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date and time at which the measurement system was deployed in UTC.",
                        null=True,
                        verbose_name="Deployment date (UTC)",
                    ),
                ),
                (
                    "deployment_vessel",
                    models.CharField(
                        blank=True,
                        help_text="Name of the vehicle associated with the deployment.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "recovery_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date and time at which the measurement system was recovered in UTC.",
                        null=True,
                        verbose_name="Recovery date (UTC)",
                    ),
                ),
                (
                    "recovery_vessel",
                    models.CharField(
                        blank=True,
                        help_text="Name of the vehicle associated with the recovery.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Optional description of deployment and recovery conditions (weather, technical issues,...).",
                        null=True,
                    ),
                ),
                (
                    "campaign",
                    models.ForeignKey(
                        blank=True,
                        help_text="Campaign during which the instrument was deployed.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="deployments",
                        to="acquisition.campaign",
                    ),
                ),
                (
                    "contacts",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Contacts related to the deployment.",
                        related_name="deployments",
                        to="common.ContactRole",
                    ),
                ),
            ],
            options={
                "ordering": ["project", "name"],
                "db_table": "metadatax_acquisition_deployment",
            },
        ),
        migrations.CreateModel(
            name="Project",
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
                (
                    "name",
                    models.CharField(
                        help_text="Name of the project", max_length=255, unique=True
                    ),
                ),
                (
                    "accessibility",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("C", "Confidential"),
                            ("R", "Upon request"),
                            ("O", "Open access"),
                        ],
                        help_text="Accessibility level of the data. If the availability is not sure or non-uniform within the project, the default value is upon request.",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "doi",
                    models.CharField(
                        blank=True,
                        help_text="Digital Object Identifier of the data, if existing.",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "project_goal",
                    models.TextField(
                        blank=True,
                        help_text="Description of the goal of the project.",
                        null=True,
                    ),
                ),
                (
                    "financing",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PU", "Public"),
                            ("PR", "Private"),
                            ("MI", "Mixte"),
                            ("NF", "Not Financed"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "contacts",
                    models.ManyToManyField(
                        help_text="Should have at least one 'Main Contact'",
                        to="common.ContactRole",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "db_table": "metadatax_acquisition_project",
            },
        ),
        migrations.CreateModel(
            name="ProjectType",
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
                (
                    "name",
                    models.CharField(
                        help_text="Description of the type of the project",
                        max_length=255,
                        unique=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "db_table": "metadatax_acquisition_projecttype",
            },
        ),
        migrations.CreateModel(
            name="Site",
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
                (
                    "name",
                    models.CharField(
                        help_text="Name of the platform conceptual location. A site may group together several platforms in relatively close proximity, or describes a location where regular deployments are carried out.",
                        max_length=255,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        help_text="Project associated to this site",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sites",
                        to="acquisition.project",
                    ),
                ),
            ],
            options={
                "ordering": ["project", "name"],
                "db_table": "metadatax_acquisition_site",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="project_type",
            field=models.ForeignKey(
                blank=True,
                help_text="Description of the type of the project (e.g., research, marine renewable energies, long monitoring,...).",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects",
                to="acquisition.projecttype",
            ),
        ),
        migrations.CreateModel(
            name="DeploymentMobilePosition",
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
                (
                    "datetime",
                    models.DateTimeField(
                        help_text="Datetime for the mobile platform position"
                    ),
                ),
                (
                    "longitude",
                    models.FloatField(help_text="Longitude of the mobile platform"),
                ),
                (
                    "latitude",
                    models.FloatField(help_text="Latitude of the mobile platform"),
                ),
                (
                    "depth",
                    models.FloatField(
                        help_text="Hydrophone depth of the mobile platform (In positive meters)",
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "heading",
                    models.FloatField(
                        blank=True,
                        default=0.0,
                        help_text="Heading of the mobile platform",
                        null=True,
                    ),
                ),
                (
                    "pitch",
                    models.FloatField(
                        blank=True,
                        default=0.0,
                        help_text="Pitch of the mobile platform",
                        null=True,
                    ),
                ),
                (
                    "roll",
                    models.FloatField(
                        blank=True,
                        default=0.0,
                        help_text="Roll of the mobile platform",
                        null=True,
                    ),
                ),
                (
                    "deployment",
                    models.ForeignKey(
                        help_text="Related deployment",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mobile_positions",
                        to="acquisition.deployment",
                    ),
                ),
            ],
            options={
                "ordering": ["project", "name"],
                "db_table": "metadatax_acquisition_deploymentmobileposition",
            },
        ),
    ]
