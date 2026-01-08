from django.contrib import admin

from metadatax.acquisition.models import Site


class SiteInline(admin.TabularInline):
    model = Site
    extra = 0
