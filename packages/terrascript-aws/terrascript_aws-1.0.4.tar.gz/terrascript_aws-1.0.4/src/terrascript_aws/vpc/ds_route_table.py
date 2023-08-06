import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Routes(core.Schema):

    carrier_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    destination_prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    egress_only_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    gateway_id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_cidr_block: str | core.StringOut = core.attr(str, computed=True)

    local_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    nat_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_endpoint_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_peering_connection_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        carrier_gateway_id: str | core.StringOut,
        cidr_block: str | core.StringOut,
        core_network_arn: str | core.StringOut,
        destination_prefix_list_id: str | core.StringOut,
        egress_only_gateway_id: str | core.StringOut,
        gateway_id: str | core.StringOut,
        instance_id: str | core.StringOut,
        ipv6_cidr_block: str | core.StringOut,
        local_gateway_id: str | core.StringOut,
        nat_gateway_id: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        transit_gateway_id: str | core.StringOut,
        vpc_endpoint_id: str | core.StringOut,
        vpc_peering_connection_id: str | core.StringOut,
    ):
        super().__init__(
            args=Routes.Args(
                carrier_gateway_id=carrier_gateway_id,
                cidr_block=cidr_block,
                core_network_arn=core_network_arn,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_gateway_id=egress_only_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                ipv6_cidr_block=ipv6_cidr_block,
                local_gateway_id=local_gateway_id,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                transit_gateway_id=transit_gateway_id,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        carrier_gateway_id: str | core.StringOut = core.arg()

        cidr_block: str | core.StringOut = core.arg()

        core_network_arn: str | core.StringOut = core.arg()

        destination_prefix_list_id: str | core.StringOut = core.arg()

        egress_only_gateway_id: str | core.StringOut = core.arg()

        gateway_id: str | core.StringOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        ipv6_cidr_block: str | core.StringOut = core.arg()

        local_gateway_id: str | core.StringOut = core.arg()

        nat_gateway_id: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()

        transit_gateway_id: str | core.StringOut = core.arg()

        vpc_endpoint_id: str | core.StringOut = core.arg()

        vpc_peering_connection_id: str | core.StringOut = core.arg()


@core.schema
class Associations(core.Schema):

    gateway_id: str | core.StringOut = core.attr(str, computed=True)

    main: bool | core.BoolOut = core.attr(bool, computed=True)

    route_table_association_id: str | core.StringOut = core.attr(str, computed=True)

    route_table_id: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        gateway_id: str | core.StringOut,
        main: bool | core.BoolOut,
        route_table_association_id: str | core.StringOut,
        route_table_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=Associations.Args(
                gateway_id=gateway_id,
                main=main,
                route_table_association_id=route_table_association_id,
                route_table_id=route_table_id,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        gateway_id: str | core.StringOut = core.arg()

        main: bool | core.BoolOut = core.arg()

        route_table_association_id: str | core.StringOut = core.arg()

        route_table_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.data(type="aws_route_table", namespace="vpc")
class DsRouteTable(core.Data):
    """
    ARN of the route table.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    List of associations with attributes detailed below.
    """
    associations: list[Associations] | core.ArrayOut[Associations] = core.attr(
        Associations, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) ID of an Internet Gateway or Virtual Private Gateway which is connected to the Route Tabl
    e (not exported if not passed as a parameter).
    """
    gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ID of the AWS account that owns the route table.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ID of the specific Route Table to retrieve.
    """
    route_table_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    List of routes with attributes detailed below.
    """
    routes: list[Routes] | core.ArrayOut[Routes] = core.attr(
        Routes, computed=True, kind=core.Kind.array
    )

    """
    (Optional) ID of a Subnet which is connected to the Route Table (not exported if not passed as a par
    ameter).
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags, each pair of which must exactly match a pair on the desired Route Table.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) ID of the VPC that the desired Route Table belongs to.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        gateway_id: str | core.StringOut | None = None,
        route_table_id: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRouteTable.Args(
                filter=filter,
                gateway_id=gateway_id,
                route_table_id=route_table_id,
                subnet_id=subnet_id,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        gateway_id: str | core.StringOut | None = core.arg(default=None)

        route_table_id: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
