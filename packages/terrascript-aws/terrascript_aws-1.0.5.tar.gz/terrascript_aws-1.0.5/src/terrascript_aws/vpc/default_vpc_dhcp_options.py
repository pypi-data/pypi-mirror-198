import terrascript.core as core


@core.resource(type="aws_default_vpc_dhcp_options", namespace="vpc")
class DefaultVpcDhcpOptions(core.Resource):
    """
    The ARN of the DHCP Options Set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    domain_name: str | core.StringOut = core.attr(str, computed=True)

    domain_name_servers: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the DHCP Options Set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of NETBIOS name servers.
    """
    netbios_name_servers: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and mu
    lticast are not supported in their network. For more information about these node types, see [RFC 21
    32](http://www.ietf.org/rfc/rfc2132.txt).
    """
    netbios_node_type: str | core.StringOut = core.attr(str, computed=True)

    ntp_servers: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the DHCP options set.
    """
    owner_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the resource.
    """
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
        owner_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultVpcDhcpOptions.Args(
                owner_id=owner_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        owner_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
