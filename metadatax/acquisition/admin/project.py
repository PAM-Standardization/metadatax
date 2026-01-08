from django import forms
from django.contrib import admin
from django.forms import widgets
from django.utils.safestring import mark_safe
from django_extended.admin import JSONExportModelAdmin

from metadatax.acquisition.models import Project, Financing
from metadatax.acquisition.serializers import ProjectExportSerializer
from metadatax.common.models import Accessibility
from .inlines import CampaignInline, SiteInline, ProjectContactInline


class ProjectForm(forms.ModelForm):
    accessibility = forms.CharField(
        widget=widgets.RadioSelect(choices=Accessibility.choices)
    )

    financing = forms.CharField(required=False, widget=widgets.RadioSelect(choices=Financing.choices))

    class Meta:
        model = Project
        fields = "__all__"


@admin.register(Project)
class ProjectAdmin(JSONExportModelAdmin):
    """Project presentation in DjangoAdmin"""

    serializer = ProjectExportSerializer
    form = ProjectForm
    list_display = [
        "name",
        "list_contacts",
        "accessibility",
        "doi",
        "project_type",
        "project_goal",
        "start_date",
        "end_date",
        "financing",
        "list_campaigns",
        "list_sites",
    ]
    search_fields = [
        "name",
        "project_goal",
        "doi",
    ]
    list_filter = [
        "accessibility",
        "project_type",
    ]
    filter_horizontal = [
        "related_bibliography",
    ]
    exclude = ("contacts",)
    inlines = [
        ProjectContactInline,
        CampaignInline,
        SiteInline,
    ]
    autocomplete_fields = [
        "project_type",
    ]

    @admin.display(description="Contacts")
    def list_contacts(self, obj: Project) -> str:
        """Display readable list of responsible_parties"""
        return mark_safe("<br/>".join([str(role) for role in obj.contacts.all()]))

    @admin.display(description="Campaigns")
    def list_campaigns(self, obj: Project) -> str:
        return mark_safe("<br/>".join([c.name for c in obj.campaigns.all()]))

    @admin.display(description="Sites")
    def list_sites(self, obj: Project) -> str:
        return mark_safe("<br/>".join([s.name for s in obj.sites.all()]))
