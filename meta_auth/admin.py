"""Meta_auth administration"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase

from .models import User


class UserAdmin(UserAdminBase):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'institution', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdmin)
