from rest_framework import serializers


class SimpleSerializer(serializers.ModelSerializer):
    """Serializer meant to output basic data"""

    class Meta:
        model = None
        fields = "__all__"


class EnumField(serializers.ChoiceField):
    """Serializer for enums"""

    def __init__(self, enum, **kwargs):
        self.enum = enum
        self.choices = enum.choices
        kwargs["choices"] = [(e.name, e.name) for e in enum]
        super().__init__(**kwargs)

    def to_representation(self, value):
        return self.enum(value).label

    def to_internal_value(self, data):

        index = self.enum.labels.index(data)
        value = self.enum.values[index]
        try:
            return self.enum(value)
        except KeyError:
            return self.fail("invalid_choice", input=data)
