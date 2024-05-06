from django.shortcuts import redirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, serializers
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView
from metadatax.models.data import (File)
from django.urls import URLPattern, URLResolver
import json
import re
from django.shortcuts import render
from metadatax.models.acquisition import ChannelConfiguration, Deployment
import metadatax.serializers.acquisition as sz
import metadatax.view.acquisition as acq
import requests
#Show position of deployment on world map
class Metadatax(object):
    def metadatax(self):
        data =[]
        # deployment =[x.get('fields') for x in json.loads(acq.GetAllDeployment().get(self).content)]
        # print(deployment)
        deployment = Deployment.objects.all()
        print(deployment)
        deploymentserializer = sz.DeploymentSerializer(deployment, many=True).data
        for  x in deploymentserializer:
            d={}
            for k in x.items():
                key = k[0]
                d[key] = str(k[1])
            d['period'] = d['recovery_date'].split('T')[0] + ' to '+d['deployment_date'].split('T')[0]
            data.append(d)
        print(data)
        return render(self, 'map.html', {"data":data, "deployment":deployment})


        # data =[]
        # # institution =[x for x in json.loads(acq.GetAllInstitution().get(self).content)]
        # # deployment =[x.get('fields') for x in json.loads(acq.GetAllDeployment().get(self).content)]
        # deployment = Deployment.objects.all()
        # institution = Institution.objects.all()
        # # print(deployment)
        # # print(institution)
        #
        #
        # # print(sz.DeploymentSerializer(deployment, many=True))
        # print(sz.InstitutionSerializer(institution, many=True).data)
        # # deploymentserializer = sz.DeploymentSerializer(deployment, many=True)
        # # print(deploymentserializer)
        # institution= sz.InstitutionSerializer(institution, many=True).data
        # for  x in institution:
        #     d={}
        #     for k in x.items():
        #         key = k[0]
        #         d[key] = str(k[1])
        #         if 'deployments' in k[0]:
        #             print(k[1])
        #             for i in k[1]:
        #                 for j in i.items():
        #                     key = j[0]
        #                     d[key] = str(j[1])
        #     print(d)
        #     data.append(d)
        # print(json.loads(str(data)))
        # return render(self, 'map.html', {"data":data })