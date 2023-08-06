import terrascript.core as core


@core.resource(type="aws_vpc_dhcp_options", namespace="vpc")
class DhcpOptions(core.Resource):
    """
    The ARN of the DHCP Options Set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) the suffix domain name to use by default when resolving non Fully Qualified Domain Names.
    In other words, this is what ends up being the `search` value in the `/etc/resolv.conf` file.
    """
    domain_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) List of name servers to configure in `/etc/resolv.conf`. If you want to use the default A
    WS nameservers you should set this to `AmazonProvidedDNS`.
    """
    domain_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the DHCP Options Set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of NETBIOS name servers.
    """
    netbios_name_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and mu
    lticast are not supported in their network. For more information about these node types, see [RFC 21
    32](http://www.ietf.org/rfc/rfc2132.txt).
    """
    netbios_node_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) List of NTP servers to configure.
    """
    ntp_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the AWS account that owns the DHCP options set.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
