# Generated by Django 3.2.25 on 2025-07-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bibliography", "0003_alter_bibliography_conference_information"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="bibliography",
            name="Conference has required information",
        ),
        migrations.AddConstraint(
            model_name="bibliography",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        models.Q(("type", "C"), _negated=True),
                        ("conference_information__isnull", True),
                    ),
                    models.Q(("conference_information__isnull", False), ("type", "C")),
                    ("type", "P"),
                    _connector="OR",
                ),
                name="Conference has required information",
            ),
        ),
    ]
