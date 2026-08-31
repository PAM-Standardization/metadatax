import graphene

from metadatax.utils.custom_fields.byte import ByteUnitEnum


class RecorderSpecificationInput(graphene.InputObjectType):
    channels_count = graphene.Int(required=False)
    storage_slots_count = graphene.Int(required=False)
    storage_type = graphene.String(required=False)
    storage_maximum_capacity_amount = graphene.Int(required=False)
    storage_maximum_capacity_unit = ByteUnitEnum()
