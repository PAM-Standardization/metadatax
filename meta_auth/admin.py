"""Meta_auth administration"""

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as UserAdminBase

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


admin.site.register(User, UserAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
