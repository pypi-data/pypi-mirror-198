import terrascript.core as core


@core.resource(type="aws_vpc_ipam_organization_admin_account", namespace="vpc_ipam")
class OrganizationAdminAccount(core.Resource):
    """
    The Organizations ARN for the delegate account.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required)
    """
    delegated_admin_account_id: str | core.StringOut = core.attr(str)

    """
    The Organizations email for the delegate account.
    """
    email: str | core.StringOut = core.attr(str, computed=True)

    """
    The Organizations member account ID that you want to enable as the IPAM account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Organizations name for the delegate account.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS service principal.
    """
    service_principal: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        delegated_admin_account_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationAdminAccount.Args(
                delegated_admin_account_id=delegated_admin_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delegated_admin_account_id: str | core.StringOut = core.arg()
