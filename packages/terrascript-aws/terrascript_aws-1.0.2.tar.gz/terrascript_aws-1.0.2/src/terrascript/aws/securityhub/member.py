import terrascript.core as core


@core.resource(type="aws_securityhub_member", namespace="aws_securityhub")
class Member(core.Resource):
    """
    (Required) The ID of the member AWS account.
    """

    account_id: str | core.StringOut = core.attr(str)

    """
    (Required) The email of the member AWS account.
    """
    email: str | core.StringOut = core.attr(str)

    """
    The ID of the member AWS account (matches `account_id`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
    """
    invite: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The ID of the master Security Hub AWS account.
    """
    master_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the member account relationship.
    """
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
