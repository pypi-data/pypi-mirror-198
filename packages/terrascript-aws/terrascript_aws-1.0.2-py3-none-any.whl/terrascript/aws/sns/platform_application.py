import terrascript.core as core


@core.resource(type="aws_sns_platform_application", namespace="aws_sns")
class PlatformApplication(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    event_delivery_failure_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    event_endpoint_created_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    event_endpoint_deleted_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    event_endpoint_updated_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    platform: str | core.StringOut = core.attr(str)

    platform_credential: str | core.StringOut = core.attr(str)

    platform_principal: str | core.StringOut | None = core.attr(str, default=None)

    success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    success_feedback_sample_rate: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        platform: str | core.StringOut,
        platform_credential: str | core.StringOut,
        event_delivery_failure_topic_arn: str | core.StringOut | None = None,
        event_endpoint_created_topic_arn: str | core.StringOut | None = None,
        event_endpoint_deleted_topic_arn: str | core.StringOut | None = None,
        event_endpoint_updated_topic_arn: str | core.StringOut | None = None,
        failure_feedback_role_arn: str | core.StringOut | None = None,
        platform_principal: str | core.StringOut | None = None,
        success_feedback_role_arn: str | core.StringOut | None = None,
        success_feedback_sample_rate: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PlatformApplication.Args(
                name=name,
                platform=platform,
                platform_credential=platform_credential,
                event_delivery_failure_topic_arn=event_delivery_failure_topic_arn,
                event_endpoint_created_topic_arn=event_endpoint_created_topic_arn,
                event_endpoint_deleted_topic_arn=event_endpoint_deleted_topic_arn,
                event_endpoint_updated_topic_arn=event_endpoint_updated_topic_arn,
                failure_feedback_role_arn=failure_feedback_role_arn,
                platform_principal=platform_principal,
                success_feedback_role_arn=success_feedback_role_arn,
                success_feedback_sample_rate=success_feedback_sample_rate,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        event_delivery_failure_topic_arn: str | core.StringOut | None = core.arg(default=None)

        event_endpoint_created_topic_arn: str | core.StringOut | None = core.arg(default=None)

        event_endpoint_deleted_topic_arn: str | core.StringOut | None = core.arg(default=None)

        event_endpoint_updated_topic_arn: str | core.StringOut | None = core.arg(default=None)

        failure_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        platform: str | core.StringOut = core.arg()

        platform_credential: str | core.StringOut = core.arg()

        platform_principal: str | core.StringOut | None = core.arg(default=None)

        success_feedback_role_arn: str | core.StringOut | None = core.arg(default=None)

        success_feedback_sample_rate: str | core.StringOut | None = core.arg(default=None)
