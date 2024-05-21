"""Website views"""

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets

from meta_auth.form import SignupForm
from metadatax.models import Deployment
from metadatax.serializers.acquisition import DeploymentSerializer


class WebsiteView(viewsets.ViewSet):

    @cache_page(60 * 15)
    @csrf_protect
    def home(self):
        return render(self, 'home.html', {
            'register_form': SignupForm(),
            'isConnected': self.user.is_staff
        })

    def map(self):
        data = []
        deployment = Deployment.objects.all()
        deployment_serialized = DeploymentSerializer(deployment, many=True).data
        for x in deployment_serialized:
            d = {}
            for k in x.items():
                key = k[0]
                d[key] = str(k[1])
            d['period'] = d['recovery_date'].split('T')[0] + ' to ' + d['deployment_date'].split('T')[0]
            data.append(d)
        return render(self, 'map.html', {"data": data, "deployment": deployment})
