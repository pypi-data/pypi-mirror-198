import terrascript.core as core


@core.schema
class SourceVpc(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=SourceVpc.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Vpc(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Vpc.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Component(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Component.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class TransitGatewayRouteTableRoute(core.Schema):

    attachment_id: str | core.StringOut = core.attr(str, computed=True)

    destination_cidr: str | core.StringOut = core.attr(str, computed=True)

    prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    resource_id: str | core.StringOut = core.attr(str, computed=True)

    resource_type: str | core.StringOut = core.attr(str, computed=True)

    route_origin: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attachment_id: str | core.StringOut,
        destination_cidr: str | core.StringOut,
        prefix_list_id: str | core.StringOut,
        resource_id: str | core.StringOut,
        resource_type: str | core.StringOut,
        route_origin: str | core.StringOut,
        state: str | core.StringOut,
    ):
        super().__init__(
            args=TransitGatewayRouteTableRoute.Args(
                attachment_id=attachment_id,
                destination_cidr=destination_cidr,
                prefix_list_id=prefix_list_id,
                resource_id=resource_id,
                resource_type=resource_type,
                route_origin=route_origin,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_id: str | core.StringOut = core.arg()

        destination_cidr: str | core.StringOut = core.arg()

        prefix_list_id: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        resource_type: str | core.StringOut = core.arg()

        route_origin: str | core.StringOut = core.arg()

        state: str | core.StringOut = core.arg()


@core.schema
class SourcePortRanges(core.Schema):

    from_: int | core.IntOut = core.attr(int, computed=True, alias="from")

    to: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: int | core.IntOut,
        to: int | core.IntOut,
    ):
        super().__init__(
            args=SourcePortRanges.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: int | core.IntOut = core.arg()

        to: int | core.IntOut = core.arg()


@core.schema
class DestinationPortRanges(core.Schema):

    from_: int | core.IntOut = core.attr(int, computed=True, alias="from")

    to: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: int | core.IntOut,
        to: int | core.IntOut,
    ):
        super().__init__(
            args=DestinationPortRanges.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: int | core.IntOut = core.arg()

        to: int | core.IntOut = core.arg()


@core.schema
class OutboundHeader(core.Schema):

    destination_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    destination_port_ranges: list[DestinationPortRanges] | core.ArrayOut[
        DestinationPortRanges
    ] = core.attr(DestinationPortRanges, computed=True, kind=core.Kind.array)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    source_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_port_ranges: list[SourcePortRanges] | core.ArrayOut[SourcePortRanges] = core.attr(
        SourcePortRanges, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination_addresses: list[str] | core.ArrayOut[core.StringOut],
        destination_port_ranges: list[DestinationPortRanges] | core.ArrayOut[DestinationPortRanges],
        protocol: str | core.StringOut,
        source_addresses: list[str] | core.ArrayOut[core.StringOut],
        source_port_ranges: list[SourcePortRanges] | core.ArrayOut[SourcePortRanges],
    ):
        super().__init__(
            args=OutboundHeader.Args(
                destination_addresses=destination_addresses,
                destination_port_ranges=destination_port_ranges,
                protocol=protocol,
                source_addresses=source_addresses,
                source_port_ranges=source_port_ranges,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        destination_port_ranges: list[DestinationPortRanges] | core.ArrayOut[
            DestinationPortRanges
        ] = core.arg()

        protocol: str | core.StringOut = core.arg()

        source_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        source_port_ranges: list[SourcePortRanges] | core.ArrayOut[SourcePortRanges] = core.arg()


@core.schema
class PortRange(core.Schema):

    from_: int | core.IntOut = core.attr(int, computed=True, alias="from")

    to: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: int | core.IntOut,
        to: int | core.IntOut,
    ):
        super().__init__(
            args=PortRange.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: int | core.IntOut = core.arg()

        to: int | core.IntOut = core.arg()


@core.schema
class SecurityGroupRule(core.Schema):

    cidr: str | core.StringOut = core.attr(str, computed=True)

    direction: str | core.StringOut = core.attr(str, computed=True)

    port_range: list[PortRange] | core.ArrayOut[PortRange] = core.attr(
        PortRange, computed=True, kind=core.Kind.array
    )

    prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    security_group_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
        direction: str | core.StringOut,
        port_range: list[PortRange] | core.ArrayOut[PortRange],
        prefix_list_id: str | core.StringOut,
        protocol: str | core.StringOut,
        security_group_id: str | core.StringOut,
    ):
        super().__init__(
            args=SecurityGroupRule.Args(
                cidr=cidr,
                direction=direction,
                port_range=port_range,
                prefix_list_id=prefix_list_id,
                protocol=protocol,
                security_group_id=security_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()

        direction: str | core.StringOut = core.arg()

        port_range: list[PortRange] | core.ArrayOut[PortRange] = core.arg()

        prefix_list_id: str | core.StringOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        security_group_id: str | core.StringOut = core.arg()


@core.schema
class AdditionalDetails(core.Schema):

    additional_detail_type: str | core.StringOut = core.attr(str, computed=True)

    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        additional_detail_type: str | core.StringOut,
        component: list[Component] | core.ArrayOut[Component],
    ):
        super().__init__(
            args=AdditionalDetails.Args(
                additional_detail_type=additional_detail_type,
                component=component,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_detail_type: str | core.StringOut = core.arg()

        component: list[Component] | core.ArrayOut[Component] = core.arg()


@core.schema
class DestinationVpc(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=DestinationVpc.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class RouteTableRoute(core.Schema):

    destination_cidr: str | core.StringOut = core.attr(str, computed=True)

    destination_prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    egress_only_internet_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    gateway_id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str, computed=True)

    nat_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    origin: str | core.StringOut = core.attr(str, computed=True)

    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_peering_connection_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination_cidr: str | core.StringOut,
        destination_prefix_list_id: str | core.StringOut,
        egress_only_internet_gateway_id: str | core.StringOut,
        gateway_id: str | core.StringOut,
        instance_id: str | core.StringOut,
        nat_gateway_id: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        origin: str | core.StringOut,
        transit_gateway_id: str | core.StringOut,
        vpc_peering_connection_id: str | core.StringOut,
    ):
        super().__init__(
            args=RouteTableRoute.Args(
                destination_cidr=destination_cidr,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_internet_gateway_id=egress_only_internet_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                origin=origin,
                transit_gateway_id=transit_gateway_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_cidr: str | core.StringOut = core.arg()

        destination_prefix_list_id: str | core.StringOut = core.arg()

        egress_only_internet_gateway_id: str | core.StringOut = core.arg()

        gateway_id: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        nat_gateway_id: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()

        origin: str | core.StringOut = core.arg()

        transit_gateway_id: str | core.StringOut = core.arg()

        vpc_peering_connection_id: str | core.StringOut = core.arg()


@core.schema
class AttachedTo(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=AttachedTo.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class TransitGateway(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=TransitGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class AclRule(core.Schema):

    cidr: str | core.StringOut = core.attr(str, computed=True)

    egress: bool | core.BoolOut = core.attr(bool, computed=True)

    port_range: list[PortRange] | core.ArrayOut[PortRange] = core.attr(
        PortRange, computed=True, kind=core.Kind.array
    )

    protocol: str | core.StringOut = core.attr(str, computed=True)

    rule_action: str | core.StringOut = core.attr(str, computed=True)

    rule_number: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
        egress: bool | core.BoolOut,
        port_range: list[PortRange] | core.ArrayOut[PortRange],
        protocol: str | core.StringOut,
        rule_action: str | core.StringOut,
        rule_number: int | core.IntOut,
    ):
        super().__init__(
            args=AclRule.Args(
                cidr=cidr,
                egress=egress,
                port_range=port_range,
                protocol=protocol,
                rule_action=rule_action,
                rule_number=rule_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()

        egress: bool | core.BoolOut = core.arg()

        port_range: list[PortRange] | core.ArrayOut[PortRange] = core.arg()

        protocol: str | core.StringOut = core.arg()

        rule_action: str | core.StringOut = core.arg()

        rule_number: int | core.IntOut = core.arg()


@core.schema
class InboundHeader(core.Schema):

    destination_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    destination_port_ranges: list[DestinationPortRanges] | core.ArrayOut[
        DestinationPortRanges
    ] = core.attr(DestinationPortRanges, computed=True, kind=core.Kind.array)

    protocol: str | core.StringOut = core.attr(str, computed=True)

    source_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_port_ranges: list[SourcePortRanges] | core.ArrayOut[SourcePortRanges] = core.attr(
        SourcePortRanges, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination_addresses: list[str] | core.ArrayOut[core.StringOut],
        destination_port_ranges: list[DestinationPortRanges] | core.ArrayOut[DestinationPortRanges],
        protocol: str | core.StringOut,
        source_addresses: list[str] | core.ArrayOut[core.StringOut],
        source_port_ranges: list[SourcePortRanges] | core.ArrayOut[SourcePortRanges],
    ):
        super().__init__(
            args=InboundHeader.Args(
                destination_addresses=destination_addresses,
                destination_port_ranges=destination_port_ranges,
                protocol=protocol,
                source_addresses=source_addresses,
                source_port_ranges=source_port_ranges,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        destination_port_ranges: list[DestinationPortRanges] | core.ArrayOut[
            DestinationPortRanges
        ] = core.arg()

        protocol: str | core.StringOut = core.arg()

        source_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        source_port_ranges: list[SourcePortRanges] | core.ArrayOut[SourcePortRanges] = core.arg()


@core.schema
class Subnet(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Subnet.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class ReturnPathComponents(core.Schema):

    acl_rule: list[AclRule] | core.ArrayOut[AclRule] = core.attr(
        AclRule, computed=True, kind=core.Kind.array
    )

    additional_details: list[AdditionalDetails] | core.ArrayOut[AdditionalDetails] = core.attr(
        AdditionalDetails, computed=True, kind=core.Kind.array
    )

    attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo] = core.attr(
        AttachedTo, computed=True, kind=core.Kind.array
    )

    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc] = core.attr(
        DestinationVpc, computed=True, kind=core.Kind.array
    )

    inbound_header: list[InboundHeader] | core.ArrayOut[InboundHeader] = core.attr(
        InboundHeader, computed=True, kind=core.Kind.array
    )

    outbound_header: list[OutboundHeader] | core.ArrayOut[OutboundHeader] = core.attr(
        OutboundHeader, computed=True, kind=core.Kind.array
    )

    route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute] = core.attr(
        RouteTableRoute, computed=True, kind=core.Kind.array
    )

    security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule] = core.attr(
        SecurityGroupRule, computed=True, kind=core.Kind.array
    )

    sequence_number: int | core.IntOut = core.attr(int, computed=True)

    source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc] = core.attr(
        SourceVpc, computed=True, kind=core.Kind.array
    )

    subnet: list[Subnet] | core.ArrayOut[Subnet] = core.attr(
        Subnet, computed=True, kind=core.Kind.array
    )

    transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway] = core.attr(
        TransitGateway, computed=True, kind=core.Kind.array
    )

    transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute] | core.ArrayOut[
        TransitGatewayRouteTableRoute
    ] = core.attr(TransitGatewayRouteTableRoute, computed=True, kind=core.Kind.array)

    vpc: list[Vpc] | core.ArrayOut[Vpc] = core.attr(Vpc, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        acl_rule: list[AclRule] | core.ArrayOut[AclRule],
        additional_details: list[AdditionalDetails] | core.ArrayOut[AdditionalDetails],
        attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo],
        component: list[Component] | core.ArrayOut[Component],
        destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc],
        inbound_header: list[InboundHeader] | core.ArrayOut[InboundHeader],
        outbound_header: list[OutboundHeader] | core.ArrayOut[OutboundHeader],
        route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute],
        security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule],
        sequence_number: int | core.IntOut,
        source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc],
        subnet: list[Subnet] | core.ArrayOut[Subnet],
        transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway],
        transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute]
        | core.ArrayOut[TransitGatewayRouteTableRoute],
        vpc: list[Vpc] | core.ArrayOut[Vpc],
    ):
        super().__init__(
            args=ReturnPathComponents.Args(
                acl_rule=acl_rule,
                additional_details=additional_details,
                attached_to=attached_to,
                component=component,
                destination_vpc=destination_vpc,
                inbound_header=inbound_header,
                outbound_header=outbound_header,
                route_table_route=route_table_route,
                security_group_rule=security_group_rule,
                sequence_number=sequence_number,
                source_vpc=source_vpc,
                subnet=subnet,
                transit_gateway=transit_gateway,
                transit_gateway_route_table_route=transit_gateway_route_table_route,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl_rule: list[AclRule] | core.ArrayOut[AclRule] = core.arg()

        additional_details: list[AdditionalDetails] | core.ArrayOut[AdditionalDetails] = core.arg()

        attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo] = core.arg()

        component: list[Component] | core.ArrayOut[Component] = core.arg()

        destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc] = core.arg()

        inbound_header: list[InboundHeader] | core.ArrayOut[InboundHeader] = core.arg()

        outbound_header: list[OutboundHeader] | core.ArrayOut[OutboundHeader] = core.arg()

        route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute] = core.arg()

        security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule] = core.arg()

        sequence_number: int | core.IntOut = core.arg()

        source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc] = core.arg()

        subnet: list[Subnet] | core.ArrayOut[Subnet] = core.arg()

        transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway] = core.arg()

        transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute] | core.ArrayOut[
            TransitGatewayRouteTableRoute
        ] = core.arg()

        vpc: list[Vpc] | core.ArrayOut[Vpc] = core.arg()


@core.schema
class VpnGateway(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=VpnGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class TransitGatewayAttachment(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=TransitGatewayAttachment.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class VpnConnection(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=VpnConnection.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class ElasticLoadBalancerListener(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=ElasticLoadBalancerListener.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class TransitGatewayRouteTable(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=TransitGatewayRouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class VpcEndpoint(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=VpcEndpoint.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class IngressRouteTable(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=IngressRouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class SubnetRouteTable(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=SubnetRouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class ClassicLoadBalancerListener(core.Schema):

    instance_port: int | core.IntOut = core.attr(int, computed=True)

    load_balancer_port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        instance_port: int | core.IntOut,
        load_balancer_port: int | core.IntOut,
    ):
        super().__init__(
            args=ClassicLoadBalancerListener.Args(
                instance_port=instance_port,
                load_balancer_port=load_balancer_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_port: int | core.IntOut = core.arg()

        load_balancer_port: int | core.IntOut = core.arg()


@core.schema
class SecurityGroup(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=SecurityGroup.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class CustomerGateway(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=CustomerGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class RouteTable(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=RouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Destination(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Destination.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class LoadBalancerTargetGroup(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LoadBalancerTargetGroup.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class LoadBalancerTargetGroups(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=LoadBalancerTargetGroups.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class NatGateway(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=NatGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Acl(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Acl.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class NetworkInterface(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkInterface.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class PrefixList(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=PrefixList.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class VpcPeeringConnection(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=VpcPeeringConnection.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class PortRanges(core.Schema):

    from_: int | core.IntOut = core.attr(int, computed=True, alias="from")

    to: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: int | core.IntOut,
        to: int | core.IntOut,
    ):
        super().__init__(
            args=PortRanges.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: int | core.IntOut = core.arg()

        to: int | core.IntOut = core.arg()


@core.schema
class SecurityGroups(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=SecurityGroups.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class InternetGateway(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        id: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=InternetGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Explanations(core.Schema):

    acl: list[Acl] | core.ArrayOut[Acl] = core.attr(Acl, computed=True, kind=core.Kind.array)

    acl_rule: list[AclRule] | core.ArrayOut[AclRule] = core.attr(
        AclRule, computed=True, kind=core.Kind.array
    )

    address: str | core.StringOut = core.attr(str, computed=True)

    addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo] = core.attr(
        AttachedTo, computed=True, kind=core.Kind.array
    )

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cidrs: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    classic_load_balancer_listener: list[ClassicLoadBalancerListener] | core.ArrayOut[
        ClassicLoadBalancerListener
    ] = core.attr(ClassicLoadBalancerListener, computed=True, kind=core.Kind.array)

    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    customer_gateway: list[CustomerGateway] | core.ArrayOut[CustomerGateway] = core.attr(
        CustomerGateway, computed=True, kind=core.Kind.array
    )

    destination: list[Destination] | core.ArrayOut[Destination] = core.attr(
        Destination, computed=True, kind=core.Kind.array
    )

    destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc] = core.attr(
        DestinationVpc, computed=True, kind=core.Kind.array
    )

    direction: str | core.StringOut = core.attr(str, computed=True)

    elastic_load_balancer_listener: list[ElasticLoadBalancerListener] | core.ArrayOut[
        ElasticLoadBalancerListener
    ] = core.attr(ElasticLoadBalancerListener, computed=True, kind=core.Kind.array)

    explanation_code: str | core.StringOut = core.attr(str, computed=True)

    ingress_route_table: list[IngressRouteTable] | core.ArrayOut[IngressRouteTable] = core.attr(
        IngressRouteTable, computed=True, kind=core.Kind.array
    )

    internet_gateway: list[InternetGateway] | core.ArrayOut[InternetGateway] = core.attr(
        InternetGateway, computed=True, kind=core.Kind.array
    )

    load_balancer_arn: str | core.StringOut = core.attr(str, computed=True)

    load_balancer_listener_port: int | core.IntOut = core.attr(int, computed=True)

    load_balancer_target_group: list[LoadBalancerTargetGroup] | core.ArrayOut[
        LoadBalancerTargetGroup
    ] = core.attr(LoadBalancerTargetGroup, computed=True, kind=core.Kind.array)

    load_balancer_target_groups: list[LoadBalancerTargetGroups] | core.ArrayOut[
        LoadBalancerTargetGroups
    ] = core.attr(LoadBalancerTargetGroups, computed=True, kind=core.Kind.array)

    load_balancer_target_port: int | core.IntOut = core.attr(int, computed=True)

    missing_component: str | core.StringOut = core.attr(str, computed=True)

    nat_gateway: list[NatGateway] | core.ArrayOut[NatGateway] = core.attr(
        NatGateway, computed=True, kind=core.Kind.array
    )

    network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] = core.attr(
        NetworkInterface, computed=True, kind=core.Kind.array
    )

    packet_field: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    port_ranges: list[PortRanges] | core.ArrayOut[PortRanges] = core.attr(
        PortRanges, computed=True, kind=core.Kind.array
    )

    prefix_list: list[PrefixList] | core.ArrayOut[PrefixList] = core.attr(
        PrefixList, computed=True, kind=core.Kind.array
    )

    protocols: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    route_table: list[RouteTable] | core.ArrayOut[RouteTable] = core.attr(
        RouteTable, computed=True, kind=core.Kind.array
    )

    route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute] = core.attr(
        RouteTableRoute, computed=True, kind=core.Kind.array
    )

    security_group: list[SecurityGroup] | core.ArrayOut[SecurityGroup] = core.attr(
        SecurityGroup, computed=True, kind=core.Kind.array
    )

    security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule] = core.attr(
        SecurityGroupRule, computed=True, kind=core.Kind.array
    )

    security_groups: list[SecurityGroups] | core.ArrayOut[SecurityGroups] = core.attr(
        SecurityGroups, computed=True, kind=core.Kind.array
    )

    source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc] = core.attr(
        SourceVpc, computed=True, kind=core.Kind.array
    )

    state: str | core.StringOut = core.attr(str, computed=True)

    subnet: list[Subnet] | core.ArrayOut[Subnet] = core.attr(
        Subnet, computed=True, kind=core.Kind.array
    )

    subnet_route_table: list[SubnetRouteTable] | core.ArrayOut[SubnetRouteTable] = core.attr(
        SubnetRouteTable, computed=True, kind=core.Kind.array
    )

    transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway] = core.attr(
        TransitGateway, computed=True, kind=core.Kind.array
    )

    transit_gateway_attachment: list[TransitGatewayAttachment] | core.ArrayOut[
        TransitGatewayAttachment
    ] = core.attr(TransitGatewayAttachment, computed=True, kind=core.Kind.array)

    transit_gateway_route_table: list[TransitGatewayRouteTable] | core.ArrayOut[
        TransitGatewayRouteTable
    ] = core.attr(TransitGatewayRouteTable, computed=True, kind=core.Kind.array)

    transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute] | core.ArrayOut[
        TransitGatewayRouteTableRoute
    ] = core.attr(TransitGatewayRouteTableRoute, computed=True, kind=core.Kind.array)

    vpc: list[Vpc] | core.ArrayOut[Vpc] = core.attr(Vpc, computed=True, kind=core.Kind.array)

    vpc_endpoint: list[VpcEndpoint] | core.ArrayOut[VpcEndpoint] = core.attr(
        VpcEndpoint, computed=True, kind=core.Kind.array
    )

    vpc_peering_connection: list[VpcPeeringConnection] | core.ArrayOut[
        VpcPeeringConnection
    ] = core.attr(VpcPeeringConnection, computed=True, kind=core.Kind.array)

    vpn_connection: list[VpnConnection] | core.ArrayOut[VpnConnection] = core.attr(
        VpnConnection, computed=True, kind=core.Kind.array
    )

    vpn_gateway: list[VpnGateway] | core.ArrayOut[VpnGateway] = core.attr(
        VpnGateway, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        acl: list[Acl] | core.ArrayOut[Acl],
        acl_rule: list[AclRule] | core.ArrayOut[AclRule],
        address: str | core.StringOut,
        addresses: list[str] | core.ArrayOut[core.StringOut],
        attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo],
        availability_zones: list[str] | core.ArrayOut[core.StringOut],
        cidrs: list[str] | core.ArrayOut[core.StringOut],
        classic_load_balancer_listener: list[ClassicLoadBalancerListener]
        | core.ArrayOut[ClassicLoadBalancerListener],
        component: list[Component] | core.ArrayOut[Component],
        customer_gateway: list[CustomerGateway] | core.ArrayOut[CustomerGateway],
        destination: list[Destination] | core.ArrayOut[Destination],
        destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc],
        direction: str | core.StringOut,
        elastic_load_balancer_listener: list[ElasticLoadBalancerListener]
        | core.ArrayOut[ElasticLoadBalancerListener],
        explanation_code: str | core.StringOut,
        ingress_route_table: list[IngressRouteTable] | core.ArrayOut[IngressRouteTable],
        internet_gateway: list[InternetGateway] | core.ArrayOut[InternetGateway],
        load_balancer_arn: str | core.StringOut,
        load_balancer_listener_port: int | core.IntOut,
        load_balancer_target_group: list[LoadBalancerTargetGroup]
        | core.ArrayOut[LoadBalancerTargetGroup],
        load_balancer_target_groups: list[LoadBalancerTargetGroups]
        | core.ArrayOut[LoadBalancerTargetGroups],
        load_balancer_target_port: int | core.IntOut,
        missing_component: str | core.StringOut,
        nat_gateway: list[NatGateway] | core.ArrayOut[NatGateway],
        network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface],
        packet_field: str | core.StringOut,
        port: int | core.IntOut,
        port_ranges: list[PortRanges] | core.ArrayOut[PortRanges],
        prefix_list: list[PrefixList] | core.ArrayOut[PrefixList],
        protocols: list[str] | core.ArrayOut[core.StringOut],
        route_table: list[RouteTable] | core.ArrayOut[RouteTable],
        route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute],
        security_group: list[SecurityGroup] | core.ArrayOut[SecurityGroup],
        security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule],
        security_groups: list[SecurityGroups] | core.ArrayOut[SecurityGroups],
        source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc],
        state: str | core.StringOut,
        subnet: list[Subnet] | core.ArrayOut[Subnet],
        subnet_route_table: list[SubnetRouteTable] | core.ArrayOut[SubnetRouteTable],
        transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway],
        transit_gateway_attachment: list[TransitGatewayAttachment]
        | core.ArrayOut[TransitGatewayAttachment],
        transit_gateway_route_table: list[TransitGatewayRouteTable]
        | core.ArrayOut[TransitGatewayRouteTable],
        transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute]
        | core.ArrayOut[TransitGatewayRouteTableRoute],
        vpc: list[Vpc] | core.ArrayOut[Vpc],
        vpc_endpoint: list[VpcEndpoint] | core.ArrayOut[VpcEndpoint],
        vpc_peering_connection: list[VpcPeeringConnection] | core.ArrayOut[VpcPeeringConnection],
        vpn_connection: list[VpnConnection] | core.ArrayOut[VpnConnection],
        vpn_gateway: list[VpnGateway] | core.ArrayOut[VpnGateway],
    ):
        super().__init__(
            args=Explanations.Args(
                acl=acl,
                acl_rule=acl_rule,
                address=address,
                addresses=addresses,
                attached_to=attached_to,
                availability_zones=availability_zones,
                cidrs=cidrs,
                classic_load_balancer_listener=classic_load_balancer_listener,
                component=component,
                customer_gateway=customer_gateway,
                destination=destination,
                destination_vpc=destination_vpc,
                direction=direction,
                elastic_load_balancer_listener=elastic_load_balancer_listener,
                explanation_code=explanation_code,
                ingress_route_table=ingress_route_table,
                internet_gateway=internet_gateway,
                load_balancer_arn=load_balancer_arn,
                load_balancer_listener_port=load_balancer_listener_port,
                load_balancer_target_group=load_balancer_target_group,
                load_balancer_target_groups=load_balancer_target_groups,
                load_balancer_target_port=load_balancer_target_port,
                missing_component=missing_component,
                nat_gateway=nat_gateway,
                network_interface=network_interface,
                packet_field=packet_field,
                port=port,
                port_ranges=port_ranges,
                prefix_list=prefix_list,
                protocols=protocols,
                route_table=route_table,
                route_table_route=route_table_route,
                security_group=security_group,
                security_group_rule=security_group_rule,
                security_groups=security_groups,
                source_vpc=source_vpc,
                state=state,
                subnet=subnet,
                subnet_route_table=subnet_route_table,
                transit_gateway=transit_gateway,
                transit_gateway_attachment=transit_gateway_attachment,
                transit_gateway_route_table=transit_gateway_route_table,
                transit_gateway_route_table_route=transit_gateway_route_table_route,
                vpc=vpc,
                vpc_endpoint=vpc_endpoint,
                vpc_peering_connection=vpc_peering_connection,
                vpn_connection=vpn_connection,
                vpn_gateway=vpn_gateway,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl: list[Acl] | core.ArrayOut[Acl] = core.arg()

        acl_rule: list[AclRule] | core.ArrayOut[AclRule] = core.arg()

        address: str | core.StringOut = core.arg()

        addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo] = core.arg()

        availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        cidrs: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        classic_load_balancer_listener: list[ClassicLoadBalancerListener] | core.ArrayOut[
            ClassicLoadBalancerListener
        ] = core.arg()

        component: list[Component] | core.ArrayOut[Component] = core.arg()

        customer_gateway: list[CustomerGateway] | core.ArrayOut[CustomerGateway] = core.arg()

        destination: list[Destination] | core.ArrayOut[Destination] = core.arg()

        destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc] = core.arg()

        direction: str | core.StringOut = core.arg()

        elastic_load_balancer_listener: list[ElasticLoadBalancerListener] | core.ArrayOut[
            ElasticLoadBalancerListener
        ] = core.arg()

        explanation_code: str | core.StringOut = core.arg()

        ingress_route_table: list[IngressRouteTable] | core.ArrayOut[IngressRouteTable] = core.arg()

        internet_gateway: list[InternetGateway] | core.ArrayOut[InternetGateway] = core.arg()

        load_balancer_arn: str | core.StringOut = core.arg()

        load_balancer_listener_port: int | core.IntOut = core.arg()

        load_balancer_target_group: list[LoadBalancerTargetGroup] | core.ArrayOut[
            LoadBalancerTargetGroup
        ] = core.arg()

        load_balancer_target_groups: list[LoadBalancerTargetGroups] | core.ArrayOut[
            LoadBalancerTargetGroups
        ] = core.arg()

        load_balancer_target_port: int | core.IntOut = core.arg()

        missing_component: str | core.StringOut = core.arg()

        nat_gateway: list[NatGateway] | core.ArrayOut[NatGateway] = core.arg()

        network_interface: list[NetworkInterface] | core.ArrayOut[NetworkInterface] = core.arg()

        packet_field: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()

        port_ranges: list[PortRanges] | core.ArrayOut[PortRanges] = core.arg()

        prefix_list: list[PrefixList] | core.ArrayOut[PrefixList] = core.arg()

        protocols: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        route_table: list[RouteTable] | core.ArrayOut[RouteTable] = core.arg()

        route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute] = core.arg()

        security_group: list[SecurityGroup] | core.ArrayOut[SecurityGroup] = core.arg()

        security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule] = core.arg()

        security_groups: list[SecurityGroups] | core.ArrayOut[SecurityGroups] = core.arg()

        source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc] = core.arg()

        state: str | core.StringOut = core.arg()

        subnet: list[Subnet] | core.ArrayOut[Subnet] = core.arg()

        subnet_route_table: list[SubnetRouteTable] | core.ArrayOut[SubnetRouteTable] = core.arg()

        transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway] = core.arg()

        transit_gateway_attachment: list[TransitGatewayAttachment] | core.ArrayOut[
            TransitGatewayAttachment
        ] = core.arg()

        transit_gateway_route_table: list[TransitGatewayRouteTable] | core.ArrayOut[
            TransitGatewayRouteTable
        ] = core.arg()

        transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute] | core.ArrayOut[
            TransitGatewayRouteTableRoute
        ] = core.arg()

        vpc: list[Vpc] | core.ArrayOut[Vpc] = core.arg()

        vpc_endpoint: list[VpcEndpoint] | core.ArrayOut[VpcEndpoint] = core.arg()

        vpc_peering_connection: list[VpcPeeringConnection] | core.ArrayOut[
            VpcPeeringConnection
        ] = core.arg()

        vpn_connection: list[VpnConnection] | core.ArrayOut[VpnConnection] = core.arg()

        vpn_gateway: list[VpnGateway] | core.ArrayOut[VpnGateway] = core.arg()


@core.schema
class ForwardPathComponents(core.Schema):

    acl_rule: list[AclRule] | core.ArrayOut[AclRule] = core.attr(
        AclRule, computed=True, kind=core.Kind.array
    )

    additional_details: list[AdditionalDetails] | core.ArrayOut[AdditionalDetails] = core.attr(
        AdditionalDetails, computed=True, kind=core.Kind.array
    )

    attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo] = core.attr(
        AttachedTo, computed=True, kind=core.Kind.array
    )

    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc] = core.attr(
        DestinationVpc, computed=True, kind=core.Kind.array
    )

    inbound_header: list[InboundHeader] | core.ArrayOut[InboundHeader] = core.attr(
        InboundHeader, computed=True, kind=core.Kind.array
    )

    outbound_header: list[OutboundHeader] | core.ArrayOut[OutboundHeader] = core.attr(
        OutboundHeader, computed=True, kind=core.Kind.array
    )

    route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute] = core.attr(
        RouteTableRoute, computed=True, kind=core.Kind.array
    )

    security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule] = core.attr(
        SecurityGroupRule, computed=True, kind=core.Kind.array
    )

    sequence_number: int | core.IntOut = core.attr(int, computed=True)

    source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc] = core.attr(
        SourceVpc, computed=True, kind=core.Kind.array
    )

    subnet: list[Subnet] | core.ArrayOut[Subnet] = core.attr(
        Subnet, computed=True, kind=core.Kind.array
    )

    transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway] = core.attr(
        TransitGateway, computed=True, kind=core.Kind.array
    )

    transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute] | core.ArrayOut[
        TransitGatewayRouteTableRoute
    ] = core.attr(TransitGatewayRouteTableRoute, computed=True, kind=core.Kind.array)

    vpc: list[Vpc] | core.ArrayOut[Vpc] = core.attr(Vpc, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        acl_rule: list[AclRule] | core.ArrayOut[AclRule],
        additional_details: list[AdditionalDetails] | core.ArrayOut[AdditionalDetails],
        attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo],
        component: list[Component] | core.ArrayOut[Component],
        destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc],
        inbound_header: list[InboundHeader] | core.ArrayOut[InboundHeader],
        outbound_header: list[OutboundHeader] | core.ArrayOut[OutboundHeader],
        route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute],
        security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule],
        sequence_number: int | core.IntOut,
        source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc],
        subnet: list[Subnet] | core.ArrayOut[Subnet],
        transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway],
        transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute]
        | core.ArrayOut[TransitGatewayRouteTableRoute],
        vpc: list[Vpc] | core.ArrayOut[Vpc],
    ):
        super().__init__(
            args=ForwardPathComponents.Args(
                acl_rule=acl_rule,
                additional_details=additional_details,
                attached_to=attached_to,
                component=component,
                destination_vpc=destination_vpc,
                inbound_header=inbound_header,
                outbound_header=outbound_header,
                route_table_route=route_table_route,
                security_group_rule=security_group_rule,
                sequence_number=sequence_number,
                source_vpc=source_vpc,
                subnet=subnet,
                transit_gateway=transit_gateway,
                transit_gateway_route_table_route=transit_gateway_route_table_route,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl_rule: list[AclRule] | core.ArrayOut[AclRule] = core.arg()

        additional_details: list[AdditionalDetails] | core.ArrayOut[AdditionalDetails] = core.arg()

        attached_to: list[AttachedTo] | core.ArrayOut[AttachedTo] = core.arg()

        component: list[Component] | core.ArrayOut[Component] = core.arg()

        destination_vpc: list[DestinationVpc] | core.ArrayOut[DestinationVpc] = core.arg()

        inbound_header: list[InboundHeader] | core.ArrayOut[InboundHeader] = core.arg()

        outbound_header: list[OutboundHeader] | core.ArrayOut[OutboundHeader] = core.arg()

        route_table_route: list[RouteTableRoute] | core.ArrayOut[RouteTableRoute] = core.arg()

        security_group_rule: list[SecurityGroupRule] | core.ArrayOut[SecurityGroupRule] = core.arg()

        sequence_number: int | core.IntOut = core.arg()

        source_vpc: list[SourceVpc] | core.ArrayOut[SourceVpc] = core.arg()

        subnet: list[Subnet] | core.ArrayOut[Subnet] = core.arg()

        transit_gateway: list[TransitGateway] | core.ArrayOut[TransitGateway] = core.arg()

        transit_gateway_route_table_route: list[TransitGatewayRouteTableRoute] | core.ArrayOut[
            TransitGatewayRouteTableRoute
        ] = core.arg()

        vpc: list[Vpc] | core.ArrayOut[Vpc] = core.arg()


@core.schema
class AlternatePathHints(core.Schema):

    component_arn: str | core.StringOut = core.attr(str, computed=True)

    component_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        component_arn: str | core.StringOut,
        component_id: str | core.StringOut,
    ):
        super().__init__(
            args=AlternatePathHints.Args(
                component_arn=component_arn,
                component_id=component_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        component_arn: str | core.StringOut = core.arg()

        component_id: str | core.StringOut = core.arg()


@core.resource(type="aws_ec2_network_insights_analysis", namespace="vpc")
class Ec2NetworkInsightsAnalysis(core.Resource):
    """
    Potential intermediate components of a feasible path. Described below.
    """

    alternate_path_hints: list[AlternatePathHints] | core.ArrayOut[AlternatePathHints] = core.attr(
        AlternatePathHints, computed=True, kind=core.Kind.array
    )

    """
    ARN of the Network Insights Analysis.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Explanation codes for an unreachable path. See the [AWS documentation](https://docs.aws.amazon.com/A
    WSEC2/latest/APIReference/API_Explanation.html) for details.
    """
    explanations: list[Explanations] | core.ArrayOut[Explanations] = core.attr(
        Explanations, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A list of ARNs for resources the path must traverse.
    """
    filter_in_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The components in the path from source to destination. See the [AWS documentation](https://docs.aws.
    amazon.com/AWSEC2/latest/APIReference/API_PathComponent.html) for details.
    """
    forward_path_components: list[ForwardPathComponents] | core.ArrayOut[
        ForwardPathComponents
    ] = core.attr(ForwardPathComponents, computed=True, kind=core.Kind.array)

    """
    ID of the Network Insights Analysis.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the Network Insights Path to run an analysis on.
    """
    network_insights_path_id: str | core.StringOut = core.attr(str)

    """
    Set to `true` if the destination was reachable.
    """
    path_found: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The components in the path from destination to source. See the [AWS documentation](https://docs.aws.
    amazon.com/AWSEC2/latest/APIReference/API_PathComponent.html) for details.
    """
    return_path_components: list[ReturnPathComponents] | core.ArrayOut[
        ReturnPathComponents
    ] = core.attr(ReturnPathComponents, computed=True, kind=core.Kind.array)

    """
    The date/time the analysis was started.
    """
    start_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the analysis. `succeeded` means the analysis was completed, not that a path was found,
    for that see `path_found`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    A message to provide more context when the `status` is `failed`.
    """
    status_message: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with
    matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](/docs/providers/aws/index.html#default_tags-configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) If enabled, the resource will wait for the Network Insights Analysis status to change to
    succeeded` or `failed`. Setting this to `false` will skip the process. Default: `true`.
    """
    wait_for_completion: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The warning message.
    """
    warning_message: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        network_insights_path_id: str | core.StringOut,
        filter_in_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        wait_for_completion: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2NetworkInsightsAnalysis.Args(
                network_insights_path_id=network_insights_path_id,
                filter_in_arns=filter_in_arns,
                tags=tags,
                tags_all=tags_all,
                wait_for_completion=wait_for_completion,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        filter_in_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        network_insights_path_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        wait_for_completion: bool | core.BoolOut | None = core.arg(default=None)
