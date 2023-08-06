import terrascript.core as core


@core.resource(type="aws_autoscaling_schedule", namespace="autoscaling")
class Schedule(core.Resource):
    """
    The ARN assigned by AWS to the autoscaling schedule.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name or Amazon Resource Name (ARN) of the Auto Scaling group.
    """
    autoscaling_group_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if
    you don't want to change the desired capacity at the scheduled time.
    """
    desired_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for ex
    ample, 2014-06-01T00:00:00Z ).
    """
    end_time: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The maximum size for the Auto Scaling group. Default 0.
    """
    max_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The minimum size for the Auto Scaling group. Default 0.
    """
    min_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The time when recurring future actions will start. Start time is specified by the user fo
    llowing the Unix cron syntax format.
    """
    recurrence: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name of this scaling action.
    """
    scheduled_action_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for
    example, 2014-06-01T00:00:00Z ).
    """
    start_time: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional)  The timezone for the cron expression. Valid values are the canonical names of the IANA t
    ime zones (such as Etc/GMT+9 or Pacific/Tahiti).
    """
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
