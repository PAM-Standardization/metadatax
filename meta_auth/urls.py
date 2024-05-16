from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path("user/register/", UserViewSet.register, name="user-register"),
]
