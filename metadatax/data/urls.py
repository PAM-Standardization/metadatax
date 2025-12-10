from django.urls import path, include
from rest_framework import routers

from metadatax.data.views import FileViewSet, AudioFileViewSet, DetectionFileViewSet

router = routers.DefaultRouter()
router.register(r"file", FileViewSet, basename="file")
router.register(r"file/audio", AudioFileViewSet, basename="file-audio")
router.register(r"file/detection", DetectionFileViewSet, basename="file-detection")

urlpatterns = [
    path(r"", include(router.urls)),
]
