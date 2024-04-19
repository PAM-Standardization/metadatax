"""Acquisition models for metadata app"""

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from metadatax.models.equipment import Hydrophone, Recorder
from metadatax.serializers.equipment import HydrophoneAPIParametersSerializer, RecorderAPIParametersSerializer, CreateHydrophoneAPIParametersSerializer, CreateRecorderAPIParametersSerializer
from django.core import serializers as sz
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from rest_framework import status


def create_item(self, request):
    serializer = self(data=request.query_params)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# """Recorder"""
class GetAllRecorder(APIView):
        @swagger_auto_schema()
        @staticmethod
        def get(self ):
            print("-----------------Getting Recorder-------------------")
            return HttpResponse(sz.serialize("json", Recorder.objects.all()))

class GetRecorderByName(APIView):
    @swagger_auto_schema(query_serializer=RecorderAPIParametersSerializer)
    def get(self, request):
        print("-----------------Getting RecroderByName-------------------", request.query_params.get("recorder_provider_name"))
        return HttpResponse(sz.serialize("json", Recorder.objects.get(request.query_params.get("recorder_provider_name"))))

class CreateRecorder(APIView):
    @swagger_auto_schema(operation_description='Create new institution',query_serializer=CreateRecorderAPIParametersSerializer )
    @action(detail=False, methods=['post'], name='create_institution', url_path='create-institution')
    def post(self, request):
       return create_item(CreateRecorderAPIParametersSerializer,request)


# """Hydrophone"""
class GetAllHydrophone(APIView):
    @swagger_auto_schema()
    @staticmethod
    def get(self):
        print("-----------------Getting Hydrophone-------------------")
        return HttpResponse(sz.serialize("json", Hydrophone.objects.all()))

class GetHydrophoneByName(APIView):
    @swagger_auto_schema(query_serializer=HydrophoneAPIParametersSerializer)
    def get(self, request):
        print("-----------------Getting HydrophoneByName-------------------", request.query_params.get("hydrophone_provider_name"))
        return HttpResponse(sz.serialize("json", Hydrophone.objects.get(request.query_params.get("hydrophone_provider_name"))))


class CreateHydrophone(APIView):
    @swagger_auto_schema(operation_description='Create new institution',query_serializer=CreateHydrophoneAPIParametersSerializer )
    @action(detail=False, methods=['post'], name='create_institution', url_path='create-institution')
    def post(self, request):
       return create_item(CreateHydrophoneAPIParametersSerializer,request)