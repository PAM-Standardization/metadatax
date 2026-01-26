import csv
import io
from typing import Optional

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import transaction, IntegrityError
from django_extension.forms.widgets import AdminAutocompleteSelectWidget, AdminAutocompleteSelectMultipleWidget

from metadatax.acquisition.models import ChannelConfiguration
from metadatax.acquisition.models.channel_configuration_specifications import ChannelConfigurationRecorderSpecification, \
    ChannelConfigurationDetectorSpecification
from metadatax.data.models import AudioProperties, File, FileFormat
from metadatax.equipment.models import Equipment


class ChannelConfigurationForm(forms.ModelForm):
    # Additional typing
    instance: Optional[ChannelConfiguration]

    class Meta:
        model = ChannelConfiguration
        fields = "__all__"

    # Recorder specification
    recorder = ChannelConfigurationRecorderSpecification._meta.get_field("recorder").formfield(
        queryset=Equipment.objects.filter(
            model__specification_relations__specification_type__model="RecorderSpecification".lower()
        ),
        widget=AdminAutocompleteSelectWidget(),
    )
    hydrophone = ChannelConfigurationRecorderSpecification._meta.get_field("hydrophone").formfield(
        queryset=Equipment.objects.filter(
            model__specification_relations__specification_type__model="HydrophoneSpecification".lower()
        ),
        widget=AdminAutocompleteSelectWidget()
    )
    recording_formats = ChannelConfigurationRecorderSpecification._meta.get_field("recording_formats").formfield(
        widget=AdminAutocompleteSelectMultipleWidget(),
    )
    sampling_frequency = ChannelConfigurationRecorderSpecification._meta.get_field("sampling_frequency").formfield()
    sample_depth = ChannelConfigurationRecorderSpecification._meta.get_field("sample_depth").formfield()
    gain = ChannelConfigurationRecorderSpecification._meta.get_field("gain").formfield()
    channel_name = ChannelConfigurationRecorderSpecification._meta.get_field("channel_name").formfield()

    # Detector specification
    detector = ChannelConfigurationDetectorSpecification._meta.get_field("detector").formfield(
        queryset=Equipment.objects.filter(
            model__specification_relations__specification_type__model="AcousticDetectorSpecification".lower()
        ),
        widget=AdminAutocompleteSelectWidget(),
    )
    output_formats = ChannelConfigurationDetectorSpecification._meta.get_field("output_formats").formfield(
        widget=AdminAutocompleteSelectMultipleWidget(),
    )
    labels = ChannelConfigurationDetectorSpecification._meta.get_field("labels").formfield()
    min_frequency = ChannelConfigurationDetectorSpecification._meta.get_field("min_frequency").formfield()
    max_frequency = ChannelConfigurationDetectorSpecification._meta.get_field("max_frequency").formfield()
    filter = ChannelConfigurationDetectorSpecification._meta.get_field("filter").formfield()
    configuration = ChannelConfigurationDetectorSpecification._meta.get_field("configuration").formfield()

    # Files
    csv_audio_file = forms.FileField(
        help_text="Conflicting files will be ignored. "
                  "The file should contains the following columns: "
                  "name* (file name),  "
                  "format* (file format),"
                  "initial_timestamp*, "
                  "duration*, "
                  "sampling_frequency*, "
                  "storage_location, "
                  "file_size, "
                  "accessibility (C - Confidential, R - upon Request, O - Open), "
                  "sample_depth, ",
        validators=[validators.FileExtensionValidator(["csv"])],
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is None:
            pass

        if self.instance.recorder_specification:
            self.fields['recorder'].initial = self.instance.recorder_specification.recorder
            self.fields['hydrophone'].initial = self.instance.recorder_specification.hydrophone
            self.fields['recording_formats'].initial = self.instance.recorder_specification.recording_formats.all()
            self.fields['sampling_frequency'].initial = self.instance.recorder_specification.sampling_frequency
            self.fields['sample_depth'].initial = self.instance.recorder_specification.sample_depth
            self.fields['gain'].initial = self.instance.recorder_specification.gain
            self.fields['channel_name'].initial = self.instance.recorder_specification.channel_name

        if self.instance.detector_specification:
            self.fields['detector'].initial = self.instance.detector_specification.detector
            self.fields['output_formats'].initial = self.instance.detector_specification.output_formats.all()
            self.fields['labels'].initial = self.instance.detector_specification.labels.all()
            self.fields['min_frequency'].initial = self.instance.detector_specification.min_frequency
            self.fields['max_frequency'].initial = self.instance.detector_specification.max_frequency
            self.fields['filter'].initial = self.instance.detector_specification.filter
            self.fields['configuration'].initial = self.instance.detector_specification.configuration

    def _clean_fields(self):
        print("_clean_fields")

        if not self.model_fields(ChannelConfigurationRecorderSpecification)[1]:
            self.fields['detector'].required = False
            self.fields['output_formats'].required = False
            self.fields['labels'].required = False

        if not self.model_fields(ChannelConfigurationDetectorSpecification)[1]:
            self.fields['recorder'].required = False
            self.fields['hydrophone'].required = False
            self.fields['recording_formats'].required = False
            self.fields['sampling_frequency'].required = False
            self.fields['sample_depth'].required = False
            self.fields['gain'].required = False
            pass

        super()._clean_fields()

    def model_fields(self, model: type) -> (dict, bool):
        should_exists = False
        models_fields = {}
        for field in self.cleaned_data:
            if field == 'recording_formats':
                if self.cleaned_data.get(
                        'recording_formats').exists() and model == ChannelConfigurationRecorderSpecification:
                    should_exists = True
                continue
            if field == 'output_formats':
                if self.cleaned_data.get(
                        'output_formats').exists() and model == ChannelConfigurationDetectorSpecification:
                    should_exists = True
                continue
            if field == 'labels':
                if self.cleaned_data.get('labels').exists() and model == ChannelConfigurationDetectorSpecification:
                    should_exists = True
                continue
            if field in model.__dict__ and self.cleaned_data.get(field) not in (None, ''):
                should_exists = True
                models_fields[field] = self.cleaned_data.get(field)
        return models_fields, should_exists

    @transaction.atomic
    def save(self, commit=True):
        super().save(commit)

        self.save_model(ChannelConfigurationRecorderSpecification)
        self.save_model(ChannelConfigurationDetectorSpecification)
        self.save_files()

        if commit:
            # Instance
            self.instance.save()
        return self.instance

    def save_model(self, model: type, commit=True):
        models_fields, should_exists = self.model_fields(model)

        field = None
        if model == ChannelConfigurationRecorderSpecification:
            field = "recorder_specification"
        if model == ChannelConfigurationDetectorSpecification:
            field = "detector_specification"

        if not field or not commit:
            return

        if should_exists:
            if getattr(self.instance, field):
                model.objects.filter(pk=getattr(self.instance, field).pk).update(**models_fields)
            else:
                try:
                    setattr(self.instance, field, model.objects.create(**models_fields))
                except IntegrityError as e:
                    raise ValidationError(message=str(e))
            if model == ChannelConfigurationRecorderSpecification:
                for ff in self.cleaned_data.get('recording_formats'):
                    self.instance.recorder_specification.recording_formats.add(ff)
            if model == ChannelConfigurationDetectorSpecification:
                for of in self.cleaned_data.get('output_formats'):
                    self.instance.detector_specification.output_formats.add(of)
                for l in self.cleaned_data.get('labels'):
                    self.instance.detector_specification.labels.add(l)
        else:
            if getattr(self.instance, field):
                getattr(self.instance, field).delete()

    def save_files(self, commit=True):
        csv_file: Optional[InMemoryUploadedFile] = self.cleaned_data.get(
            "csv_file", None
        )
        if csv_file is None:
            return

        content = csv_file.read().decode("utf-8")
        audio_properties: list[AudioProperties] = []
        files: list[File] = []
        file: dict
        for file in csv.DictReader(io.StringIO(content)):
            _format, _ = FileFormat.objects.get_or_create(
                name=str(file["format"]).upper()
            )
            audio = AudioProperties(
                sampling_frequency=file["sampling_frequency"],
                initial_timestamp=file["initial_timestamp"],
                duration=file["duration"],
                sample_depth=file["sample_depth"],
            )
            audio_properties.append(audio)
            files.append(
                File(
                    filename=file["name"],
                    format=_format,
                    audio_properties=audio,
                    storage_location=file["storage_location"],
                    file_size=file["file_size"],
                    accessibility=file["accessibility"],
                )
            )

        if commit:
            AudioProperties.objects.bulk_create(audio_properties, ignore_conflicts=True)
            self.instance.files.bulk_create(files, ignore_conflicts=True)
