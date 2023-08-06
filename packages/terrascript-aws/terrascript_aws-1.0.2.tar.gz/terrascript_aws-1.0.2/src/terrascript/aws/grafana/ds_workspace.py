import terrascript.core as core


@core.data(type="aws_grafana_workspace", namespace="aws_grafana")
class DsWorkspace(core.Data):

    account_access_type: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    created_date: str | core.StringOut = core.attr(str, computed=True)

    data_sources: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    grafana_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    notification_destinations: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    organization_role_name: str | core.StringOut = core.attr(str, computed=True)

    organizational_units: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    permission_type: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    saml_configuration_status: str | core.StringOut = core.attr(str, computed=True)

    stack_set_name: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
