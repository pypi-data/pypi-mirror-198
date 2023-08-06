import terrascript.core as core


@core.resource(type="aws_macie2_member", namespace="aws_macie2")
class Member(core.Resource):

    account_id: str | core.StringOut = core.attr(str)

    administrator_account_id: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    email: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    invitation_disable_email_notification: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    invitation_message: str | core.StringOut | None = core.attr(str, default=None)

    invite: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    invited_at: str | core.StringOut = core.attr(str, computed=True)

    master_account_id: str | core.StringOut = core.attr(str, computed=True)

    relationship_status: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
