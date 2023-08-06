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


@core.data(type="aws_vpc_dhcp_options", namespace="vpc")
class DsDhcpOptions(core.Data):
    """
    The ARN of the DHCP Options Set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The EC2 DHCP Options ID.
    """
    dhcp_options_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The suffix domain name to used when resolving non Fully Qualified Domain NamesE.g., the `search` val
    ue in the `/etc/resolv.conf` file.
    """
    domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    List of name servers.
    """
    domain_name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) List of custom filters as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    EC2 DHCP Options ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of NETBIOS name servers.
    """
    netbios_name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The NetBIOS node type (1, 2, 4, or 8). For more information about these node types, see [RFC 2132](h
    ttp://www.ietf.org/rfc/rfc2132.txt).
    """
    netbios_node_type: str | core.StringOut = core.attr(str, computed=True)

    """
    List of NTP servers.
    """
    ntp_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The ID of the AWS account that owns the DHCP options set.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        dhcp_options_id: str | core.StringOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDhcpOptions.Args(
                dhcp_options_id=dhcp_options_id,
                filter=filter,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dhcp_options_id: str | core.StringOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
