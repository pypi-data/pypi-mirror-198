import terrascript.core as core


@core.resource(type="aws_sns_platform_application", namespace="sns")
class PlatformApplication(core.Resource):
    """
    The ARN of the SNS platform application
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN of the SNS Topic triggered when a delivery to any of the platform endpoints assoc
    iated with your platform application encounters a permanent failure.
    """
    event_delivery_failure_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the SNS Topic triggered when a new platform endpoint is added to your platform
    application.
    """
    event_endpoint_created_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the SNS Topic triggered when an existing platform endpoint is deleted from you
    r platform application.
    """
    event_endpoint_deleted_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARN of the SNS Topic triggered when an existing platform endpoint is changed from you
    r platform application.
    """
    event_endpoint_updated_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM role ARN permitted to receive failure feedback for this application and give SNS
    write access to use CloudWatch logs on your behalf.
    """
    failure_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the SNS platform application
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly name for the SNS platform application
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The platform that the app is registered with. See [Platform][1] for supported platforms.
    """
    platform: str | core.StringOut = core.attr(str)

    """
    (Required) Application Platform credential. See [Credential][1] for type of credential required for
    platform. The value of this attribute when stored into the Terraform state is only a hash of the rea
    l value, so therefore it is not practical to use this as an attribute for other resources.
    """
    platform_credential: str | core.StringOut = core.attr(str)

    """
    (Optional) Application Platform principal. See [Principal][2] for type of principal required for pla
    tform. The value of this attribute when stored into the Terraform state is only a hash of the real v
    alue, so therefore it is not practical to use this as an attribute for other resources.
    """
    platform_principal: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IAM role ARN permitted to receive success feedback for this application and give SNS
    write access to use CloudWatch logs on your behalf.
    """
    success_feedback_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The sample rate percentage (0-100) of successfully delivered messages.
    """
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
