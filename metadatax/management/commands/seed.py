from datetime import datetime

from django.core import management
from django.core.management.base import BaseCommand
from django.utils import timezone

from meta_auth.models import User
from metadatax_acquisition.models import (
    ProjectType,
    Project,
    ChannelConfigurationRecorderSpecification,
)
from metadatax_common.models import Accessibility, Contact, ContactRole
from metadatax_data.models import FileFormat
from metadatax_equipment.models import (
    PlatformType,
    Platform,
    RecorderSpecification,
    Equipment,
    HydrophoneSpecification,
)


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        # Flush database
        self.stdout.write("[DATABASE] flush...", ending="   ")
        management.call_command("flush", interactive=False)
        self.stdout.write(" ✓")

        # Create users
        self.stdout.write("[CREATE] Users...", ending="      ")
        self.create_admin()

        # Create projects
        self.stdout.write("[CREATE] Projects...", ending="  ")
        self.create_CETIROISE_project()

    def create_admin(self):
        User.objects.create_user(
            "admin", "admin@test.fr", "admin", is_superuser=True, is_staff=True
        )
        self.stdout.write("admin ✓\n")

    def create_CETIROISE_project(self):
        project_type, _ = ProjectType.objects.get_or_create(name="research")
        project = Project.objects.create(
            name="CETIROISE",
            project_type=project_type,
            accessibility=Accessibility.REQUEST,
        )

        project.contacts.create(
            contact=Contact.objects.create(name="OFB", mail="contact@ofb.test"),
            role=ContactRole.Type.MAIN_CONTACT,
        )
        ensta = Contact.objects.create(
            name="ENSTA Bretagne", mail="contact@ensta-bretagne.test"
        )
        project.contacts.create(contact=ensta, role=ContactRole.Type.PROJECT_MANAGER)

        phase1 = project.campaigns.create(name="Phase 1")
        site_a = project.sites.create(name="A")
        site_b = project.sites.create(name="B")

        platform_type, _ = PlatformType.objects.get_or_create(
            name="mooring line with acoustic release"
        )
        mooring_line = Platform.objects.create(
            name="Mooring line CETIROISE",
            type=platform_type,
            owner=ensta,
            provider=ensta,
        )

        vessel = "Céladon"
        deployment = project.deployments.create(
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

        project.deployments.create(
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
        contact_role = ContactRole.objects.create(
            contact=ensta,
            role=ContactRole.Type.CONTACT_POINT,
        )
        for d in project.deployments.all():
            d.contacts.add(contact_role)

        file_format, _ = FileFormat.objects.get_or_create(name=".wav")
        channel = deployment.channel_configurations.create(
            recorder_specification=ChannelConfigurationRecorderSpecification.objects.create(
                recorder=Equipment.objects.create(
                    model="LP-440",
                    serial_number="001",
                    owner=ensta,
                    provider=Contact.objects.create(name="RTSYS"),
                    recorder_specification=RecorderSpecification.objects.create(
                        channels_count=1
                    ),
                ),
                hydrophone=Equipment.objects.create(
                    model="HTI-99HF",
                    serial_number="785465",
                    owner=ensta,
                    provider=Contact.objects.create(name="HTI"),
                    hydrophone_specification=HydrophoneSpecification.objects.create(
                        sensitivity=-169.9
                    ),
                ),
                sampling_frequency=128_000,
                channel_name="A",
                sample_depth=16,
                gain=0,
            ),
            continuous=True,
            instrument_depth=100,
        )
        channel.recorder_specification.recording_formats.add(file_format)
        self.stdout.write(" CETIROISE ✓\n")
