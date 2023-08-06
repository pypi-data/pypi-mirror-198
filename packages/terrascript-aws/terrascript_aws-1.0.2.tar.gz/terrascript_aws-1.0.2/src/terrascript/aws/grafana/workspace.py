import terrascript.core as core


@core.resource(type="aws_grafana_workspace", namespace="aws_grafana")
class Workspace(core.Resource):

    account_access_type: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    data_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    grafana_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    notification_destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    organization_role_name: str | core.StringOut | None = core.attr(str, default=None)

    organizational_units: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    permission_type: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    saml_configuration_status: str | core.StringOut = core.attr(str, computed=True)

    stack_set_name: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        account_access_type: str | core.StringOut,
        authentication_providers: list[str] | core.ArrayOut[core.StringOut],
        permission_type: str | core.StringOut,
        data_sources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        notification_destinations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        organization_role_name: str | core.StringOut | None = None,
        organizational_units: list[str] | core.ArrayOut[core.StringOut] | None = None,
        role_arn: str | core.StringOut | None = None,
        stack_set_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workspace.Args(
                account_access_type=account_access_type,
                authentication_providers=authentication_providers,
                permission_type=permission_type,
                data_sources=data_sources,
                description=description,
                name=name,
                notification_destinations=notification_destinations,
                organization_role_name=organization_role_name,
                organizational_units=organizational_units,
                role_arn=role_arn,
                stack_set_name=stack_set_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_access_type: str | core.StringOut = core.arg()

        authentication_providers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        data_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        notification_destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        organization_role_name: str | core.StringOut | None = core.arg(default=None)

        organizational_units: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        permission_type: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        stack_set_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
