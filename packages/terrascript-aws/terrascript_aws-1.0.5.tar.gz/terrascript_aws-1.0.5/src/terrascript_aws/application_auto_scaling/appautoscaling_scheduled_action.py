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


@core.resource(type="aws_appautoscaling_scheduled_action", namespace="application_auto_scaling")
class AppautoscalingScheduledAction(core.Resource):
    """
    The Amazon Resource Name (ARN) of the scheduled action.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The date and time for the scheduled action to end in RFC 3339 format. The timezone is not
    affected by the setting of `timezone`.
    """
    end_time: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the scheduled action.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The identifier of the resource associated with the scheduled action. Documentation can be
    found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com
    /ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutSc
    heduledAction-request-ResourceId)
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    (Required) The scalable dimension. Documentation can be found in the parameter at: [AWS Application
    Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/A
    PI_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Exam
    ple: ecs:service:DesiredCount
    """
    scalable_dimension: str | core.StringOut = core.attr(str)

    """
    (Required) The new minimum and maximum capacity. You can set both values or just one. See [below](#s
    calable-target-action-arguments)
    """
    scalable_target_action: ScalableTargetAction = core.attr(ScalableTargetAction)

    """
    (Required) The schedule for this action. The following formats are supported: At expressions - at(yy
    yy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). Times for a
    t expressions and cron expressions are evaluated using the time zone configured in `timezone`. Docum
    entation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs
    .aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAu
    toScaling-PutScheduledAction-request-Schedule)
    """
    schedule: str | core.StringOut = core.attr(str)

    """
    (Required) The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Ap
    plication Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIR
    eference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamesp
    ace) Example: ecs
    """
    service_namespace: str | core.StringOut = core.attr(str)

    """
    (Optional) The date and time for the scheduled action to start in RFC 3339 format. The timezone is n
    ot affected by the setting of `timezone`.
    """
    start_time: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The time zone used when setting a scheduled action by using an at or cron expression. Doe
    s not affect timezone for `start_time` and `end_time`. Valid values are the [canonical names of the
    IANA time zones supported by Joda-Time](https://www.joda.org/joda-time/timezones.html), such as `Etc
    /GMT+9` or `Pacific/Tahiti`. Default is `UTC`.
    """
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
