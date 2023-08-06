import terrascript.core as core


@core.resource(type="aws_detective_member", namespace="detective")
class Member(core.Resource):
    """
    (Required) AWS account ID for the account.
    """

    account_id: str | core.StringOut = core.attr(str)

    """
    AWS account ID for the administrator account.
    """
    administrator_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If set to true, then the root user of the invited account will _not_ receive an email not
    ification. This notification is in addition to an alert that the root user receives in AWS Personal
    Health Dashboard. By default, this is set to `false`.
    """
    disable_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    disabled_reason: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Email address for the account.
    """
    email_address: str | core.StringOut = core.attr(str)

    """
    (Required) ARN of the behavior graph to invite the member accounts to contribute their data to.
    """
    graph_arn: str | core.StringOut = core.attr(str)

    """
    Unique identifier (ID) of the Detective.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time, in UTC and extended RFC 3339 format, when an Amazon Detective membership invitation w
    as last sent to the account.
    """
    invited_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A custom message to include in the invitation. Amazon Detective adds this message to the
    standard content that it sends for an invitation.
    """
    message: str | core.StringOut | None = core.attr(str, default=None)

    """
    Current membership status of the member account.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time, in UTC and extended RFC 3339 format, of the most recent change to the member account'
    s status.
    """
    updated_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Data volume in bytes per day for the member account.
    """
    volume_usage_in_bytes: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        email_address: str | core.StringOut,
        graph_arn: str | core.StringOut,
        disable_email_notification: bool | core.BoolOut | None = None,
        message: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email_address=email_address,
                graph_arn=graph_arn,
                disable_email_notification=disable_email_notification,
                message=message,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        disable_email_notification: bool | core.BoolOut | None = core.arg(default=None)

        email_address: str | core.StringOut = core.arg()

        graph_arn: str | core.StringOut = core.arg()

        message: str | core.StringOut | None = core.arg(default=None)
