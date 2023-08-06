from .ami import Ami
from .ami_copy import AmiCopy
from .ami_from_instance import AmiFromInstance
from .ami_launch_permission import AmiLaunchPermission
from .availability_zone_group import AvailabilityZoneGroup
from .capacity_reservation import CapacityReservation
from .ds_ami import DsAmi
from .ds_ami_ids import DsAmiIds
from .ds_availability_zone import DsAvailabilityZone
from .ds_availability_zones import DsAvailabilityZones
from .ds_eip import DsEip
from .ds_eips import DsEips
from .ds_host import DsHost
from .ds_instance import DsInstance
from .ds_instance_type import DsInstanceType
from .ds_instance_type_offering import DsInstanceTypeOffering
from .ds_instance_type_offerings import DsInstanceTypeOfferings
from .ds_instance_types import DsInstanceTypes
from .ds_instances import DsInstances
from .ds_key_pair import DsKeyPair
from .ds_launch_template import DsLaunchTemplate
from .ds_serial_console_access import DsSerialConsoleAccess
from .ds_spot_price import DsSpotPrice
from .eip import Eip
from .eip_association import EipAssociation
from .fleet import Fleet
from .host import Host
from .instance import Instance
from .key_pair import KeyPair
from .launch_template import LaunchTemplate
from .placement_group import PlacementGroup
from .serial_console_access import SerialConsoleAccess
from .spot_datafeed_subscription import SpotDatafeedSubscription
from .spot_fleet_request import SpotFleetRequest
from .spot_instance_request import SpotInstanceRequest
from .tag import Tag

__all__ = [
    "LaunchTemplate",
    "Eip",
    "AmiFromInstance",
    "PlacementGroup",
    "CapacityReservation",
    "SerialConsoleAccess",
    "AvailabilityZoneGroup",
    "Instance",
    "SpotDatafeedSubscription",
    "AmiCopy",
    "SpotInstanceRequest",
    "Tag",
    "KeyPair",
    "Ami",
    "Fleet",
    "Host",
    "EipAssociation",
    "SpotFleetRequest",
    "AmiLaunchPermission",
    "DsHost",
    "DsSerialConsoleAccess",
    "DsInstances",
    "DsLaunchTemplate",
    "DsInstance",
    "DsAvailabilityZones",
    "DsInstanceTypeOffering",
    "DsInstanceType",
    "DsInstanceTypeOfferings",
    "DsInstanceTypes",
    "DsAmi",
    "DsKeyPair",
    "DsEips",
    "DsEip",
    "DsAvailabilityZone",
    "DsAmiIds",
    "DsSpotPrice",
]
