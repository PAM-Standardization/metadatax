from django.contrib import admin

from metadatax.acquisition.models import Deployment
from metadatax.common.forms.contact_relation import ContactRelationForm


class DeploymentContactForm(ContactRelationForm):
    class Meta:
        model = Deployment.contacts.through
        fields = ("role", "contact")


class DeploymentContactInline(admin.TabularInline):
    model = Deployment.contacts.through
    extra = 0
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'
    form = DeploymentContactForm
