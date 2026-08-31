from graphene import ObjectType

from .deployment import DeploymentMutation
from .channel_configuration import ChannelConfigurationMutation
from .recorder_specification import ChannelConfigurationRecorderSpecificationMutation
from .short_acquisition import ImportShortAcquisition


class AcquisitionMutation(ObjectType):
    # Project

    # Site

    # Campaign

    # Deployment
    deployment = DeploymentMutation.Field()

    # Channel Configuration
    channel_configuration = ChannelConfigurationMutation.Field()
    channel_configuration_recorder_specification = ChannelConfigurationRecorderSpecificationMutation.Field()

    import_short_acquisition = ImportShortAcquisition.Field()
