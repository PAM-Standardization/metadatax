from django.urls import path, include
from rest_framework import routers

from metadatax.common.views import (
    ContactRoleViewSet,
    ContactViewSet,
    InstitutionViewSet,
)

router = routers.DefaultRouter()
router.register(r"contact", ContactViewSet, basename="contact")
router.register(r"contact/role", ContactRoleViewSet, basename="contact-role")
router.register(r"institution", InstitutionViewSet, basename="institution")

urlpatterns = [
    path(r"", include(router.urls)),
]
