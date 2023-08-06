import terrascript.core as core


@core.resource(type="aws_network_interface_attachment", namespace="aws_vpc")
class NetworkInterfaceAttachment(core.Resource):

    attachment_id: str | core.StringOut = core.attr(str, computed=True)

    device_index: int | core.IntOut = core.attr(int)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    network_interface_id: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        device_index: int | core.IntOut,
        instance_id: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkInterfaceAttachment.Args(
                device_index=device_index,
                instance_id=instance_id,
                network_interface_id=network_interface_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_index: int | core.IntOut = core.arg()

        instance_id: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()
