import terrascript.core as core


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


@core.schema
class DnsOptions(core.Schema):

    dns_record_ip_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dns_record_ip_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DnsOptions.Args(
                dns_record_ip_type=dns_record_ip_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_record_ip_type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_vpc_endpoint", namespace="aws_vpc")
class Endpoint(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_accept: bool | core.BoolOut | None = core.attr(bool, default=None)

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    dns_entry: list[DnsEntry] | core.ArrayOut[DnsEntry] = core.attr(
        DnsEntry, computed=True, kind=core.Kind.array
    )

    dns_options: DnsOptions | None = core.attr(DnsOptions, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    prefix_list_id: str | core.StringOut = core.attr(str, computed=True)

    private_dns_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    requester_managed: bool | core.BoolOut = core.attr(bool, computed=True)

    route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    service_name: str | core.StringOut = core.attr(str)

    state: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_type: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        service_name: str | core.StringOut,
        vpc_id: str | core.StringOut,
        auto_accept: bool | core.BoolOut | None = None,
        dns_options: DnsOptions | None = None,
        ip_address_type: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        private_dns_enabled: bool | core.BoolOut | None = None,
        route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_endpoint_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                service_name=service_name,
                vpc_id=vpc_id,
                auto_accept=auto_accept,
                dns_options=dns_options,
                ip_address_type=ip_address_type,
                policy=policy,
                private_dns_enabled=private_dns_enabled,
                route_table_ids=route_table_ids,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_type=vpc_endpoint_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_accept: bool | core.BoolOut | None = core.arg(default=None)

        dns_options: DnsOptions | None = core.arg(default=None)

        ip_address_type: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        private_dns_enabled: bool | core.BoolOut | None = core.arg(default=None)

        route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        service_name: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_type: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
