from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from metadatax.models.data import File
from metadatax.serializers.data import DataAPIParametersSerializer
from django.shortcuts import HttpResponse
from django.core import serializers as sz



class GetAllData(APIView):
        @swagger_auto_schema(query_serializer=DataAPIParametersSerializer)
        @staticmethod
        def get(self):
            print("-----------------Getting Data-------------------")
            return HttpResponse(sz.serialize("json", File.objects.all()))


class SaveDataAPI(APIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    @swagger_auto_schema(operation_description='Upload Audio file...', )
    @action(detail=False, methods=['post'], name='file', url_path='upload-audio-file')
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data["file"])
            return Response("Success")
        return Response("Failed")