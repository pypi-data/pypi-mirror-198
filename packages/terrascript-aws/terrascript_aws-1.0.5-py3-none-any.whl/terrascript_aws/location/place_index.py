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


@core.resource(type="aws_location_place_index", namespace="location")
class PlaceIndex(core.Resource):
    """
    The timestamp for when the place index resource was created in ISO 8601 format.
    """

    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the geospatial data provider for the new place index.
    """
    data_source: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block with the data storage option chosen for requesting Places. Detailed b
    elow.
    """
    data_source_configuration: DataSourceConfiguration | None = core.attr(
        DataSourceConfiguration, default=None, computed=True
    )

    """
    (Optional) The optional description for the place index resource.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) for the place index resource. Used to specify a resource across AWS.
    """
    index_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the place index resource.
    """
    index_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value tags for the place index. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    The timestamp for when the place index resource was last update in ISO 8601.
    """
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
