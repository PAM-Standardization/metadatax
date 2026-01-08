from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet, Exists, OuterRef
from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from django.utils.translation import gettext_lazy as _

from metadatax.common.models import Tag, TaggedItem


class TaggedFilter(MultipleChoiceListFilter):
    title = _("Tag")
    parameter_name = "tag__in"

    def lookups(self, request, model_admin):
        return [
            (t.id, str(t))
            for t in Tag.objects.all()
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() is None:
            return queryset
        return queryset.filter(
            Exists(
                TaggedItem.objects.filter(
                    tag_id__in=self.value_as_list(),
                    item_type=ContentType.objects.get_for_model(queryset.model),
                    item_id=OuterRef("pk"),
                )
            )
        )
