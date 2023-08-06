import terrascript.core as core


@core.resource(type="aws_guardduty_member", namespace="aws_guardduty")
class Member(core.Resource):

    account_id: str | core.StringOut = core.attr(str)

    detector_id: str | core.StringOut = core.attr(str)

    disable_email_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    email: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    invitation_message: str | core.StringOut | None = core.attr(str, default=None)

    invite: bool | core.BoolOut | None = core.attr(bool, default=None)

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
