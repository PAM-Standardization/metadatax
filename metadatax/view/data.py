from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, serializers
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from metadatax.models.data import File
from metadatax.serializers.data import DataAPIParametersSerializer
from django.shortcuts import HttpResponse
from django.core import serializers as sz
from rest_framework import status
from rest_framework.generics import GenericAPIView


class GetAllData(GenericAPIView):
        @swagger_auto_schema(operation_description="Get all file data ",query_serializer=DataAPIParametersSerializer)
        @staticmethod
        def get(self):
            print("-----------------Getting Data-------------------")
            return HttpResponse(sz.serialize("json", File.objects.all()))


class SaveDataAPI(GenericAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    @swagger_auto_schema(operation_description='create Audio file', )
    @action(detail=False, methods=['post'], name='file', url_path='create-audio-file')
    def post(self, request):
        serializer = self(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
