import graphene

from metadatax.acquisition.schema import AcquisitionQuery
from metadatax.bibliography.schema import BibliographyQuery
from metadatax.common.schema import CommonQuery
from metadatax.data.schema import DataQuery
from metadatax.equipment.schema import EquipmentQuery
from metadatax.ontology.schema import OntologyQuery, OntologyMutation


class Query(
    CommonQuery,
    AcquisitionQuery,
    DataQuery,
    EquipmentQuery,
    BibliographyQuery,
    OntologyQuery,
    graphene.ObjectType,
):
    pass


class Mutation(OntologyMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
