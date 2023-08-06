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
class Associations(core.Schema):

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    transit_gateway_attachment_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        subnet_id: str | core.StringOut,
        transit_gateway_attachment_id: str | core.StringOut,
    ):
        super().__init__(
            args=Associations.Args(
                subnet_id=subnet_id,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_id: str | core.StringOut = core.arg()

        transit_gateway_attachment_id: str | core.StringOut = core.arg()


@core.schema
class Sources(core.Schema):

    group_ip_address: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        group_ip_address: str | core.StringOut,
        network_interface_id: str | core.StringOut,
    ):
        super().__init__(
            args=Sources.Args(
                group_ip_address=group_ip_address,
                network_interface_id=network_interface_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_ip_address: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()


@core.schema
class Members(core.Schema):

    group_ip_address: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        group_ip_address: str | core.StringOut,
        network_interface_id: str | core.StringOut,
    ):
        super().__init__(
            args=Members.Args(
                group_ip_address=group_ip_address,
                network_interface_id=network_interface_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_ip_address: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()


@core.data(type="aws_ec2_transit_gateway_multicast_domain", namespace="transit_gateway")
class DsEc2TransitGatewayMulticastDomain(core.Data):
    """
    EC2 Transit Gateway Multicast Domain Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    EC2 Transit Gateway Multicast Domain Associations
    """
    associations: list[Associations] | core.ArrayOut[Associations] = core.attr(
        Associations, computed=True, kind=core.Kind.array
    )

    """
    Whether to automatically accept cross-account subnet associations that are associated with the EC2 T
    ransit Gateway Multicast Domain.
    """
    auto_accept_shared_associations: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    EC2 Transit Gateway Multicast Domain identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether to enable Internet Group Management Protocol (IGMP) version 2 for the EC2 Transit Gateway Mu
    lticast Domain.
    """
    igmpv2_support: str | core.StringOut = core.attr(str, computed=True)

    """
    EC2 Multicast Domain Group Members
    """
    members: list[Members] | core.ArrayOut[Members] = core.attr(
        Members, computed=True, kind=core.Kind.array
    )

    """
    Identifier of the AWS account that owns the EC2 Transit Gateway Multicast Domain.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    EC2 Multicast Domain Group Sources
    """
    sources: list[Sources] | core.ArrayOut[Sources] = core.attr(
        Sources, computed=True, kind=core.Kind.array
    )

    state: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether to enable support for statically configuring multicast group sources for the EC2 Transit Gat
    eway Multicast Domain.
    """
    static_sources_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the EC2 Transit Gateway Multicast Domain.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The ID of the transit gateway attachment.
    """
    transit_gateway_attachment_id: str | core.StringOut = core.attr(str, computed=True)

    """
    EC2 Transit Gateway identifier.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Identifier of the EC2 Transit Gateway Multicast Domain.
    """
    transit_gateway_multicast_domain_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_multicast_domain_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayMulticastDomain.Args(
                filter=filter,
                tags=tags,
                transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_multicast_domain_id: str | core.StringOut | None = core.arg(default=None)
