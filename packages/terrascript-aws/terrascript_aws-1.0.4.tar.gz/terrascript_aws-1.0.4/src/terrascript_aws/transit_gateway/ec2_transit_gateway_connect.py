import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_connect", namespace="transit_gateway")
class Ec2TransitGatewayConnect(core.Resource):
    """
    EC2 Transit Gateway Attachment identifier
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The tunnel protocol. Valida values: `gre`. Default is `gre`.
    """
    protocol: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway Connect. If configured with a provider [`defau
    lt_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defa
    ult_tags-configuration-block) present, tags with matching keys will overwrite those defined at the p
    rovider-level.
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
    (Optional) Boolean whether the Connect should be associated with the EC2 Transit Gateway association
    default route table. This cannot be configured or perform drift detection with Resource Access Mana
    ger shared EC2 Transit Gateways. Default value: `true`.
    """
    transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Optional) Boolean whether the Connect should propagate routes with the EC2 Transit Gateway propagat
    ion default route table. This cannot be configured or perform drift detection with Resource Access M
    anager shared EC2 Transit Gateways. Default value: `true`.
    """
    transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Required) Identifier of EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str)

    """
    (Required) The underlaying VPC attachment
    """
    transport_attachment_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_id: str | core.StringOut,
        transport_attachment_id: str | core.StringOut,
        protocol: str | core.StringOut | None = None,
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
            args=Ec2TransitGatewayConnect.Args(
                transit_gateway_id=transit_gateway_id,
                transport_attachment_id=transport_attachment_id,
                protocol=protocol,
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
        protocol: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_default_route_table_association: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_default_route_table_propagation: bool | core.BoolOut | None = core.arg(
            default=None
        )

        transit_gateway_id: str | core.StringOut = core.arg()

        transport_attachment_id: str | core.StringOut = core.arg()
