import terrascript.core as core


@core.resource(type="aws_pinpoint_email_channel", namespace="aws_pinpoint")
class EmailChannel(core.Resource):
    """
    (Required) The application ID.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The ARN of the Amazon SES configuration set that you want to apply to messages that you s
    end through the channel.
    """
    configuration_set: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether the channel is enabled or disabled. Defaults to `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The email address used to send emails from. You can use email only (`user@example.com`) o
    r friendly address (`User <user@example.com>`). This field comply with [RFC 5322](https://www.ietf.o
    rg/rfc/rfc5322.txt).
    """
    from_address: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of an identity verified with SES.
    """
    identity: str | core.StringOut = core.attr(str)

    """
    Messages per second that can be sent.
    """
    messages_per_second: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) The ARN of an IAM Role used to submit events to Mobile Analytics' event ingestion service
    .
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        from_address: str | core.StringOut,
        identity: str | core.StringOut,
        configuration_set: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        role_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EmailChannel.Args(
                application_id=application_id,
                from_address=from_address,
                identity=identity,
                configuration_set=configuration_set,
                enabled=enabled,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        configuration_set: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        from_address: str | core.StringOut = core.arg()

        identity: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)
