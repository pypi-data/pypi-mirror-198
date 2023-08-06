import terrascript.core as core


@core.resource(type="aws_autoscaling_schedule", namespace="aws_autoscaling")
class Schedule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    autoscaling_group_name: str | core.StringOut = core.attr(str)

    desired_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    end_time: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    max_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    min_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    recurrence: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    scheduled_action_name: str | core.StringOut = core.attr(str)

    start_time: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    time_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: str | core.StringOut,
        scheduled_action_name: str | core.StringOut,
        desired_capacity: int | core.IntOut | None = None,
        end_time: str | core.StringOut | None = None,
        max_size: int | core.IntOut | None = None,
        min_size: int | core.IntOut | None = None,
        recurrence: str | core.StringOut | None = None,
        start_time: str | core.StringOut | None = None,
        time_zone: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Schedule.Args(
                autoscaling_group_name=autoscaling_group_name,
                scheduled_action_name=scheduled_action_name,
                desired_capacity=desired_capacity,
                end_time=end_time,
                max_size=max_size,
                min_size=min_size,
                recurrence=recurrence,
                start_time=start_time,
                time_zone=time_zone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_group_name: str | core.StringOut = core.arg()

        desired_capacity: int | core.IntOut | None = core.arg(default=None)

        end_time: str | core.StringOut | None = core.arg(default=None)

        max_size: int | core.IntOut | None = core.arg(default=None)

        min_size: int | core.IntOut | None = core.arg(default=None)

        recurrence: str | core.StringOut | None = core.arg(default=None)

        scheduled_action_name: str | core.StringOut = core.arg()

        start_time: str | core.StringOut | None = core.arg(default=None)

        time_zone: str | core.StringOut | None = core.arg(default=None)
