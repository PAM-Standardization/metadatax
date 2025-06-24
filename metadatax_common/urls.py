from django.urls import path, include
from rest_framework import routers

from metadatax_common.views import ContactRoleViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r"contact", ContactViewSet, basename="contact")
router.register(r"contact/role", ContactRoleViewSet, basename="contact-role")

urlpatterns = [
    path(r"", include(router.urls)),
]
