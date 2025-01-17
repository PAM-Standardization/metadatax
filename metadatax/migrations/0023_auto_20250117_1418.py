# Generated by Django 3.2.25 on 2025-01-17 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadatax', '0022_auto_20240911_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='recorder',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the recorder', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='latitude',
            field=models.FloatField(blank=True, help_text='Latitude of the platform position (WGS84 decimal degrees).', null=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='longitude',
            field=models.FloatField(blank=True, help_text='Longitude of the platform position (WGS84 decimal degree).', null=True),
        ),
        migrations.CreateModel(
            name='MobilePlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('hydrophone_depth', models.FloatField()),
                ('heading', models.FloatField(blank=True, default=0.0, null=True)),
                ('pitch', models.FloatField(blank=True, default=0.0, null=True)),
                ('roll', models.FloatField(blank=True, default=0.0, null=True)),
                ('deployment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadatax.deployment')),
            ],
        ),
    ]
