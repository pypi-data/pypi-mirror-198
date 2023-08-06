import terrascript.core as core


@core.resource(type="aws_servicecatalog_organizations_access", namespace="servicecatalog")
class OrganizationsAccess(core.Resource):
    """
    (Required) Whether to enable AWS Organizations access.
    """

    enabled: bool | core.BoolOut = core.attr(bool)

    """
    Account ID for the account using the resource.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        enabled: bool | core.BoolOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationsAccess.Args(
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: bool | core.BoolOut = core.arg()
