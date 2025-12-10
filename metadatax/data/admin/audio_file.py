from django import forms
from django.contrib import admin
from django.forms import widgets
from django.forms.utils import ErrorList

from metadatax.common.models import Accessibility
from metadatax.data.models import AudioFile, AudioProperties


class AudioFileForm(forms.ModelForm):
    accessibility = forms.CharField(
        widget=widgets.RadioSelect(choices=Accessibility.choices)
    )

    sampling_frequency = AudioProperties._meta.get_field("sampling_frequency").formfield()
    initial_timestamp = AudioProperties._meta.get_field("initial_timestamp").formfield()
    duration = AudioProperties._meta.get_field("duration").formfield()
    sample_depth = AudioProperties._meta.get_field("sample_depth").formfield()

    class Meta:
        model = AudioFile
        fields = "__all__"

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance: AudioFile = None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        if instance is None:
            return

        self.fields['sampling_frequency'].initial = instance.audio_properties.sampling_frequency
        self.fields['initial_timestamp'].initial = instance.audio_properties.initial_timestamp
        self.fields['duration'].initial = instance.audio_properties.duration
        self.fields['sample_depth'].initial = instance.audio_properties.sample_depth

    def save(self, commit=True):
        super().save(commit)

        if self.instance.audio_properties is None:
            self.instance.audio_properties = AudioProperties.objects.create(
                sampling_frequency=self.cleaned_data['sampling_frequency'],
                initial_timestamp=self.cleaned_data['initial_timestamp'],
                duration=self.cleaned_data['duration'],
                sample_depth=self.cleaned_data['sample_depth'],
            )
            self.instance.save()
        else:
            self.instance.audio_properties.sampling_frequency = self.cleaned_data['sampling_frequency']
            self.instance.audio_properties.initial_timestamp = self.cleaned_data['initial_timestamp']
            self.instance.audio_properties.duration = self.cleaned_data['duration']
            self.instance.audio_properties.sample_depth = self.cleaned_data['sample_depth']
            self.instance.audio_properties.save()

        return self.instance


@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    form = AudioFileForm
    list_display = [
        "filename",
        "format",
        "storage_location",
        "file_size",
        "accessibility",
        "sampling_frequency",
        "initial_timestamp",
        "duration",
        "sample_depth",
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

    @admin.display(description="Sampling frequency")
    def sampling_frequency(self, obj: AudioFile):
        return obj.audio_properties.sampling_frequency

    @admin.display(description="Initial timestamp")
    def initial_timestamp(self, obj: AudioFile):
        return obj.audio_properties.initial_timestamp

    @admin.display(description="Duration")
    def duration(self, obj: AudioFile):
        return obj.audio_properties.duration

    @admin.display(description="Sampling depth")
    def sample_depth(self, obj: AudioFile):
        return obj.audio_properties.sample_depth
