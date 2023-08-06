import terrascript.core as core


@core.data(type="aws_grafana_workspace", namespace="grafana")
class DsWorkspace(core.Data):
    """
    (Required) The type of account access for the workspace. Valid values are `CURRENT_ACCOUNT` and `ORG
    ANIZATION`. If `ORGANIZATION` is specified, then `organizational_units` must also be present.
    """

    account_access_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the Grafana workspace.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The authentication providers for the workspace. Valid values are `AWS_SSO`, `SAML`, or bo
    th.
    """
    authentication_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The creation date of the Grafana workspace.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The data sources for the workspace.
    """
    data_sources: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The workspace description.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The endpoint of the Grafana workspace.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The version of Grafana running on the workspace.
    """
    grafana_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last updated date of the Grafana workspace.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The Grafana workspace name.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    The notification destinations.
    """
    notification_destinations: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The role name that the workspace uses to access resources through Amazon Organizations.
    """
    organization_role_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Organizations organizational units that the workspace is authorized to use data sources f
    rom.
    """
    organizational_units: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The permission type of the workspace.
    """
    permission_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The IAM role ARN that the workspace assumes.
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    saml_configuration_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS CloudFormation stack set name that provisions IAM roles to be used by the workspace.
    """
    stack_set_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of the Grafana workspace.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The tags assigned to the resource
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The Grafana workspace ID.
    """
    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        workspace_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsWorkspace.Args(
                workspace_id=workspace_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        workspace_id: str | core.StringOut = core.arg()
