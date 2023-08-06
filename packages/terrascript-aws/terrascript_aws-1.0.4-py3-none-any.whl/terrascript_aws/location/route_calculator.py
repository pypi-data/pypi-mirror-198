import terrascript.core as core


@core.resource(type="aws_location_route_calculator", namespace="location")
class RouteCalculator(core.Resource):
    """
    The Amazon Resource Name (ARN) for the Route calculator resource. Use the ARN when you specify a res
    ource across AWS.
    """

    calculator_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the route calculator resource.
    """
    calculator_name: str | core.StringOut = core.attr(str)

    """
    The timestamp for when the route calculator resource was created in ISO 8601 format.
    """
    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the data provider of traffic and road network data.
    """
    data_source: str | core.StringOut = core.attr(str)

    """
    (Optional) The optional description for the route calculator resource.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value tags for the route calculator. If configured with a provider [`default_tags` co
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

    """
    The timestamp for when the route calculator resource was last update in ISO 8601.
    """
    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        calculator_name: str | core.StringOut,
        data_source: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RouteCalculator.Args(
                calculator_name=calculator_name,
                data_source=data_source,
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
        calculator_name: str | core.StringOut = core.arg()

        data_source: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
