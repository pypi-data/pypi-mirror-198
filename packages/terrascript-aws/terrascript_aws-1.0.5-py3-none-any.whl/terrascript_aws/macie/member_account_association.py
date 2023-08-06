import terrascript.core as core


@core.resource(type="aws_macie_member_account_association", namespace="macie")
class MemberAccountAssociation(core.Resource):
    """
    The ID of the association.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the AWS account that you want to associate with Amazon Macie as a member accoun
    t.
    """
    member_account_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        member_account_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MemberAccountAssociation.Args(
                member_account_id=member_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        member_account_id: str | core.StringOut = core.arg()
