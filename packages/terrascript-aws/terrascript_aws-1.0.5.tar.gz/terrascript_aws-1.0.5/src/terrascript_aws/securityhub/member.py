import terrascript.core as core


@core.resource(type="aws_securityhub_member", namespace="securityhub")
class Member(core.Resource):

    account_id: str | core.StringOut = core.attr(str)

    email: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    invite: bool | core.BoolOut | None = core.attr(bool, default=None)

    master_id: str | core.StringOut = core.attr(str, computed=True)

    member_status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut,
        email: str | core.StringOut,
        invite: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email=email,
                invite=invite,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut = core.arg()

        email: str | core.StringOut = core.arg()

        invite: bool | core.BoolOut | None = core.arg(default=None)
