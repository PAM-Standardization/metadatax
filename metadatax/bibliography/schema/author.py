from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet
from graphene import relay
from graphene_django import DjangoObjectType

from metadatax.bibliography.models import Author


class AuthorFilter(FilterSet):
    institutions = NumberFilter()

    class Meta:
        model = Author
        fields = {
            "id": ["exact", "in"],
            "order": ["exact", "lt", "lte", "gt", "gte"],
            "bibliography_id": ["exact", "in"],
            "contact_id": ["exact", "in"],
            "institutions": ["exact", "in"],
        }


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"
        filterset_class = AuthorFilter
        interfaces = (relay.Node,)
