from django.urls import path, include
from rest_framework import routers

from metadatax.acquisition.views import (
    DeploymentViewSet,
    ProjectViewSet,
    SiteViewSet,
    CampaignViewSet,
    DeploymentMobilePositionViewSet,
    ChannelConfigurationViewSet,
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
router.register(
    r"channel-configuration",
    ChannelConfigurationViewSet,
    basename="channel-configuration",
)

urlpatterns = [
    path(r"acquisition/", include(router.urls)),
]
