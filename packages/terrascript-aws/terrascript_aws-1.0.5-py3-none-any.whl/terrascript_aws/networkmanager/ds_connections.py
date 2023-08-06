import terrascript.core as core


@core.data(type="aws_networkmanager_connections", namespace="networkmanager")
class DsConnections(core.Data):
    """
    (Optional) The ID of the device of the connections to retrieve.
    """

    device_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the Global Network of the connections to retrieve.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IDs of the connections.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Restricts the list to the connections with these tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: str | core.StringOut,
        device_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConnections.Args(
                global_network_id=global_network_id,
                device_id=device_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_id: str | core.StringOut | None = core.arg(default=None)

        global_network_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
