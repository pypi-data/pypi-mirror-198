import terrascript.core as core


@core.resource(type="aws_autoscaling_lifecycle_hook", namespace="autoscaling")
class LifecycleHook(core.Resource):
    """
    (Required) The name of the Auto Scaling group to which you want to assign the lifecycle hook
    """

    autoscaling_group_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Defines the action the Auto Scaling group should take when the lifecycle hook timeout ela
    pses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABAN
    DON. The default value for this parameter is ABANDON.
    """
    default_result: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Defines the amount of time, in seconds, that can elapse before the lifecycle hook times o
    ut. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult
    parameter
    """
    heartbeat_timeout: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The instance state to which you want to attach the lifecycle hook. For a list of lifecycl
    e hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/a
    utoscaling/describe-lifecycle-hook-types.html#examples)
    """
    lifecycle_transition: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the lifecycle hook.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Contains additional information that you want to include any time Auto Scaling sends a me
    ssage to the notification target.
    """
    notification_metadata: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the notification target that Auto Scaling will use to notify you when an insta
    nce is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or
    an SNS topic.
    """
    notification_target_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the IAM role that allows the Auto Scaling group to publish to the specified no
    tification target.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: str | core.StringOut,
        lifecycle_transition: str | core.StringOut,
        name: str | core.StringOut,
        default_result: str | core.StringOut | None = None,
        heartbeat_timeout: int | core.IntOut | None = None,
        notification_metadata: str | core.StringOut | None = None,
        notification_target_arn: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LifecycleHook.Args(
                autoscaling_group_name=autoscaling_group_name,
                lifecycle_transition=lifecycle_transition,
                name=name,
                default_result=default_result,
                heartbeat_timeout=heartbeat_timeout,
                notification_metadata=notification_metadata,
                notification_target_arn=notification_target_arn,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_group_name: str | core.StringOut = core.arg()

        default_result: str | core.StringOut | None = core.arg(default=None)

        heartbeat_timeout: int | core.IntOut | None = core.arg(default=None)

        lifecycle_transition: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        notification_metadata: str | core.StringOut | None = core.arg(default=None)

        notification_target_arn: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)
