from django.shortcuts import redirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, serializers
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView
from metadatax.models.data import (File)

class Metadatax(object):
    def metadatax(self):
        return redirect('/admin/login/?next=/admin/')


