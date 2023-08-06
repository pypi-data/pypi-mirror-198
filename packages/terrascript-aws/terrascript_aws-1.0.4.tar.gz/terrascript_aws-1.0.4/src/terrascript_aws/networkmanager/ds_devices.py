import terrascript.core as core


@core.data(type="aws_networkmanager_devices", namespace="networkmanager")
class DsDevices(core.Data):
    """
    (Required) The ID of the Global Network of the devices to retrieve.
    """

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IDs of the devices.
    """
    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ID of the site of the devices to retrieve.
    """
    site_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Restricts the list to the devices with these tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: str | core.StringOut,
        site_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDevices.Args(
                global_network_id=global_network_id,
                site_id=site_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: str | core.StringOut = core.arg()

        site_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
