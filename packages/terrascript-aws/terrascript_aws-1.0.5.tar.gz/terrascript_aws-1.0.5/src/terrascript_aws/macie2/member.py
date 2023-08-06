import terrascript.core as core


@core.resource(type="aws_macie2_member", namespace="macie2")
class Member(core.Resource):
    """
    (Required) The AWS account ID for the account.
    """

    account_id: str | core.StringOut = core.attr(str)

    """
    The AWS account ID for the administrator account.
    """
    administrator_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the account.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The email address for the account.
    """
    email: str | core.StringOut = core.attr(str)

    """
    The unique identifier (ID) of the macie Member.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether to send an email notification to the root user of each account that the
    invitation will be sent to. This notification is in addition to an alert that the root user receive
    s in AWS Personal Health Dashboard. To send an email notification to the root user of each account,
    set this value to `true`.
    """
    invitation_disable_email_notification: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Optional) A custom message to include in the invitation. Amazon Macie adds this message to the stan
    dard content that it sends for an invitation.
    """
    invitation_message: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Send an invitation to a member
    """
    invite: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The date and time, in UTC and extended RFC 3339 format, when an Amazon Macie membership invitation w
    as last sent to the account. This value is null if a Macie invitation hasn't been sent to the accoun
    t.
    """
    invited_at: str | core.StringOut = core.attr(str, computed=True)

    master_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The current status of the relationship between the account and the administrator account.
    """
    relationship_status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the status for the account. To enable Amazon Macie and start all Macie activiti
    es for the account, set this value to `ENABLED`. Valid values are `ENABLED` or `PAUSED`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of key-value pairs that specifies the tags to associate with the account in Amazon
    Macie.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The date and time, in UTC and extended RFC 3339 format, of the most recent change to the status of t
    he relationship between the account and the administrator account.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        email: str | core.StringOut,
        invitation_disable_email_notification: bool | core.BoolOut | None = None,
        invitation_message: str | core.StringOut | None = None,
        invite: bool | core.BoolOut | None = None,
        status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email=email,
                invitation_disable_email_notification=invitation_disable_email_notification,
                invitation_message=invitation_message,
                invite=invite,
                status=status,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        email: str | core.StringOut = core.arg()

        invitation_disable_email_notification: bool | core.BoolOut | None = core.arg(default=None)

        invitation_message: str | core.StringOut | None = core.arg(default=None)

        invite: bool | core.BoolOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
