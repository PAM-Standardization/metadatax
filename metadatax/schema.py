import graphene
from graphene_django.debug import DjangoDebug

from metadatax.acquisition.schema import AcquisitionQuery, AcquisitionMutation
from metadatax.bibliography.schema import BibliographyQuery, BibliographyTypeEnum, BibliographyStatusEnum
from metadatax.common.schema import CommonQuery, RoleEnum, CommonMutation
from metadatax.data.schema import DataQuery, DataMutation
from metadatax.equipment.schema import EquipmentQuery, EquipmentMutation
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


class Mutation(
    CommonMutation,
    AcquisitionMutation,
    OntologyMutation,
    EquipmentMutation,
    DataMutation,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation, types=[
    RoleEnum,
    BibliographyTypeEnum,
    BibliographyStatusEnum,
])
