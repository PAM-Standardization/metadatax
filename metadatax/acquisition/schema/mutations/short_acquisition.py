import datetime

import graphene
from django.db import transaction
from graphene_django.types import ErrorType

from metadatax.acquisition.models import Site
from metadatax.common.schema.mutations import ContactMutation
from metadatax.data.schema.mutations.visual_observation import VisualObservationForm
from .channel_configuration import ChannelConfigurationInput, ChannelConfigurationForm
from .deployment import DeploymentForm
from .detector_specification import ChannelConfigurationDetectorSpecificationForm
from .recorder_specification import ChannelConfigurationRecorderSpecificationForm


class ImportShortAcquisition(graphene.Mutation):
    class Arguments:
        channel_configuration = graphene.List(ChannelConfigurationInput, required=True)

    ok = graphene.Boolean()
    errors = graphene.List(ErrorType)

    @classmethod
    @transaction.atomic
    def mutate(cls, root, info, channel_configuration):
        input_data = channel_configuration
        sid = transaction.savepoint()
        errors = []

        for index in range(0, len(input_data)):
            can_save_full_data = True
            data = input_data[index]
            deployment_data = data.pop("deployment")

            site_data = data.pop("site", None)
            if site_data:
                data["site"] = Site.objects.get_or_create(
                    project_id=deployment_data["project_id"],
                    name=site_data,
                )[0].id

            campaign_data = data.pop("campaign", None)
            if campaign_data:
                data["campaign"] = Site.objects.get_or_create(
                    project_id=deployment_data["project_id"],
                    name=campaign_data,
                )[0].id

            contacts_data = deployment_data.pop("contacts", None)
            if contacts_data:
                contacts = []
                for k in range(0, len(contacts_data)):
                    d = contacts_data[k]
                    d_mutation = ContactMutation()
                    d_payload = d_mutation.mutate(None, info=info, input=d)
                    if d_payload.contact:
                        contacts.append(d_payload.contact)
                    if d_payload.errors:
                        for e in d_payload.errors:
                            errors.append(
                                ErrorType(
                                    field=f"{index}-deployment-contacts-{k}-{e.field}",
                                    messages=e.messages,
                                )
                            )

            visual_observations_data = deployment_data.pop("visual_observations", None)

            deployment_data["contacts"] = [c.id for c in contacts]
            deployment_form = DeploymentForm(data=deployment_data)
            if deployment_form.is_valid():
                data["deployment"] = deployment_form.save().id
            else:
                can_save_full_data = False
                for field, messages in deployment_form.errors.items():
                    errors.append(
                        ErrorType(
                            field=f"{index}-deployment-{field}", messages=messages
                        )
                    )

            if visual_observations_data:
                for k in range(0, len(visual_observations_data)):
                    d = visual_observations_data[k]
                    d["deployment"] = data["deployment"]
                    visual_observations_form = VisualObservationForm(data=d)
                    if visual_observations_form.is_valid():
                        visual_observations_form.save()
                    else:
                        can_save_full_data = False
                        for field, messages in visual_observations_form.errors.items():
                            errors.append(
                                ErrorType(
                                    field=f"{index}-deployment-visual_observations-{field}",
                                    messages=messages,
                                )
                            )

            recorder_specification_data = data.pop("recorder_specification", None)
            if recorder_specification_data:
                recorder_specification_form = (
                    ChannelConfigurationRecorderSpecificationForm(
                        data=recorder_specification_data
                    )
                )
                if recorder_specification_form.is_valid():
                    data[
                        "recorder_specification"
                    ] = recorder_specification_form.save().id
                else:
                    can_save_full_data = False
                    for field, messages in recorder_specification_form.errors.items():
                        errors.append(
                            ErrorType(
                                field=f"{index}-recorder_specification-{field}",
                                messages=messages,
                            )
                        )

            detector_specification_data = data.pop("detector_specification", None)
            if detector_specification_data:
                detector_specification_form = (
                    ChannelConfigurationDetectorSpecificationForm(
                        data=detector_specification_data
                    )
                )
                if detector_specification_form.is_valid():
                    data[
                        "detector_specification"
                    ] = detector_specification_form.save().id
                else:
                    can_save_full_data = False
                    for field, messages in detector_specification_form.errors.items():
                        errors.append(
                            ErrorType(
                                field=f"{index}-detector_specification-{field}",
                                messages=messages,
                            )
                        )

            if can_save_full_data:
                form_data = ChannelConfigurationForm(data=data)
                if form_data.is_valid():
                    form_data.save()
                else:
                    for field, messages in form_data.errors.items():
                        errors.append(
                            ErrorType(field=f"{index}-{field}", messages=messages)
                        )

        if len(errors) > 0:
            transaction.savepoint_rollback(sid)
            return cls(errors=errors)

        return cls(ok=True)
