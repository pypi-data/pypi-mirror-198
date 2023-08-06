import terrascript.core as core


@core.schema
class ScalableTargetAction(core.Schema):

    max_capacity: str | core.StringOut | None = core.attr(str, default=None)

    min_capacity: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_capacity: str | core.StringOut | None = None,
        min_capacity: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScalableTargetAction.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_capacity: str | core.StringOut | None = core.arg(default=None)

        min_capacity: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_appautoscaling_scheduled_action", namespace="aws_application_auto_scaling")
class AppautoscalingScheduledAction(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    end_time: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    resource_id: str | core.StringOut = core.attr(str)

    scalable_dimension: str | core.StringOut = core.attr(str)

    scalable_target_action: ScalableTargetAction = core.attr(ScalableTargetAction)

    schedule: str | core.StringOut = core.attr(str)

    service_namespace: str | core.StringOut = core.attr(str)

    start_time: str | core.StringOut | None = core.attr(str, default=None)

    timezone: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        resource_id: str | core.StringOut,
        scalable_dimension: str | core.StringOut,
        scalable_target_action: ScalableTargetAction,
        schedule: str | core.StringOut,
        service_namespace: str | core.StringOut,
        end_time: str | core.StringOut | None = None,
        start_time: str | core.StringOut | None = None,
        timezone: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppautoscalingScheduledAction.Args(
                name=name,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                scalable_target_action=scalable_target_action,
                schedule=schedule,
                service_namespace=service_namespace,
                end_time=end_time,
                start_time=start_time,
                timezone=timezone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        end_time: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()

        scalable_dimension: str | core.StringOut = core.arg()

        scalable_target_action: ScalableTargetAction = core.arg()

        schedule: str | core.StringOut = core.arg()

        service_namespace: str | core.StringOut = core.arg()

        start_time: str | core.StringOut | None = core.arg(default=None)

        timezone: str | core.StringOut | None = core.arg(default=None)
