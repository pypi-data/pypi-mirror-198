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


@core.data(type="aws_location_place_index", namespace="location")
class DsPlaceIndex(core.Data):
    """
    The timestamp for when the place index resource was created in ISO 8601 format.
    """

    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The data provider of geospatial data.
    """
    data_source: str | core.StringOut = core.attr(str, computed=True)

    """
    List of configurations that specify data storage option for requesting Places.
    """
    data_source_configuration: list[DataSourceConfiguration] | core.ArrayOut[
        DataSourceConfiguration
    ] = core.attr(DataSourceConfiguration, computed=True, kind=core.Kind.array)

    """
    The optional description for the place index resource.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) for the place index resource.
    """
    index_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the place index resource.
    """
    index_name: str | core.StringOut = core.attr(str)

    """
    Key-value map of resource tags for the place index.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The timestamp for when the place index resource was last updated in ISO 8601 format.
    """
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
