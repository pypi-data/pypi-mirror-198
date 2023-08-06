import terrascript.core as core


@core.schema
class DataSourceConfiguration(core.Schema):

    intended_use: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        intended_use: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DataSourceConfiguration.Args(
                intended_use=intended_use,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intended_use: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_location_place_index", namespace="aws_location")
class PlaceIndex(core.Resource):

    create_time: str | core.StringOut = core.attr(str, computed=True)

    data_source: str | core.StringOut = core.attr(str)

    data_source_configuration: DataSourceConfiguration | None = core.attr(
        DataSourceConfiguration, default=None, computed=True
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_arn: str | core.StringOut = core.attr(str, computed=True)

    index_name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        data_source: str | core.StringOut,
        index_name: str | core.StringOut,
        data_source_configuration: DataSourceConfiguration | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PlaceIndex.Args(
                data_source=data_source,
                index_name=index_name,
                data_source_configuration=data_source_configuration,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data_source: str | core.StringOut = core.arg()

        data_source_configuration: DataSourceConfiguration | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        index_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
