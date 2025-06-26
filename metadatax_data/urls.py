from django.urls import path, include
from rest_framework import routers

from metadatax_data.views.file import FileViewSet

router = routers.DefaultRouter()
router.register(r"file", FileViewSet, basename="file")

urlpatterns = [
    path(r"", include(router.urls)),
]
