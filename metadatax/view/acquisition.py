"""Acquisition models for metadata app"""
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
# from rest_framework.views import GenericAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from metadatax.models.acquisition import ChannelConfiguration, Deployment, Project, Institution
from metadatax.serializers.acquisition import ProjectAPIParametersSerializer, InstitutionAPIParametersSerializer, \
    ChannelConfigurationAPIParametersSerializer,DeploymentAPIParametersSerializer, CreateInstitutionAPIParametersSerializer,\
    CreateProjectAPIParametersSerializer,CreateDeploymentAPIParametersSerializer, CreateChannelConfigurationAPIParametersSerializer
from django.core import serializers as sz
from rest_framework import status


def create_item(self, request):
    serializer = self(data=request.query_params)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# """Data acquisition project"""
class GetAllProject(GenericAPIView):
    @swagger_auto_schema(operation_description="Get all project")
    @staticmethod
    def get(self):
        print("-----------------Getting Project-------------------")
        return HttpResponse(sz.serialize("json", Project.objects.all()), status=status.HTTP_200_OK)


class GetProjectByName(GenericAPIView):
    @swagger_auto_schema(operation_description="Get project by name",query_serializer=ProjectAPIParametersSerializer)
    def get(self, request):
        print("-----------------Getting ProjectByName-------------------", request.query_params.get("project_name"))
        return  HttpResponse(sz.serialize("json", Project.objects.filter(name=request.query_params.get("project_name"))), status=status.HTTP_200_OK)

class CreateProject(GenericAPIView):
    @swagger_auto_schema(operation_description='Create new Project',query_serializer=CreateProjectAPIParametersSerializer )
    @action(detail=False, methods=['post'], name='create_project', url_path='create-project')
    def post(self, request):
        return create_item(CreateProjectAPIParametersSerializer,request)

# """Institution"""
class GetAllInstitution(GenericAPIView):
        @swagger_auto_schema(operation_description="Get All Institution")
        @staticmethod
        def get(self):
            print("-----------------Getting Institution-------------------")
            return HttpResponse(sz.serialize("json", Institution.objects.all()), status=status.HTTP_200_OK)

class GetInstitutionByName(GenericAPIView):
    @swagger_auto_schema(operation_description="Get InsitutionByName",query_serializer=InstitutionAPIParametersSerializer)
    def get(self, request):
        print("-----------------Getting InstitutionByName-------------------", request.query_params.get("institution_name"))
        return HttpResponse(sz.serialize("json", Institution.objects.get(request.query_params.get("institution_name"))), status=status.HTTP_200_OK)

class CreateInstitution(GenericAPIView):
    @swagger_auto_schema(operation_description='Create new institution',query_serializer=CreateInstitutionAPIParametersSerializer )
    @action(detail=False, methods=['post'], name='create_institution', url_path='create-institution')
    def post(self, request):
        return create_item(CreateInstitutionAPIParametersSerializer, request)


# """Material deployment for data acquisition"""
class GetAllDeployment(GenericAPIView):
    @swagger_auto_schema(operation_description= "Get all deployment")
    @staticmethod
    def get(self):
        print("-----------------Getting Deployment-------------------")
        return  HttpResponse(sz.serialize("json", Deployment.objects.all()), status=status.HTTP_200_OK)

class GetDeploymentByName(GenericAPIView):
    @swagger_auto_schema(operation_description="Get DeploymentByName", query_serializer=DeploymentAPIParametersSerializer)
    def get(self, request):
        print("-----------------Getting DeploymentByName-------------------", request.query_params.get("deployment_name"))
        return HttpResponse(sz.serialize("json",Deployment.objects.get(request.query_params.get("deployment_name"))), status=status.HTTP_200_OK)

class CreateDeployment(GenericAPIView):
    @swagger_auto_schema(operation_description='Create new deployment',query_serializer=CreateDeploymentAPIParametersSerializer )
    @action(detail=False, methods=['post'], name='create_deployment', url_path='create-deployment')
    def post(self, request):
       return create_item(CreateDeploymentAPIParametersSerializer,request)

# """Configuration of a recorded channel for a Hydrophone on a Recorder in a deployment"""
class GetAllChannelConfigurationAPI(GenericAPIView):
    @swagger_auto_schema(operation_description='Get ALL ChannelConfiguration')
    @staticmethod
    def get(self):
        print("-----------------Getting ChannelConfiguration-------------------")
        return  HttpResponse(sz.serialize("json", ChannelConfiguration.objects.all()), status=status.HTTP_200_OK)

class GetChannelConfigurationAPIByChannelName(GenericAPIView):
    @swagger_auto_schema(operation_description='Get ChannelConfigurationByName',query_serializer=ChannelConfigurationAPIParametersSerializer)
    def get(self, request):
        print("-----------------Getting ChannelConfigurationByName-------------------", request.query_params.get("channel_name"))
        return  HttpResponse(sz.serialize("json", ChannelConfiguration.objects.get(request.query_params.get("channel_name"))), status=status.HTTP_200_OK)

class CreateChannelConfiguration(GenericAPIView):
    @swagger_auto_schema(operation_description='Create new Channel Configuration',query_serializer=CreateChannelConfigurationAPIParametersSerializer )
    @action(detail=False, methods=['post'], name='create_channel_configuration', url_path='create-channel-configuration')
    def post(self, request):
       return create_item(CreateChannelConfigurationAPIParametersSerializer,request)