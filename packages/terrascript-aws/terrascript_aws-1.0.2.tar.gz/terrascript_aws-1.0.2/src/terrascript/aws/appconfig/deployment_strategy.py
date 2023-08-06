import terrascript.core as core


@core.resource(type="aws_appconfig_deployment_strategy", namespace="aws_appconfig")
class DeploymentStrategy(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    deployment_duration_in_minutes: int | core.IntOut = core.attr(int)

    description: str | core.StringOut | None = core.attr(str, default=None)

    final_bake_time_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    growth_factor: float | core.FloatOut = core.attr(float)

    growth_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    replicate_to: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_duration_in_minutes: int | core.IntOut,
        growth_factor: float | core.FloatOut,
        name: str | core.StringOut,
        replicate_to: str | core.StringOut,
        description: str | core.StringOut | None = None,
        final_bake_time_in_minutes: int | core.IntOut | None = None,
        growth_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeploymentStrategy.Args(
                deployment_duration_in_minutes=deployment_duration_in_minutes,
                growth_factor=growth_factor,
                name=name,
                replicate_to=replicate_to,
                description=description,
                final_bake_time_in_minutes=final_bake_time_in_minutes,
                growth_type=growth_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deployment_duration_in_minutes: int | core.IntOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        final_bake_time_in_minutes: int | core.IntOut | None = core.arg(default=None)

        growth_factor: float | core.FloatOut = core.arg()

        growth_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        replicate_to: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
