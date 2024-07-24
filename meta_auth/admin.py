"""Meta_auth administration"""

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet, Model
from django.http import JsonResponse
from rest_framework.serializers import ModelSerializer

from metadatax.serializers.utils import SimpleSerializer
from metadatax.utils import export
from .models import User


class UserAdmin(UserAdminBase):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "institution", "password1", "password2"),
            },
        ),
    )
    search_fields = ("username", "email", "first_name", "last_name", "institution")
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "institution",
        "is_staff",
        "accept_mailing",
    )


class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "content_type",
        "action_flag",
        "user",
        "action_time",
    )
    search_fields = (
        "object_repr",
        "user__email",
        "content_type__app_label",
        "content_type__model",
    )
    list_filter = ("action_flag",)


class JSONExportModelAdmin(admin.ModelAdmin):
    serializer: ModelSerializer.__class__ = None
    model: Model.__class__ = None
    depth: int = 0

    actions = [
        "export",
    ]

    @admin.action(description="Download data as JSON")
    def export(self, request: WSGIRequest, queryset: QuerySet):
        """Export JSON file containing serialized queryset"""
        path = request.path.split("/")
        path.pop()
        filename = path.pop()
        return export(
            filename=filename,
            queryset=queryset,
            model=self.model,
            depth=self.depth,
            serializer=self.serializer,
        )


admin.site.register(User, UserAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
