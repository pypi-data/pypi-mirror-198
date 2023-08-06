import terrascript.core as core


@core.resource(type="aws_autoscaling_lifecycle_hook", namespace="aws_autoscaling")
class LifecycleHook(core.Resource):

    autoscaling_group_name: str | core.StringOut = core.attr(str)

    default_result: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    heartbeat_timeout: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    lifecycle_transition: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    notification_metadata: str | core.StringOut | None = core.attr(str, default=None)

    notification_target_arn: str | core.StringOut | None = core.attr(str, default=None)

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
