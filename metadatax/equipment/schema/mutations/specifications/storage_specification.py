import graphene

from metadatax.utils.custom_fields.byte import ByteUnitEnum


class StorageSpecificationInput(graphene.InputObjectType):
    capacity_amount = graphene.Int(required=True)
    capacity_unit = graphene.NonNull(ByteUnitEnum)
    type = graphene.String(required=False)
