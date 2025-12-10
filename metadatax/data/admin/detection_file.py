from django import forms
from django.contrib import admin
from django.forms import widgets
from django.forms.utils import ErrorList

from metadatax.common.models import Accessibility
from metadatax.data.models import DetectionFile, DetectionProperties


class DetectionFileForm(forms.ModelForm):
    accessibility = forms.CharField(
        widget=widgets.RadioSelect(choices=Accessibility.choices)
    )

    start = DetectionProperties._meta.get_field("start").formfield()
    end = DetectionProperties._meta.get_field("end").formfield()

    class Meta:
        model = DetectionFile
        fields = "__all__"

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance: DetectionFile = None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        if instance is None:
            return

        self.fields['start'].initial = instance.detection_properties.start
        self.fields['end'].initial = instance.detection_properties.end

    def save(self, commit=True):
        super().save(commit)

        if self.instance.detection_properties is None:
            self.instance.detection_properties = DetectionProperties.objects.create(
                start=self.cleaned_data['start'],
                end=self.cleaned_data['end'],
            )
            self.instance.save()
        else:
            self.instance.detection_properties.start = self.cleaned_data['start']
            self.instance.detection_properties.end = self.cleaned_data['end']
            self.instance.detection_properties.save()

        return self.instance


@admin.register(DetectionFile)
class DetectionFileAdmin(admin.ModelAdmin):
    form = DetectionFileForm
    list_display = [
        "filename",
        "format",
        "storage_location",
        "file_size",
        "accessibility",
        "start",
        "end",
    ]
    search_fields = [
        "filename",
        "storage_location",
    ]
    list_filter = [
        "format",
        "accessibility",
    ]
    autocomplete_fields = [
        "format",
    ]

    @admin.display(description="Start")
    def start(self, obj: DetectionFile):
        return obj.detection_properties.start

    @admin.display(description="End")
    def end(self, obj: DetectionFile):
        return obj.detection_properties.end
