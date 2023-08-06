import terrascript.core as core


@core.data(type="aws_networkmanager_connection", namespace="networkmanager")
class DsConnection(core.Data):
    """
    The ARN of the connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the second device in the connection.
    """
    connected_device_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the link for the second device.
    """
    connected_link_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The id of the specific connection to retrieve.
    """
    connection_id: str | core.StringOut = core.attr(str)

    """
    A description of the connection.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the first device in the connection.
    """
    device_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Global Network of the connection to retrieve.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the link for the first device.
    """
    link_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value tags for the connection.
    """
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
