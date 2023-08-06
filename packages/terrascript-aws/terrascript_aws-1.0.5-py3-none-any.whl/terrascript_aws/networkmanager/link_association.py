import terrascript.core as core


@core.resource(type="aws_networkmanager_link_association", namespace="networkmanager")
class LinkAssociation(core.Resource):
    """
    (Required) The ID of the device.
    """

    device_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the global network.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the link.
    """
    link_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        device_id: str | core.StringOut,
        global_network_id: str | core.StringOut,
        link_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LinkAssociation.Args(
                device_id=device_id,
                global_network_id=global_network_id,
                link_id=link_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_id: str | core.StringOut = core.arg()

        global_network_id: str | core.StringOut = core.arg()

        link_id: str | core.StringOut = core.arg()
