# Generated by Django 3.2.25 on 2024-05-16 14:31

from django.db import migrations


def add_missing_permissions(apps, _):
    user_model = apps.get_model("meta_auth", "User")
    permission_model = apps.get_model("auth", "Permission")
    users = user_model.objects.filter(is_staff=True, is_superuser=False)
    for user in users:
        user.user_permissions.add(
            permission_model.objects.get(codename="add_projecttype"),
            permission_model.objects.get(codename="change_projecttype"),
            permission_model.objects.get(codename="view_projecttype"),
            permission_model.objects.get(codename="add_site"),
            permission_model.objects.get(codename="change_site"),
            permission_model.objects.get(codename="view_site"),
            permission_model.objects.get(codename="add_campaign"),
            permission_model.objects.get(codename="change_campaign"),
            permission_model.objects.get(codename="view_campaign"),
            permission_model.objects.get(codename="add_platform"),
            permission_model.objects.get(codename="change_platform"),
            permission_model.objects.get(codename="view_platform"),
            permission_model.objects.get(codename="add_platformtype"),
            permission_model.objects.get(codename="change_platformtype"),
            permission_model.objects.get(codename="view_platformtype"),
            permission_model.objects.get(codename="add_fileformat"),
            permission_model.objects.get(codename="change_fileformat"),
            permission_model.objects.get(codename="view_fileformat"),
            permission_model.objects.get(codename="add_hydrophonemodel"),
            permission_model.objects.get(codename="change_hydrophonemodel"),
            permission_model.objects.get(codename="view_hydrophonemodel"),
            permission_model.objects.get(codename="add_recordermodel"),
            permission_model.objects.get(codename="change_recordermodel"),
            permission_model.objects.get(codename="view_recordermodel"),
            permission_model.objects.get(codename="add_equipmentprovider"),
            permission_model.objects.get(codename="change_equipmentprovider"),
            permission_model.objects.get(codename="view_equipmentprovider"),
        )


class Migration(migrations.Migration):
    dependencies = [
        ("meta_auth", "0003_alter_user_email"),
    ]

    operations = [migrations.RunPython(add_missing_permissions)]
