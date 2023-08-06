import terrascript.core as core


@core.resource(type="aws_dataexchange_data_set", namespace="dataexchange")
class DataSet(core.Resource):
    """
    The Amazon Resource Name of this data set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of asset that is added to a data set. Valid values are: `S3_SNAPSHOT`, `REDSHIFT
    _DATA_SHARE`, and `API_GATEWAY_API`.
    """
    asset_type: str | core.StringOut = core.attr(str)

    """
    (Required) A description for the data set.
    """
    description: str | core.StringOut = core.attr(str)

    """
    The Id of the data set.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the data set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
        asset_type: str | core.StringOut,
        description: str | core.StringOut,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataSet.Args(
                asset_type=asset_type,
                description=description,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        asset_type: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
