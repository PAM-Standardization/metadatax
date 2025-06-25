from django.urls import path, include
from rest_framework import routers

from metadatax_acquisition.views import (
    DeploymentViewSet,
    ProjectViewSet,
    SiteViewSet,
    CampaignViewSet,
    DeploymentMobilePositionViewSet,
)

router = routers.DefaultRouter()
router.register(r"project", ProjectViewSet, basename="project")
router.register(r"site", SiteViewSet, basename="site")
router.register(r"campaign", CampaignViewSet, basename="campaign")
router.register(r"deployment", DeploymentViewSet, basename="deployment")
router.register(
    r"deployment/mobile-position",
    DeploymentMobilePositionViewSet,
    basename="deployment-mobile-position",
)

urlpatterns = [
    path(r"", include(router.urls)),
]
