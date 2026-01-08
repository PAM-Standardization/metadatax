from django.contrib import admin

from metadatax.acquisition.models import Project
from metadatax.common.forms import ContactRelationForm


class ProjectContactForm(ContactRelationForm):
    class Meta:
        model = Project.contacts.through
        fields = ("role", "contact")


class ProjectContactInline(admin.TabularInline):
    model = Project.contacts.through
    extra = 0
    min_num = 1
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'
    form = ProjectContactForm
