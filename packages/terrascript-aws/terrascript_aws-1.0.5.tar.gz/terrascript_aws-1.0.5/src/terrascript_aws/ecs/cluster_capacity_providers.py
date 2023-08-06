import terrascript.core as core


@core.schema
class DefaultCapacityProviderStrategy(core.Schema):

    base: int | core.IntOut | None = core.attr(int, default=None)

    capacity_provider: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        capacity_provider: str | core.StringOut,
        base: int | core.IntOut | None = None,
        weight: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DefaultCapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                base=base,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: int | core.IntOut | None = core.arg(default=None)

        capacity_provider: str | core.StringOut = core.arg()

        weight: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_ecs_cluster_capacity_providers", namespace="ecs")
class ClusterCapacityProviders(core.Resource):
    """
    (Optional) Set of names of one or more capacity providers to associate with the cluster. Valid value
    s also include `FARGATE` and `FARGATE_SPOT`.
    """

    capacity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required, Forces new resource) Name of the ECS cluster to manage capacity providers for.
    """
    cluster_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Set of capacity provider strategies to use by default for the cluster. Detailed below.
    """
    default_capacity_provider_strategy: list[DefaultCapacityProviderStrategy] | core.ArrayOut[
        DefaultCapacityProviderStrategy
    ] | None = core.attr(DefaultCapacityProviderStrategy, default=None, kind=core.Kind.array)

    """
    Same as `cluster_name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: str | core.StringOut,
        capacity_providers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        default_capacity_provider_strategy: list[DefaultCapacityProviderStrategy]
        | core.ArrayOut[DefaultCapacityProviderStrategy]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterCapacityProviders.Args(
                cluster_name=cluster_name,
                capacity_providers=capacity_providers,
                default_capacity_provider_strategy=default_capacity_provider_strategy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cluster_name: str | core.StringOut = core.arg()

        default_capacity_provider_strategy: list[DefaultCapacityProviderStrategy] | core.ArrayOut[
            DefaultCapacityProviderStrategy
        ] | None = core.arg(default=None)
