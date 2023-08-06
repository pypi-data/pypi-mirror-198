import terrascript.core as core


@core.resource(type="aws_grafana_workspace_saml_configuration", namespace="grafana")
class WorkspaceSamlConfiguration(core.Resource):
    """
    (Optional) The admin role values.
    """

    admin_role_values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The allowed organizations.
    """
    allowed_organizations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The editor role values.
    """
    editor_role_values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) The email assertion.
    """
    email_assertion: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The groups assertion.
    """
    groups_assertion: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The IDP Metadata URL. Note that either `idp_metadata_url` or `idp_metadata_xml` (but not
    both) must be specified.
    """
    idp_metadata_url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IDP Metadata XML. Note that either `idp_metadata_url` or `idp_metadata_xml` (but not
    both) must be specified.
    """
    idp_metadata_xml: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The login assertion.
    """
    login_assertion: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The login validity duration.
    """
    login_validity_duration: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The name assertion.
    """
    name_assertion: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The org assertion.
    """
    org_assertion: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The role assertion.
    """
    role_assertion: str | core.StringOut | None = core.attr(str, default=None)

    """
    The status of the SAML configuration.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The workspace id.
    """
    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        editor_role_values: list[str] | core.ArrayOut[core.StringOut],
        workspace_id: str | core.StringOut,
        admin_role_values: list[str] | core.ArrayOut[core.StringOut] | None = None,
        allowed_organizations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        email_assertion: str | core.StringOut | None = None,
        groups_assertion: str | core.StringOut | None = None,
        idp_metadata_url: str | core.StringOut | None = None,
        idp_metadata_xml: str | core.StringOut | None = None,
        login_assertion: str | core.StringOut | None = None,
        login_validity_duration: int | core.IntOut | None = None,
        name_assertion: str | core.StringOut | None = None,
        org_assertion: str | core.StringOut | None = None,
        role_assertion: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=WorkspaceSamlConfiguration.Args(
                editor_role_values=editor_role_values,
                workspace_id=workspace_id,
                admin_role_values=admin_role_values,
                allowed_organizations=allowed_organizations,
                email_assertion=email_assertion,
                groups_assertion=groups_assertion,
                idp_metadata_url=idp_metadata_url,
                idp_metadata_xml=idp_metadata_xml,
                login_assertion=login_assertion,
                login_validity_duration=login_validity_duration,
                name_assertion=name_assertion,
                org_assertion=org_assertion,
                role_assertion=role_assertion,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_role_values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allowed_organizations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        editor_role_values: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        email_assertion: str | core.StringOut | None = core.arg(default=None)

        groups_assertion: str | core.StringOut | None = core.arg(default=None)

        idp_metadata_url: str | core.StringOut | None = core.arg(default=None)

        idp_metadata_xml: str | core.StringOut | None = core.arg(default=None)

        login_assertion: str | core.StringOut | None = core.arg(default=None)

        login_validity_duration: int | core.IntOut | None = core.arg(default=None)

        name_assertion: str | core.StringOut | None = core.arg(default=None)

        org_assertion: str | core.StringOut | None = core.arg(default=None)

        role_assertion: str | core.StringOut | None = core.arg(default=None)

        workspace_id: str | core.StringOut = core.arg()
