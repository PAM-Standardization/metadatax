from django.urls import path, include
from rest_framework import routers

from metadatax.common.views import (
    PersonViewSet,
    InstitutionViewSet,
    TeamViewSet,
)

router = routers.DefaultRouter()
router.register(r"institution", InstitutionViewSet, basename="institution")
router.register(r"team", TeamViewSet, basename="team")
router.register(r"person", PersonViewSet, basename="person")

urlpatterns = [
    path(r"", include(router.urls)),
]
