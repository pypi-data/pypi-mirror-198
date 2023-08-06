import terrascript.core as core


@core.data(type="aws_networkmanager_global_network", namespace="networkmanager")
class DsGlobalNetwork(core.Data):
    """
    The ARN of the global network.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the global network.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The id of the specific global network to retrieve.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGlobalNetwork.Args(
                global_network_id=global_network_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
