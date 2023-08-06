import terrascript.core as core


@core.schema
class DnsOptions(core.Schema):

    dns_record_ip_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_record_ip_type: str | core.StringOut,
    ):
        super().__init__(
            args=DnsOptions.Args(
                dns_record_ip_type=dns_record_ip_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_record_ip_type: str | core.StringOut = core.arg()


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
class DnsEntry(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        hosted_zone_id: str | core.StringOut,
    ):
        super().__init__(
            args=DnsEntry.Args(
                dns_name=dns_name,
                hosted_zone_id=hosted_zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        hosted_zone_id: str | core.StringOut = core.arg()


@core.data(type="aws_vpc_endpoint", namespace="aws_vpc")
class DsEndpoint(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    dns_entry: list[DnsEntry] | core.ArrayOut[DnsEntry] = core.attr(
        DnsEntry, computed=True, kind=core.Kind.array
    )

    dns_options: list[DnsOptions] | core.ArrayOut[DnsOptions] = core.attr(
        DnsOptions, computed=True, kind=core.Kind.array
    )

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ip_address_type: str | core.StringOut = core.attr(str, computed=True)

    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str, computed=True)

    prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    requester_managed: bool | core.BoolOut = core.attr(bool, computed=True)

    route_table_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    service_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        service_name: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpoint.Args(
                filter=filter,
                id=id,
                service_name=service_name,
                state=state,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        service_name: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
