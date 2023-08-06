import terrascript.core as core


@core.resource(type="aws_vpc_ipam_organization_admin_account", namespace="aws_vpc_ipam")
class OrganizationAdminAccount(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    delegated_admin_account_id: str | core.StringOut = core.attr(str)

    email: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

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
