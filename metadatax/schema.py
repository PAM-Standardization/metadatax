import graphene
from graphene_django.debug import DjangoDebug

from metadatax.acquisition.schema import AcquisitionQuery
from metadatax.bibliography.schema import BibliographyQuery, BibliographyTypeEnum, BibliographyStatusEnum
from metadatax.common.schema import CommonQuery, RoleEnum
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
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(OntologyMutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation, types=[
    RoleEnum,
    BibliographyTypeEnum,
    BibliographyStatusEnum,
])
