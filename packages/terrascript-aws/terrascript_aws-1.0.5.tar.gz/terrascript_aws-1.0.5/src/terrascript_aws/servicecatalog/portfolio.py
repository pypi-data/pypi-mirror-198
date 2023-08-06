import terrascript.core as core


@core.resource(type="aws_servicecatalog_portfolio", namespace="servicecatalog")
class Portfolio(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Description of the portfolio
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ID of the Service Catalog Portfolio.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the portfolio.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Name of the person or organization who owns the portfolio.
    """
    provider_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Tags to apply to the connection. If configured with a provider [`default_tags` configurat
    ion block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurat
    ion-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        name: str | core.StringOut,
        provider_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Portfolio.Args(
                name=name,
                provider_name=provider_name,
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
        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
