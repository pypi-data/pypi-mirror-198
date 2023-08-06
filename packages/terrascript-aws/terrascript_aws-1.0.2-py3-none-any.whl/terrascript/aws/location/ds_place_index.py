import terrascript.core as core


@core.schema
class DataSourceConfiguration(core.Schema):

    intended_use: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        intended_use: str | core.StringOut,
    ):
        super().__init__(
            args=DataSourceConfiguration.Args(
                intended_use=intended_use,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intended_use: str | core.StringOut = core.arg()


@core.data(type="aws_location_place_index", namespace="aws_location")
class DsPlaceIndex(core.Data):

    create_time: str | core.StringOut = core.attr(str, computed=True)

    data_source: str | core.StringOut = core.attr(str, computed=True)

    data_source_configuration: list[DataSourceConfiguration] | core.ArrayOut[
        DataSourceConfiguration
    ] = core.attr(DataSourceConfiguration, computed=True, kind=core.Kind.array)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    index_arn: str | core.StringOut = core.attr(str, computed=True)

    index_name: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        index_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPlaceIndex.Args(
                index_name=index_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
