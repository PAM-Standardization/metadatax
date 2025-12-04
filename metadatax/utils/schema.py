import graphene
import graphene_django_optimizer as gql_optimizer
from graphene import ID
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from rest_framework import serializers


class MxObjectType(DjangoObjectType):
    """Dataset schema"""

    id = ID(required=True)

    class Meta:
        # pylint: disable=missing-class-docstring, too-few-public-methods
        abstract = True

    @classmethod
    def get_queryset(cls, queryset, info):
        return gql_optimizer.query(queryset, info)


class PostMutation(SerializerMutation):
    class Meta:
        abstract = True

    ok = graphene.Boolean()

    @classmethod
    def __init_subclass_with_meta__(
            cls,
            lookup_field=None,
            serializer_class=None,
            model_class=None,
            model_operations=("create", "update"),
            only_fields=(),
            exclude_fields=(),
            convert_choices_to_enum=True,
            _meta=None,
            optional_fields=(),
            **options
    ):
        return super().__init_subclass_with_meta__(
            lookup_field,
            serializer_class,
            model_class,
            model_operations,
            only_fields,
            exclude_fields,
            convert_choices_to_enum,
            _meta,
            optional_fields,
            **options
        )

    @classmethod
    def perform_mutate(cls, serializer, info):
        obj = serializer.save()

        kwargs = {}
        for f, field in serializer.fields.items():
            if not field.write_only:
                if isinstance(field, serializers.SerializerMethodField):
                    kwargs[f] = field.to_representation(obj)
                else:
                    kwargs[f] = field.get_attribute(obj)

        return cls(errors=None, data=obj, ok=True, **kwargs)


class DeleteMutation(graphene.Mutation):
    class Meta:
        abstract = True

    ok = graphene.Boolean()

    @classmethod
    def __init_subclass_with_meta__(
            cls,
            interfaces=(),
            resolver=None,
            output=None,
            arguments=None,
            model_class=None,
            _meta=None,
            **options
    ):
        cls.model_class = model_class
        super().__init_subclass_with_meta__(
            interfaces, resolver, output, arguments, _meta, **options
        )

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = cls.model_class.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)


class ByIdField(graphene.Field):

    def __init__(self, type_, args=None, *extra_args, **kwargs):
        super().__init__(type_, args, id=graphene.ID(required=True), resolver=self.resolve, *extra_args, **kwargs)

    def resolve(self, info, id: int):
        return self.type.get_node(info, id)
