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


@core.data(type="aws_location_map", namespace="aws_location")
class DsMap(core.Data):

    configuration: list[Configuration] | core.ArrayOut[Configuration] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    create_time: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    map_arn: str | core.StringOut = core.attr(str, computed=True)

    map_name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
