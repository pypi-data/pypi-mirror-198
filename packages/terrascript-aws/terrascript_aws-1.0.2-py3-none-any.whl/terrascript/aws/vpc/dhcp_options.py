import terrascript.core as core


@core.resource(type="aws_vpc_dhcp_options", namespace="aws_vpc")
class DhcpOptions(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut | None = core.attr(str, default=None)

    domain_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    netbios_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    netbios_node_type: str | core.StringOut | None = core.attr(str, default=None)

    ntp_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut | None = None,
        domain_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        netbios_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        netbios_node_type: str | core.StringOut | None = None,
        ntp_servers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DhcpOptions.Args(
                domain_name=domain_name,
                domain_name_servers=domain_name_servers,
                netbios_name_servers=netbios_name_servers,
                netbios_node_type=netbios_node_type,
                ntp_servers=ntp_servers,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: str | core.StringOut | None = core.arg(default=None)

        domain_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        netbios_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        netbios_node_type: str | core.StringOut | None = core.arg(default=None)

        ntp_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
