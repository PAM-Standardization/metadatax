from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.contenttypes.models import ContentType
from django.forms.utils import ErrorList
from django_extension.forms import ExtendedForm
from metadatax.common.models import Tag, TaggedItem


class TaggedItemForm(ExtendedForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=FilteredSelectMultiple(
            verbose_name="Tags",
            is_stacked=False,
        ),
        required=False
    )

    class Meta:
        abstract = True

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        if instance is not None:
            self.fields['tags'].initial = Tag.objects.filter(
                tagged_items__item_id=instance.id,
                tagged_items__item_type=ContentType.objects.get_for_model(instance),
            )

    def save(self, commit=True):
        tag: Tag
        for tag in self.cleaned_data['tags']:
            TaggedItem.objects.get_or_create(tag=tag, item=self.instance)
        return super().save(commit)
