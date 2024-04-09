from .views import Metadatax
from django.urls import path
urlpatterns = [
    path("", Metadatax.metadatax, name="metadatax")
]