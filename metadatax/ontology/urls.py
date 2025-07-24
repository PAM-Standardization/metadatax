from django.urls import path, include
from rest_framework import routers

from metadatax.ontology.views import (
    LabelViewSet,
    SourceViewSet,
    SoundViewSet,
)

router = routers.DefaultRouter()
router.register(r"source", SourceViewSet, basename="source")
router.register(r"sound", SoundViewSet, basename="sound")
router.register(r"label", LabelViewSet, basename="label")

urlpatterns = [
    path("", include(router.urls)),
]
