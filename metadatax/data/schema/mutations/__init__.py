from graphene import ObjectType

from .file_format import FileFormatMutation
from .visual_observation import VisualObservationMutation


class DataMutation(ObjectType):
    file_format = FileFormatMutation.Field()
    visual_observation = VisualObservationMutation.Field()
