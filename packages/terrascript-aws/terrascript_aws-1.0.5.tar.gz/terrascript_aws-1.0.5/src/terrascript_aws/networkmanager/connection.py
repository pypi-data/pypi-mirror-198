import terrascript.core as core


@core.resource(type="aws_networkmanager_connection", namespace="networkmanager")
class Connection(core.Resource):
    """
    The Amazon Resource Name (ARN) of the connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the second device in the connection.
    """
    connected_device_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The ID of the link for the second device.
    """
    connected_link_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A description of the connection.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the first device in the connection.
    """
    device_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the global network.
    """
    global_network_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the link for the first device.
    """
    link_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value tags for the connection. If configured with a provider [`default_tags` configur
    ation block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configur
    ation-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
