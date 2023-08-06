import terrascript.core as core


@core.schema
class Configuration(core.Schema):

    style: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        style: str | core.StringOut,
    ):
        super().__init__(
            args=Configuration.Args(
                style=style,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        style: str | core.StringOut = core.arg()


@core.data(type="aws_location_map", namespace="location")
class DsMap(core.Data):
    """
    List of configurations that specify the map tile style selected from a partner data provider.
    """

    configuration: list[Configuration] | core.ArrayOut[Configuration] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    """
    The timestamp for when the map resource was created in ISO 8601 format.
    """
    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The optional description for the map resource.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) for the map resource.
    """
    map_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the map resource.
    """
    map_name: str | core.StringOut = core.attr(str)

    """
    Key-value map of resource tags for the map.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The timestamp for when the map resource was last updated in ISO 8601 format.
    """
    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        map_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMap.Args(
                map_name=map_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        map_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
