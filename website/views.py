"""Website views"""

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets

from meta_auth.form import SignupForm
from metadatax.acquisition.serializers import DeploymentExportSerializer
from metadatax.acquisition.views import DeploymentViewSet, ProjectViewSet


class WebsiteView(viewsets.ViewSet):
    @cache_page(60 * 15)
    @csrf_protect
    def home(self):
        return render(
            self,
            "home.html",
            {"register_form": SignupForm(), "isConnected": self.user.is_staff},
        )

    def map(self):
        deployments = DeploymentExportSerializer(
            DeploymentViewSet.queryset.prefetch_related(
                "channel_configurations",
                "mobile_positions",
            ),
            many=True,
        ).data
        projects = ProjectViewSet.serializer_class(
            ProjectViewSet.queryset, many=True
        ).data
        return render(
            self,
            "map.html",
            {
                "deployments": deployments,
                "projects": projects,
            },
        )
