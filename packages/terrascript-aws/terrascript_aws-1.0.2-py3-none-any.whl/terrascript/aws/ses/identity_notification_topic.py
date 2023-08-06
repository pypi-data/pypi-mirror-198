import terrascript.core as core


@core.resource(type="aws_ses_identity_notification_topic", namespace="aws_ses")
class IdentityNotificationTopic(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identity for which the Amazon SNS topic will be set. You can specify an identity by u
    sing its name or by using its Amazon Resource Name (ARN).
    """
    identity: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether SES should include original email headers in SNS notifications of this type. `fal
    se` by default.
    """
    include_original_headers: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The type of notifications that will be published to the specified Amazon SNS topic. Valid
    Values: `Bounce`, `Complaint` or `Delivery`.
    """
    notification_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The Amazon Resource Name (ARN) of the Amazon SNS topic. Can be set to `""` (an empty stri
    ng) to disable publishing.
    """
    topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        identity: str | core.StringOut,
        notification_type: str | core.StringOut,
        include_original_headers: bool | core.BoolOut | None = None,
        topic_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityNotificationTopic.Args(
                identity=identity,
                notification_type=notification_type,
                include_original_headers=include_original_headers,
                topic_arn=topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity: str | core.StringOut = core.arg()

        include_original_headers: bool | core.BoolOut | None = core.arg(default=None)

        notification_type: str | core.StringOut = core.arg()

        topic_arn: str | core.StringOut | None = core.arg(default=None)
