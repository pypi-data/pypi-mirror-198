import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_vpc_attachment", namespace="transit_gateway")
class Ec2TransitGatewayVpcAttachment(core.Resource):
    """
    (Optional) Whether Appliance Mode support is enabled. If enabled, a traffic flow between a source an
    d destination uses the same Availability Zone for the VPC attachment for the lifetime of that flow.
    Valid values: `disable`, `enable`. Default value: `disable`.
    """

    appliance_mode_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable
    .
    """
    dns_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    EC2 Transit Gateway Attachment identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether IPv6 support is enabled. Valid values: `disable`, `enable`. Default value: `disab
    le`.
    """
    ipv6_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Identifiers of EC2 Subnets.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway VPC Attachment. If configured with a provider
    [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/do
    cs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined a
    t the provider-level.
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

    """
    (Optional) Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway asso
    ciation default route table. This cannot be configured or perform drift detection with Resource Acce
    ss Manager shared EC2 Transit Gateways. Default value: `true`.
    """
    transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Optional) Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway p
    ropagation default route table. This cannot be configured or perform drift detection with Resource A
    ccess Manager shared EC2 Transit Gateways. Default value: `true`.
    """
    transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Required) Identifier of EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str)

    """
    (Required) Identifier of EC2 VPC.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    """
    Identifier of the AWS account that owns the EC2 VPC.
    """
    vpc_owner_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        transit_gateway_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        appliance_mode_support: str | core.StringOut | None = None,
        dns_support: str | core.StringOut | None = None,
        ipv6_support: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_default_route_table_association: bool | core.BoolOut | None = None,
        transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayVpcAttachment.Args(
                subnet_ids=subnet_ids,
                transit_gateway_id=transit_gateway_id,
                vpc_id=vpc_id,
                appliance_mode_support=appliance_mode_support,
                dns_support=dns_support,
                ipv6_support=ipv6_support,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_default_route_table_association=transit_gateway_default_route_table_association,
                transit_gateway_default_route_table_propagation=transit_gateway_default_route_table_propagation,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        appliance_mode_support: str | core.StringOut | None = core.arg(default=None)

        dns_support: str | core.StringOut | None = core.arg(default=None)

        ipv6_support: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()
