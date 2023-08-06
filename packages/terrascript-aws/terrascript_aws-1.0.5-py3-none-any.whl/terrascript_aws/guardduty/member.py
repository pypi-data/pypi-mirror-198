import terrascript.core as core


@core.resource(type="aws_guardduty_member", namespace="guardduty")
class Member(core.Resource):
    """
    (Required) AWS account ID for member account.
    """

    account_id: str | core.StringOut = core.attr(str)

    """
    (Required) The detector ID of the GuardDuty account where you want to create member accounts.
    """
    detector_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Boolean whether an email notification is sent to the accounts. Defaults to `false`.
    """
    disable_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Email address for member account.
    """
    email: str | core.StringOut = core.attr(str)

    """
    The ID of the GuardDuty member
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Message for invitation.
    """
    invitation_message: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To d
    etect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relati
    onship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.
    """
    invite: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The status of the relationship between the member account and its primary account. More information
    can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get
    members.html).
    """
    relationship_status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        detector_id: str | core.StringOut,
        email: str | core.StringOut,
        disable_email_notification: bool | core.BoolOut | None = None,
        invitation_message: str | core.StringOut | None = None,
        invite: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                detector_id=detector_id,
                email=email,
                disable_email_notification=disable_email_notification,
                invitation_message=invitation_message,
                invite=invite,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        detector_id: str | core.StringOut = core.arg()

        disable_email_notification: bool | core.BoolOut | None = core.arg(default=None)

        email: str | core.StringOut = core.arg()

        invitation_message: str | core.StringOut | None = core.arg(default=None)

        invite: bool | core.BoolOut | None = core.arg(default=None)
