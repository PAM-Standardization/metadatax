# Generated by Django 3.2.25 on 2024-05-30 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadatax', '0019_auto_20240530_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recorder',
            options={'ordering': ['model', 'serial_number'], 'verbose_name': 'Equipment - Recorder'},
        ),
    ]
