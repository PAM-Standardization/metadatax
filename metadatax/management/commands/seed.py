from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.core import management
from django.core.management.base import BaseCommand
from django.utils import timezone

from metadatax.acquisition.models import (
    ProjectType,
    Project, Deployment, ChannelConfiguration,
)
from metadatax.acquisition.models.channel_configuration_specifications import ChannelConfigurationRecorderSpecification
from metadatax.common.models import Person, Institution, Accessibility, Role, ContactRelation
from metadatax.data.models import FileFormat
from metadatax.equipment.models import (
    PlatformType,
    Platform,
    RecorderSpecification,
    Equipment,
    HydrophoneSpecification, EquipmentModel, EquipmentModelSpecification,
)


class Contacts:

    def __init__(self, command: BaseCommand):
        super().__init__()
        self.command = command

        self.command.stdout.write("[CREATE] Contacts...", ending="\n")
        self.OFB = self._create(Institution, {
            "name": "OFB",
            "mail": "contact@ofb.test"
        })
        self.JohnDoe = self._create(Person, {
            "first_name": "John",
            "last_name": "Doe",
            "mail": "j.doe@ensta.test"
        })
        self.ENSTA = self._create(Institution, {
            "name": "ENSTA",
            "mail": "contact@ensta.test"
        })
        self.RTSYS = self._create(Institution, {"name": "RTSYS"})
        self.HTI = self._create(Institution, {"name": "HTI"})

    def _create(self, model, params):
        self.command.stdout.write(
            f"   > {model.__name__}: {params.get('name', f"{params.get('first_name')} {params.get('last_name')}")}",
            ending=" ")
        obj = model.objects.create(**params)
        self.command.stdout.write("✓", ending="\n")
        return obj


class Equipments:

    def __init__(self, command: BaseCommand, contacts: Contacts):
        super().__init__()
        self.command = command
        self.contacts = contacts

        self.command.stdout.write("[CREATE] Equipments...", ending="\n")
        self._create_recorder()
        self._create_hydrophone()

    def _create_recorder(self):
        self.command.stdout.write(f"   > Recorder: LP-440", ending=" ")
        model = EquipmentModel.objects.create(name="LP-440", provider=self.contacts.RTSYS)
        EquipmentModelSpecification.objects.create(
            model=model,
            specification_type=ContentType.objects.get_for_model(RecorderSpecification),
            specification_id=RecorderSpecification.objects.create(channels_count=1).id,
        )
        self.recorder = Equipment.objects.create(
            model=model,
            serial_number="001",
            owner_type=ContentType.objects.get_for_model(Institution),
            owner_id=self.contacts.ENSTA.id,
        )
        self.command.stdout.write("✓", ending="\n")

    def _create_hydrophone(self):
        self.command.stdout.write(f"   > Hydrophone: HTI-99HF", ending=" ")
        model = EquipmentModel.objects.create(name="HTI-99HF", provider=self.contacts.HTI)
        EquipmentModelSpecification.objects.create(
            model=model,
            specification_type=ContentType.objects.get_for_model(HydrophoneSpecification),
            specification_id=HydrophoneSpecification.objects.create().id,
        )
        self.hydrophone = Equipment.objects.create(
            model=model,
            serial_number="785465",
            owner_type=ContentType.objects.get_for_model(Institution),
            owner_id=self.contacts.ENSTA.id,
            sensitivity=-169.9
        )
        self.command.stdout.write("✓", ending="\n")


class Command(BaseCommand):
    help = "seed database for testing and development."

    contacts: Contacts
    equipments: Equipments

    def handle(self, *args, **options):
        # Flush database
        self.stdout.write("[DATABASE] flush...", ending="   ")
        management.call_command("flush", interactive=False)
        self.stdout.write(" ✓")

        # Create utils
        self.contacts = Contacts(self)
        self.equipments = Equipments(self, self.contacts)

        # Create projects
        self.stdout.write("[CREATE] Projects...", ending="  ")

        self.create_CETIROISE_project()

    def create_CETIROISE_project(self):
        # Project
        project = Project.objects.create(
            name="CETIROISE",
            project_type=ProjectType.objects.get_or_create(name="research")[0],
            accessibility=Accessibility.REQUEST,
        )
        # Project contacts
        project.contacts.add(
            ContactRelation.objects.create(
                role=Role.MAIN_CONTACT,
                contact_type=ContentType.objects.get_for_model(Institution),
                contact_id=self.contacts.OFB.id,
            )
        )
        project.contacts.add(
            ContactRelation.objects.create(
                role=Role.PROJECT_MANAGER,
                contact_type=ContentType.objects.get_for_model(Person),
                contact_id=self.contacts.JohnDoe.id,
            )
        )

        # Phase & Sites
        phase1 = project.campaigns.create(name="Phase 1")
        site_a = project.sites.create(name="A")
        site_b = project.sites.create(name="B")

        # Platform
        platform_type, _ = PlatformType.objects.get_or_create(
            name="mooring line with acoustic release"
        )
        mooring_line = Platform.objects.create(
            name="Mooring line CETIROISE",
            type=platform_type,
            owner=self.contacts.ENSTA,
            provider=self.contacts.ENSTA,
        )

        # Deployments
        vessel = "Céladon"
        deployment_A1 = Deployment.objects.create(
            project=project,
            campaign=phase1,
            site=site_a,
            platform=mooring_line,
            latitude=48.52,
            longitude=-5.23,
            deployment_date=timezone.make_aware(datetime(2022, 5, 10, 9, 12)),
            deployment_vessel=vessel,
            recovery_date=timezone.make_aware(datetime(2022, 8, 22, 9, 54)),
            recovery_vessel=vessel,
        )
        Deployment.objects.create(
            project=project,
            campaign=phase1,
            site=site_b,
            platform=mooring_line,
            latitude=48.5183,
            longitude=-5.1177,
            bathymetric_depth=102,
            deployment_date=timezone.make_aware(datetime(2022, 5, 10, 9, 56)),
            deployment_vessel=vessel,
            recovery_date=timezone.make_aware(datetime(2022, 8, 23, 11, 19)),
            recovery_vessel=vessel,
        )
        contact_role = ContactRelation.objects.create(
            contact_id=self.contacts.JohnDoe.id,
            contact_type=ContentType.objects.get_for_model(Person),
            role=Role.CONTACT_POINT,
        )
        for d in project.deployments.all():
            d.contacts.add(contact_role)

        file_format, _ = FileFormat.objects.get_or_create(name=".wav")
        channel_A = ChannelConfiguration.objects.create(
            deployment=deployment_A1,
            recorder_specification=ChannelConfigurationRecorderSpecification.objects.create(
                recorder=self.equipments.recorder,
                hydrophone=self.equipments.hydrophone,
                sampling_frequency=128_000,
                channel_name="A",
                sample_depth=16,
                gain=0,
            ),
            continuous=True,
            instrument_depth=100,
        )
        channel_A.recorder_specification.recording_formats.add(file_format)
        self.stdout.write(" CETIROISE ✓\n")
