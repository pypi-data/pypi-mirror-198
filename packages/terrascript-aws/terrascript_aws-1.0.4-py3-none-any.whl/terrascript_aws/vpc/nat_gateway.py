import terrascript.core as core


@core.resource(type="aws_nat_gateway", namespace="vpc")
class NatGateway(core.Resource):
    """
    (Optional) The Allocation ID of the Elastic IP address for the gateway. Required for `connectivity_t
    ype` of `public`.
    """

    allocation_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Connectivity type for the gateway. Valid values are `private` and `public`. Defaults to `
    public`.
    """
    connectivity_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the NAT Gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ENI ID of the network interface created by the NAT gateway.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The private IP address of the NAT Gateway.
    """
    private_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    The public IP address of the NAT Gateway.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Subnet ID of the subnet in which to place the gateway.
    """
    subnet_id: str | core.StringOut = core.attr(str)

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
        subnet_id: str | core.StringOut,
        allocation_id: str | core.StringOut | None = None,
        connectivity_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NatGateway.Args(
                subnet_id=subnet_id,
                allocation_id=allocation_id,
                connectivity_type=connectivity_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocation_id: str | core.StringOut | None = core.arg(default=None)

        connectivity_type: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
