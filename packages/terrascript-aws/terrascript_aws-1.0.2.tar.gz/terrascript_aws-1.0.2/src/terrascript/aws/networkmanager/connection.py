import terrascript.core as core


@core.resource(type="aws_networkmanager_connection", namespace="aws_networkmanager")
class Connection(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    connected_device_id: str | core.StringOut = core.attr(str)

    connected_link_id: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    device_id: str | core.StringOut = core.attr(str)

    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    link_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        connected_device_id: str | core.StringOut,
        device_id: str | core.StringOut,
        global_network_id: str | core.StringOut,
        connected_link_id: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        link_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                connected_device_id=connected_device_id,
                device_id=device_id,
                global_network_id=global_network_id,
                connected_link_id=connected_link_id,
                description=description,
                link_id=link_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connected_device_id: str | core.StringOut = core.arg()

        connected_link_id: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        device_id: str | core.StringOut = core.arg()

        global_network_id: str | core.StringOut = core.arg()

        link_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
