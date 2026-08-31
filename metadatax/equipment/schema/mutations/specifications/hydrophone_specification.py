import graphene

from ...enums import HydrophoneDirectivityEnum


class HydrophoneSpecificationInput(graphene.InputObjectType):
    directivity = HydrophoneDirectivityEnum()
    operating_min_temperature = graphene.Float(required=False)
    operating_max_temperature = graphene.Float(required=False)
    min_bandwidth = graphene.Float(required=False)
    max_bandwidth = graphene.Float(required=False)
    min_dynamic_range = graphene.Float(required=False)
    max_dynamic_range = graphene.Float(required=False)
    min_operating_depth = graphene.Float(required=False)
    max_operating_depth = graphene.Float(required=False)
    noise_floor = graphene.Float(required=False)
