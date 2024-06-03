"""Website views"""

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets

from meta_auth.form import SignupForm
from metadatax.models.acquisition import Deployment, ChannelConfiguration
from metadatax.serializers.acquisition import DeploymentSerializer, ChannelConfigurationSerializer


class WebsiteView(viewsets.ViewSet):

    @cache_page(60 * 15)
    @csrf_protect
    def home(self):
        return render(self, 'home.html', {
            'register_form': SignupForm(),
            'isConnected': self.user.is_staff
        })

    def map(self):
        channels = ChannelConfigurationSerializer(ChannelConfiguration.objects.all(), many=True).data
        return render(self, 'map.html', {
          "channels": channels
        })

