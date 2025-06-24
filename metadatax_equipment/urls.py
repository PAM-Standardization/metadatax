from django.urls import path, include
from rest_framework import routers

from metadatax_equipment.views import (
    PlatformViewSet,
)

router = routers.DefaultRouter()
router.register(r"platform", PlatformViewSet, basename="platform")

urlpatterns = [
    path(r"", include(router.urls)),
]
