import graphene

from metadatax.acquisition.schema import AcquisitionQuery
from metadatax.common.schema import CommonQuery
from metadatax.data.schema import DataQuery
from metadatax.equipment.schema import EquipmentQuery
from metadatax.ontology.schema import OntologyQuery


class Query(
    CommonQuery,
    AcquisitionQuery,
    DataQuery,
    EquipmentQuery,
    OntologyQuery,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query)
