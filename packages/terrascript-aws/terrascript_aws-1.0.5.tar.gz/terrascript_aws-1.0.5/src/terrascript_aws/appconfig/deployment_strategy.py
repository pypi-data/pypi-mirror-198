import terrascript.core as core


@core.resource(type="aws_appconfig_deployment_strategy", namespace="appconfig")
class DeploymentStrategy(core.Resource):
    """
    The Amazon Resource Name (ARN) of the AppConfig Deployment Strategy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Total amount of time for a deployment to last. Minimum value of 0, maximum value of 1440.
    """
    deployment_duration_in_minutes: int | core.IntOut = core.attr(int)

    """
    (Optional) A description of the deployment strategy. Can be at most 1024 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The amount of time AWS AppConfig monitors for alarms before considering the deployment to
    be complete and no longer eligible for automatic roll back. Minimum value of 0, maximum value of 14
    40.
    """
    final_bake_time_in_minutes: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The percentage of targets to receive a deployed configuration during each interval. Minim
    um value of 1.0, maximum value of 100.0.
    """
    growth_factor: float | core.FloatOut = core.attr(float)

    """
    (Optional) The algorithm used to define how percentage grows over time. Valid value: `LINEAR` and `E
    XPONENTIAL`. Defaults to `LINEAR`.
    """
    growth_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The AppConfig deployment strategy ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) A name for the deployment strategy. Must be between 1 and 64 charact
    ers in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) Where to save the deployment strategy. Valid values: `NONE` and `SSM
    _DOCUMENT`.
    """
    replicate_to: str | core.StringOut = core.attr(str)

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
