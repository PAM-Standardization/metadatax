from django.urls import path, include
from rest_framework import routers

from ontology.views import (
    LabelViewSet,
    SourceViewSet,
    SoundViewSet,
    PhysicalDescriptorViewSet,
)

router = routers.DefaultRouter()
router.register(r"source", SourceViewSet, basename="source")
router.register(r"sound", SoundViewSet, basename="sound")
router.register(r"label", LabelViewSet, basename="label")
router.register(
    r"physical-descriptor", PhysicalDescriptorViewSet, basename="physical-descriptor"
)

urlpatterns = [
    path(r"", include(router.urls)),
]
