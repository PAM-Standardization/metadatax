import graphene
from graphene_django.rest_framework.mutation import SerializerMutation
from rest_framework import serializers


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
