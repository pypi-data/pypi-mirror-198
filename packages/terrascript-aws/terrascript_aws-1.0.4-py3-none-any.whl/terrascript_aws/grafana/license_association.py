import terrascript.core as core


@core.resource(type="aws_grafana_license_association", namespace="grafana")
class LicenseAssociation(core.Resource):
    """
    If `license_type` is set to `ENTERPRISE_FREE_TRIAL`, this is the expiration date of the free trial.
    """

    free_trial_expiration: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    If `license_type` is set to `ENTERPRISE`, this is the expiration date of the enterprise license.
    """
    license_expiration: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The type of license for the workspace license association. Valid values are `ENTERPRISE`
    and `ENTERPRISE_FREE_TRIAL`.
    """
    license_type: str | core.StringOut = core.attr(str)

    """
    (Required) The workspace id.
    """
    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        license_type: str | core.StringOut,
        workspace_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LicenseAssociation.Args(
                license_type=license_type,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        license_type: str | core.StringOut = core.arg()

        workspace_id: str | core.StringOut = core.arg()
