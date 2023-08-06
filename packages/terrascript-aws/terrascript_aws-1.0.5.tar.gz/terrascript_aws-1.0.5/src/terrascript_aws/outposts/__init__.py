from .ds_asset import DsAsset
from .ds_assets import DsAssets
from .ds_ec2_coip_pool import DsEc2CoipPool
from .ds_ec2_coip_pools import DsEc2CoipPools
from .ds_ec2_local_gateway import DsEc2LocalGateway
from .ds_ec2_local_gateway_route_table import DsEc2LocalGatewayRouteTable
from .ds_ec2_local_gateway_route_tables import DsEc2LocalGatewayRouteTables
from .ds_ec2_local_gateway_virtual_interface import DsEc2LocalGatewayVirtualInterface
from .ds_ec2_local_gateway_virtual_interface_group import (
    DsEc2LocalGatewayVirtualInterfaceGroup,
)
from .ds_ec2_local_gateway_virtual_interface_groups import (
    DsEc2LocalGatewayVirtualInterfaceGroups,
)
from .ds_ec2_local_gateways import DsEc2LocalGateways
from .ds_outpost import DsOutpost
from .ds_outpost_instance_type import DsOutpostInstanceType
from .ds_outpost_instance_types import DsOutpostInstanceTypes
from .ds_outposts import DsOutposts
from .ds_site import DsSite
from .ds_sites import DsSites
from .ec2_local_gateway_route import Ec2LocalGatewayRoute
from .ec2_local_gateway_route_table_vpc_association import (
    Ec2LocalGatewayRouteTableVpcAssociation,
)

__all__ = [
    "Ec2LocalGatewayRoute",
    "Ec2LocalGatewayRouteTableVpcAssociation",
    "DsEc2LocalGatewayVirtualInterface",
    "DsAsset",
    "DsEc2LocalGateway",
    "DsEc2LocalGatewayRouteTable",
    "DsEc2CoipPool",
    "DsOutpostInstanceTypes",
    "DsOutpostInstanceType",
    "DsEc2LocalGatewayRouteTables",
    "DsAssets",
    "DsOutpost",
    "DsOutposts",
    "DsEc2LocalGatewayVirtualInterfaceGroup",
    "DsEc2CoipPools",
    "DsSites",
    "DsEc2LocalGatewayVirtualInterfaceGroups",
    "DsSite",
    "DsEc2LocalGateways",
]
