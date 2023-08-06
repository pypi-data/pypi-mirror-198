import terrascript.core as core


@core.schema
class RoutingStrategy(core.Schema):

    fleet_id: str | core.StringOut | None = core.attr(str, default=None)

    message: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        fleet_id: str | core.StringOut | None = None,
        message: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RoutingStrategy.Args(
                type=type,
                fleet_id=fleet_id,
                message=message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fleet_id: str | core.StringOut | None = core.arg(default=None)

        message: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_gamelift_alias", namespace="gamelift")
class Alias(core.Resource):
    """
    Alias ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the alias.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Alias ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the alias.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the fleet and/or routing type to use for the alias.
    """
    routing_strategy: RoutingStrategy = core.attr(RoutingStrategy)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        routing_strategy: RoutingStrategy,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Alias.Args(
                name=name,
                routing_strategy=routing_strategy,
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

        routing_strategy: RoutingStrategy = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
