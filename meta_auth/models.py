"""Meta_auth related models"""
from django.contrib.auth.models import AbstractUser, Permission
from django.db.models import CharField, BooleanField, EmailField
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    """Custom user with institution field"""

    email = EmailField(gettext_lazy('email address'), unique=True)
    institution = CharField(blank=True, null=True, max_length=255)
    accept_mailing = BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def allow_metadatax_edition(self):
        """Allow edition of models, except for deletion"""
        self.user_permissions.add(
            Permission.objects.get(codename="add_project"),
            Permission.objects.get(codename="change_project"),
            Permission.objects.get(codename="view_project"),

            Permission.objects.get(codename="add_institution"),
            Permission.objects.get(codename="change_institution"),
            Permission.objects.get(codename="view_institution"),

            Permission.objects.get(codename="add_deployment"),
            Permission.objects.get(codename="change_deployment"),
            Permission.objects.get(codename="view_deployment"),

            Permission.objects.get(codename="add_channelconfiguration"),
            Permission.objects.get(codename="change_channelconfiguration"),
            Permission.objects.get(codename="view_channelconfiguration"),

            Permission.objects.get(codename="add_hydrophone"),
            Permission.objects.get(codename="change_hydrophone"),
            Permission.objects.get(codename="view_hydrophone"),

            Permission.objects.get(codename="add_recorder"),
            Permission.objects.get(codename="change_recorder"),
            Permission.objects.get(codename="view_recorder"),

            Permission.objects.get(codename="add_file"),
            Permission.objects.get(codename="change_file"),
            Permission.objects.get(codename="view_file"),
        )
