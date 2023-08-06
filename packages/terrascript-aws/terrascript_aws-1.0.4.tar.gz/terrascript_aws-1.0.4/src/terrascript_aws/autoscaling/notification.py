import terrascript.core as core


@core.resource(type="aws_autoscaling_notification", namespace="autoscaling")
class Notification(core.Resource):
    """
    (Required) A list of AutoScaling Group Names
    """

    group_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of Notification Types that trigger
    """
    notifications: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Required) The Topic ARN for notifications to be sent through
    """
    topic_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_names: list[str] | core.ArrayOut[core.StringOut],
        notifications: list[str] | core.ArrayOut[core.StringOut],
        topic_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Notification.Args(
                group_names=group_names,
                notifications=notifications,
                topic_arn=topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_names: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        notifications: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        topic_arn: str | core.StringOut = core.arg()
