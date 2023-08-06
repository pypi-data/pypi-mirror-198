import terrascript.core as core


@core.resource(type="aws_network_interface_sg_attachment", namespace="vpc")
class NetworkInterfaceSgAttachment(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the network interface to attach to.
    """
    network_interface_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the security group.
    """
    security_group_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        network_interface_id: str | core.StringOut,
        security_group_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkInterfaceSgAttachment.Args(
                network_interface_id=network_interface_id,
                security_group_id=security_group_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        network_interface_id: str | core.StringOut = core.arg()

        security_group_id: str | core.StringOut = core.arg()
