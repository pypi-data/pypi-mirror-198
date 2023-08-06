import terrascript.core as core


@core.resource(type="aws_macie2_organization_admin_account", namespace="macie2")
class OrganizationAdminAccount(core.Resource):
    """
    (Required) The AWS account ID for the account to designate as the delegated Amazon Macie administrat
    or account for the organization.
    """

    admin_account_id: str | core.StringOut = core.attr(str)

    """
    The unique identifier (ID) of the macie organization admin account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        admin_account_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationAdminAccount.Args(
                admin_account_id=admin_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_account_id: str | core.StringOut = core.arg()
