import terrascript.core as core


@core.schema
class ManagedScaling(core.Schema):

    instance_warmup_period: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    maximum_scaling_step_size: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    minimum_scaling_step_size: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    target_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        instance_warmup_period: int | core.IntOut | None = None,
        maximum_scaling_step_size: int | core.IntOut | None = None,
        minimum_scaling_step_size: int | core.IntOut | None = None,
        status: str | core.StringOut | None = None,
        target_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ManagedScaling.Args(
                instance_warmup_period=instance_warmup_period,
                maximum_scaling_step_size=maximum_scaling_step_size,
                minimum_scaling_step_size=minimum_scaling_step_size,
                status=status,
                target_capacity=target_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_warmup_period: int | core.IntOut | None = core.arg(default=None)

        maximum_scaling_step_size: int | core.IntOut | None = core.arg(default=None)

        minimum_scaling_step_size: int | core.IntOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        target_capacity: int | core.IntOut | None = core.arg(default=None)


@core.schema
class AutoScalingGroupProvider(core.Schema):

    auto_scaling_group_arn: str | core.StringOut = core.attr(str)

    managed_scaling: ManagedScaling | None = core.attr(ManagedScaling, default=None, computed=True)

    managed_termination_protection: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        auto_scaling_group_arn: str | core.StringOut,
        managed_scaling: ManagedScaling | None = None,
        managed_termination_protection: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AutoScalingGroupProvider.Args(
                auto_scaling_group_arn=auto_scaling_group_arn,
                managed_scaling=managed_scaling,
                managed_termination_protection=managed_termination_protection,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_scaling_group_arn: str | core.StringOut = core.arg()

        managed_scaling: ManagedScaling | None = core.arg(default=None)

        managed_termination_protection: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ecs_capacity_provider", namespace="aws_ecs")
class CapacityProvider(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_scaling_group_provider: AutoScalingGroupProvider = core.attr(AutoScalingGroupProvider)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

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
        auto_scaling_group_provider: AutoScalingGroupProvider,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CapacityProvider.Args(
                auto_scaling_group_provider=auto_scaling_group_provider,
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
        auto_scaling_group_provider: AutoScalingGroupProvider = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
