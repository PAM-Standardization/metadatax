from metadatax.view.data import GetAllData, SaveDataAPI
from metadatax.view.acquisition import GetAllProject, GetProjectByName,GetAllDeployment,GetDeploymentByName,GetAllChannelConfigurationAPI,\
    GetChannelConfigurationAPIByChannelName, GetAllInstitution, GetInstitutionByName, CreateInstitution, CreateProject, CreateChannelConfiguration, CreateDeployment
from metadatax.view.equipment import  GetAllRecorder, GetRecorderByName, GetAllHydrophone,GetHydrophoneByName, CreateRecorder, CreateHydrophone


from .views import Metadatax
from django.urls import path, include
from rest_framework import permissions,authentication
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# schema_view = SpectacularSwaggerView(
#     openapi.Info(
#         title="Metadatax API",
#         default_version='v1',
#         description="Metadatax endpoint API"
#     )
#     # authentication_classes=[authentication.SessionAuthentication ]
# )


urlpatterns = [
    path("", Metadatax.metadatax, name="metadatax"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    path('project/', include([
        path('get_all/',GetAllProject.as_view(), name='get_all_project'),
        path('get_name/',GetProjectByName.as_view(), name='get_name_project'),
        path('create_project/', CreateProject.as_view(), name='create-project'),
    ])),
    path('deployment/', include([
        path('get_all/',GetAllDeployment.as_view(), name='get_all_deployment'),
        path('get_name/', GetDeploymentByName.as_view(), name='get_name_deployment'),
        path('create_deployment/', CreateDeployment.as_view(), name='create-deployment')
    ])),
    path('institution/', include([
        path('get_all/', GetAllInstitution.as_view(), name='get_all_institution'),
        path('get_name/', GetInstitutionByName.as_view(), name='get_institution_by_name'),
        path('create_institution/',CreateInstitution.as_view(), name='create-institution')
    ])),
    path('channelConfiguration/', include([
        path('get_all/', GetAllChannelConfigurationAPI.as_view(), name='get_all_channel_configuration'),
        path('get_name/', GetChannelConfigurationAPIByChannelName.as_view(), name='get_channel_configuration_by_name'),
        path('create_channel_configuration/', CreateChannelConfiguration.as_view(), name='create-channel-configuration')
    ])),
    path('recorder/', include([
        path('get_all/', GetAllRecorder.as_view(), name='get_all_recorder'),
        path('get_name/', GetRecorderByName.as_view(), name='get_recorder_by_name'),
        path('create_recorder/', CreateRecorder.as_view(), name='create-recorder')
    ])),
    path('hydrophone/', include([
        path('get_all/', GetAllHydrophone.as_view(), name='get_all_hydrophone' ),
        path('get_name/', GetHydrophoneByName.as_view(), name='get_hydrophone_by_name'),
        path('create_hydrophone/', CreateHydrophone.as_view(), name='create-hydrophone')
    ])),
    path('data/', include([
        path('get_all/', GetAllData.as_view(), name='file_api_endpoint'),
        path('get_name/',SaveDataAPI.as_view(), name='file_api_endpoint')]))
]