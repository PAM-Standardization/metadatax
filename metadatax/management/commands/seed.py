from datetime import datetime

from django.core import management
from django.core.management.base import BaseCommand
from django.utils import timezone

from meta_auth.models import User
from metadatax.models import Project, Recorder
from metadatax.models.acquisition import ProjectType, Accessibility, Platform, PlatformType
from metadatax.models.data import FileFormat
from metadatax.models.equipment import RecorderModel, EquipmentProvider, Hydrophone, HydrophoneModel


class Command(BaseCommand):
    help = "seed database for testing and development."

    def handle(self, *args, **options):
        # Flush database
        self.stdout.write('[DATABASE] flush...')
        management.call_command("flush", interactive=False)
        self.stdout.write('[DATABASE] flush ✓')

        # Create users
        self.stdout.write('[CREATE] Users...')
        self.create_admin()

        # Create projects
        self.stdout.write('[CREATE] Projects...')
        self.create_CETIROISE_project()

    def create_admin(self):
        User.objects.create_user(
            "admin", "admin@test.fr",
            "admin",
            is_superuser=True, is_staff=True
        )
        self.stdout.write('[CREATE] User admin ✓')



    def create_CETIROISE_project(self):
        project_type, _ = ProjectType.objects.get_or_create(name="research")
        project = Project.objects.create(
            name="CETIROISE",
            project_type=project_type,
            accessibility=Accessibility.REQUEST
        )

        project.responsible_parties.create(name="OFB", contact="contact@ofb.test")
        ensta_bretagne = project.responsible_parties.create(name="ENSTA Bretagne",
                                                                      contact="contact@ensta-bretagne.test")

        phase1 = project.campaigns.create(name="Phase 1")
        site_a = project.sites.create(name="A")
        site_b = project.sites.create(name="B")

        platform_type, _ = PlatformType.objects.get_or_create(name="mooring line with acoustic release")
        mooring_line = Platform.objects.create(
            name="Mooring line CETIROISE",
            type=platform_type
        )

        vessel = "Céladon"
        deployment = project.deployments.create(
            provider=ensta_bretagne,
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
            provider=ensta_bretagne,
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

        file_format, _ = FileFormat.objects.get_or_create(name="WAV")
        deployment.channelconfiguration_set.create(
            recorder=Recorder.objects.create(
                serial_number="001",
                model=RecorderModel.objects.create(
                    name="LP-440",
                    number_of_channels=1,
                    provider=EquipmentProvider.objects.create(name="RTSYS")
                ),
            ),
            channel_name="A",
            recording_format=file_format,
            sample_depth=16,
            sampling_frequency=128_000,
            gain=0,
            hydrophone=Hydrophone.objects.create(
                serial_number="785465",
                sensitivity=-169.9,
                model=HydrophoneModel.objects.create(
                    name="HTI-99HF",
                    provider=EquipmentProvider.objects.create(name="HTI")
                )
            ),
            hydrophone_depth=100,
            continuous=True
        )
        self.stdout.write('[CREATE] Project CETIROISE ✓')
