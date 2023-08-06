import terrascript.core as core


@core.resource(type="aws_macie2_invitation_accepter", namespace="macie2")
class InvitationAccepter(core.Resource):
    """
    (Required) The AWS account ID for the account that sent the invitation.
    """

    administrator_account_id: str | core.StringOut = core.attr(str)

    """
    The unique identifier (ID) of the macie invitation accepter.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The unique identifier for the invitation.
    """
    invitation_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        administrator_account_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InvitationAccepter.Args(
                administrator_account_id=administrator_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        administrator_account_id: str | core.StringOut = core.arg()
