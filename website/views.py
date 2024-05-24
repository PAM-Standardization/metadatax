"""Website views"""

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
import random

from meta_auth.form import SignupForm
from metadatax.models.acquisition import (
    Institution,
    Project,
    Deployment,
    ChannelConfiguration
)
from metadatax.serializers.acquisition import DeploymentSerializer,DeploymentGlobalSerializer,ProjectSerializer, DeploymentLightSerializer


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
        tooltip = []
        popup = []
        deployment = Deployment.objects.all().order_by("project__name")
        deployment_serialized = DeploymentSerializer(deployment, many=True).data
        #Dict for tooltip on deployment point: Need project name ; responsible parties, campaing/deployment name, platform type, Latitude, Longitude, , period color
        r = lambda: random.randint(0, 255)
        last_project = ""
        for x in deployment_serialized:
            d = {}
            tooltip_dict = {}
            popup_dict = {}
            for k in x.items():
                key = k[0]
                d[key] = str(k[1])
            # Build of tootltip
            tooltip_dict['Project Name'] = d['project']
            tooltip_dict['Responsible parties'] =d['provider']
            tooltip_dict['Campaign name'] =d['campaign']
            tooltip_dict['Deployment name'] =d['name']
            tooltip_dict['Period'] = d['recovery_date'].split('T')[0] + ' to ' + d['deployment_date'].split('T')[0]
            tooltip_dict['Latitude'] =d['latitude']
            tooltip_dict['Longitude'] =d['longitude']
            #TODO Color Feature : Tester la conversion string->byte du champ "projet"; puis découper le byte en 3 , normaliser en 255 et convertir en RGB.
            # A tester si plusieurs projet voir si les différences de couleurs sont notables. si non utilisé un coeff multplicateur pour "forcer" la diversité des couleurs.
            # byte_obj =tooltip_dict['Project Name'].encode('ascii')
            # tooltip_dict['Color'] ='#%02x%02x%02x' % (byte_obj[0], byte_obj[1], byte_obj[2])
            tooltip_dict['Color'] =  '#%02X%02X%02X' % (r(), r(), r()) if d['project'] != last_project else last_color
            last_color = tooltip_dict['Color']
            last_project = d['project']
            ####

            data.append(d)
            tooltip.append(tooltip_dict)

        popup_as_json =DeploymentGlobalSerializer(deployment, many=True).data

        return render(self, 'map.html', {"data": data,  "tooltip":tooltip,"popup_as_json":popup_as_json})

