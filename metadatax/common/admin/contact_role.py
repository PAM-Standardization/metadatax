from django import forms
from django.contrib import admin

from metadatax.common.models import ContactRole


class ContactRoleForm(forms.ModelForm):
    role = forms.ChoiceField(choices=ContactRole.Type.choices, widget=forms.RadioSelect)

    class Meta:
        model = ContactRole
        fields = "__all__"


@admin.register(ContactRole)
class ContactRoleAdmin(admin.ModelAdmin):
    """Contact role administration"""

    list_display = [
        "id",
        "contact",
        "institution",
        "role",
    ]
    search_fields = [
        "contact__first_name",
        "contact__last_name",
        "contact__mail",
        "contact__website",
        "institution__name",
        "institution__mail",
        "institution__website",
    ]
    list_filter = [
        "role",
    ]
    autocomplete_fields = [
        "contact",
        "institution",
    ]
    form = ContactRoleForm
