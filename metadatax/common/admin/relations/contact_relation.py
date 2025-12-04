from django.contrib import admin

from metadatax.common.forms.relations import ContactRelationForm
from metadatax.common.models.relations import ContactRelation


class ContactRelationInline(admin.TabularInline):
    model = ContactRelation
    form = ContactRelationForm
    extra = 0
