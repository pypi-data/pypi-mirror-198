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


@core.data(type="aws_subnet", namespace="aws_vpc")
class DsSubnet(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    assign_ipv6_address_on_creation: bool | core.BoolOut = core.attr(bool, computed=True)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    availability_zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    available_ip_address_count: int | core.IntOut = core.attr(int, computed=True)

    cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    customer_owned_ipv4_pool: str | core.StringOut = core.attr(str, computed=True)

    default_for_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    enable_dns64: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_resource_name_dns_a_record_on_launch: bool | core.BoolOut = core.attr(
        bool, computed=True
    )

    enable_resource_name_dns_aaaa_record_on_launch: bool | core.BoolOut = core.attr(
        bool, computed=True
    )

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ipv6_cidr_block_association_id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_native: bool | core.BoolOut = core.attr(bool, computed=True)

    map_customer_owned_ip_on_launch: bool | core.BoolOut = core.attr(bool, computed=True)

    map_public_ip_on_launch: bool | core.BoolOut = core.attr(bool, computed=True)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns_hostname_type_on_launch: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: str | core.StringOut | None = None,
        availability_zone_id: str | core.StringOut | None = None,
        cidr_block: str | core.StringOut | None = None,
        default_for_az: bool | core.BoolOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubnet.Args(
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                cidr_block=cidr_block,
                default_for_az=default_for_az,
                filter=filter,
                id=id,
                ipv6_cidr_block=ipv6_cidr_block,
                state=state,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        availability_zone_id: str | core.StringOut | None = core.arg(default=None)

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        default_for_az: bool | core.BoolOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
