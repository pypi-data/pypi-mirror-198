import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_route_table", namespace="transit_gateway")
class Ec2TransitGatewayRouteTable(core.Resource):
    """
    EC2 Transit Gateway Route Table Amazon Resource Name (ARN).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Boolean whether this is the default association route table for the EC2 Transit Gateway.
    """
    default_association_route_table: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Boolean whether this is the default propagation route table for the EC2 Transit Gateway.
    """
    default_propagation_route_table: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    EC2 Transit Gateway Route Table identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value tags for the EC2 Transit Gateway Route Table. If configured with a provider [`d
    efault_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#
    default_tags-configuration-block) present, tags with matching keys will overwrite those defined at t
    he provider-level.
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
    (Required) Identifier of EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayRouteTable.Args(
                transit_gateway_id=transit_gateway_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut = core.arg()
