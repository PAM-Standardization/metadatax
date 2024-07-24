from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from metadatax.view.acquisition import (
    InstitutionViewSet,
    ProjectViewSet,
    DeploymentViewSet,
    ChannelConfigurationViewSet,
)
from metadatax.view.equipment import (
    HydrophoneViewSet,
    RecorderViewSet,
)
from metadatax.view.data import FileViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Metadatax API",
        default_version="v1",
        description="Metadatax endpoint API",
    )
)

router = routers.DefaultRouter()
router.register(r"institution", InstitutionViewSet, basename="institution")
router.register(r"project", ProjectViewSet, basename="project")
router.register(r"deployment", DeploymentViewSet, basename="deployment")
router.register(
    r"channel-configuration",
    ChannelConfigurationViewSet,
    basename="channel-configuration",
)
router.register(r"hydrophone", HydrophoneViewSet, basename="hydrophone")
router.register(r"recorder", RecorderViewSet, basename="recorder")
router.register(r"file", FileViewSet, basename="file")

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(r"", include(router.urls)),
]
