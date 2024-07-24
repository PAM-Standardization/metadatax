from django.urls import path

from website.views import WebsiteView

urlpatterns = [
    path("", WebsiteView.home, name="home"),
    path("map/", WebsiteView.map, name="map"),
]
