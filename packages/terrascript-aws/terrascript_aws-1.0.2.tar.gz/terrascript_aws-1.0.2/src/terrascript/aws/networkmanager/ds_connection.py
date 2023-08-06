import terrascript.core as core


@core.data(type="aws_networkmanager_connection", namespace="aws_networkmanager")
class DsConnection(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    connected_device_id: str | core.StringOut = core.attr(str, computed=True)

    connected_link_id: str | core.StringOut = core.attr(str, computed=True)

    connection_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut = core.attr(str, computed=True)

    device_id: str | core.StringOut = core.attr(str, computed=True)

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    link_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        connection_id: str | core.StringOut,
        global_network_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConnection.Args(
                connection_id=connection_id,
                global_network_id=global_network_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_id: str | core.StringOut = core.arg()

        global_network_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
