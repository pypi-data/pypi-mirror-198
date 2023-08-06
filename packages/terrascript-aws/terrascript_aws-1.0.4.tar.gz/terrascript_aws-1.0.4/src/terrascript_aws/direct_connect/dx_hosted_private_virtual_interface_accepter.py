import terrascript.core as core


@core.resource(type="aws_dx_hosted_private_virtual_interface_accepter", namespace="direct_connect")
class DxHostedPrivateVirtualInterfaceAccepter(core.Resource):
    """
    The ARN of the virtual interface.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the Direct Connect gateway to which to connect the virtual interface.
    """
    dx_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the virtual interface.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

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

    """
    (Required) The ID of the Direct Connect virtual interface to accept.
    """
    virtual_interface_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The ID of the [virtual private gateway](vpn_gateway.html) to which to connect the virtual
    interface.
    """
    vpn_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        virtual_interface_id: str | core.StringOut,
        dx_gateway_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpn_gateway_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedPrivateVirtualInterfaceAccepter.Args(
                virtual_interface_id=virtual_interface_id,
                dx_gateway_id=dx_gateway_id,
                tags=tags,
                tags_all=tags_all,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        dx_gateway_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        virtual_interface_id: str | core.StringOut = core.arg()

        vpn_gateway_id: str | core.StringOut | None = core.arg(default=None)
