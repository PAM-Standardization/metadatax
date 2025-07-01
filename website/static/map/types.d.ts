type Accessibility = 'Confidential' | 'Upon request' | 'Open access';
type Financing = 'Public' | 'Private' | 'Mixte' | 'Not Financed';
type Project = {
    id: number;
    name: string;
    contacts: ContactRole[];
    accessibility: Accessibility | null;
    doi: string | null;
    project_type: ProjectType | null;
    start_date: string | null;
    end_date: string | null;
    project_goal: string | null;
    financing: Financing | null;
}
type ProjectType = {
    id: number;
    name: string;
}

type Contact = {
    id: number;
    name: string;
    mail: string | null;
    website: string | null;
}
type Role =
    'Main Contact' |
    'Funder' |
    'Project Owner' |
    'Project Manager' |
    'Dataset Supplier' |
    'Dataset Producer' |
    'Production Database' |
    'Contact Point';
type ContactRole = {
    id: number;
    contact: Contact;
    role: Role;
}

type Deployment = {
    id: number;
    project: number;
    longitude: number;
    latitude: number;
    name: string;
    contacts: ContactRole[];
    channel_configurations: ChannelConfiguration[];
    mobile_positions: DeploymentMobilePosition[];
    site: Site | null;
    campaign: Campaign | null;
    platform: Platform | null;
    bathymetric_depth: number | null;
    deployment_date: string | null;
    deployment_vessel: string | null;
    recovery_date: string | null;
    recovery_vessel: string | null;
    description: string | null;
};
type DeploymentMobilePosition = {
    id: number;
    deployment_id: number;
    datetime: string;
    longitude: number;
    latitude: number;
    depth: number;
    heading: number | null;
    pitch: number | null;
    roll: number | null;
}
type Site = {
    id: number;
    name: string;
}
type Campaign = {
    id: number;
    name: string;
}

type ChannelConfiguration = {
    id: number;
    deployment_id: number;
    other_equipments: Array<Equipment>;
    recorder_specification: ChannelConfigurationRecorderSpecification | null;
    detector_specification: ChannelConfigurationDetectorSpecificationSerializer | null;
    continuous: boolean | null;
    duty_cycle_on: number | null;
    duty_cycle_off: number | null;
    instrument_depth: number | null;
    timezone: string | null;
    extra_information: string | null;
    harvest_starting_date: string | null;
    harvest_ending_date: string | null;
}
type ChannelConfigurationRecorderSpecification = {
    id: number;
    recorder: Equipment & { recorder_specification: RecorderSpecification };
    hydrophone: Equipment & { hydrophone_specification: HydrophoneSpecification };
    recording_formats: string[];
    sampling_frequency: number;
    sample_depth: number;
    gain: number;

    channel_name: string | null;
}
type ChannelConfigurationDetectorSpecificationSerializer = {
    id: number;
    detector: Equipment & { acoustic_detector_specification: AcousticDetectorSpecification };
    output_formats: string[];
    labels: Label[];

    min_frequency: number | null;
    max_frequency: number | null;
    filter: string | null;
    configuration: string | null;
}

type Equipment = {
    id: number;
    model: string;
    serial_number: string;
    owner: Contact;
    provider: Contact;

    sd_card_specification: SDCardSpecification | null;
    recorder_specification: RecorderSpecification | null;
    hydrophone_specification: HydrophoneSpecification | null;
    acoustic_detector_specification: AcousticDetectorSpecification | null;
    purchase_date: string | null;
    name: string | null;
    battery_slots_count: number | null;
    battery_type: string | null;
    cables: string | null;
}
type SDCardSpecification = {
    id: number;
    capacity: number;
}
type RecorderSpecification = {
    id: number;
    channels_count: number | null;
    sd_slots_count: number | null;
    sd_maximum_capacity: number | null;
    sd_type: string | null;
}
type HydrophoneDirectivity =
    'Omni-directional' |
    'Bi-directional' |
    'Uni-directional' |
    'Cardioid' |
    'Supercardioid';
type HydrophoneSpecification = {
    id: number;
    sensitivity: number;
    directivity: HydrophoneDirectivity | null;
    operating_min_temperature: number | null;
    operating_max_temperature: number | null;
    min_bandwidth: number | null;
    max_bandwidth: number | null;
    min_dynamic_range: number | null;
    max_dynamic_range: number | null;
    min_operating_depth: number | null;
    max_operating_depth: number | null;
    noise_floor: number | null;
}
type AcousticDetectorSpecification = {
    id: number;
    detected_labels: Label[];
    min_frequency: number | null;
    max_frequency: number | null;
    algorithm_name: string | null;
}
type Platform = {
    id: number;
    owner: Contact;
    provider: Contact;
    type: PlatformType;
    name: string | null;
    description: string | null;
}
type PlatformType = {
    id: number;
    name: string;
    is_mobile: boolean;
}

type Label = {
    id: number;
    source: Source;
    sound: Sound | null;
    physical_descriptor: PhysicalDescriptor | null;
    nickname: string | null;
}
type Source = {
    id: number;
    english_name: string;
    latin_name: string | null;
    french_name: string | null;
    code_name: string | null;
    taxon: string | null;
    parent_id: number;
}
type Sound = {
    id: number;
    english_name: string;
    french_name: string | null;
    code_name: string | null;
    taxon: string | null;
    parent_id: number;
    associated_names: number[];
}
type SignalShape = 'Stationary' | 'Pulse' | 'Frequency modulation';
type SignalPlurality = 'One' | 'Set' | 'Repetitive set';
type PhysicalDescriptor = {
    id: number;
    shape: SignalShape;
    plurality: SignalPlurality;
    min_frequency: number | null;
    max_frequency: number | null;
    mean_duration: number | null;
    description: string | null;
}
