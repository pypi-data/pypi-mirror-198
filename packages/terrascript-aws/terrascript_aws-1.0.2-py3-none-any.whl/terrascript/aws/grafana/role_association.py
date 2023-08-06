import terrascript.core as core


@core.resource(type="aws_grafana_role_association", namespace="aws_grafana")
class RoleAssociation(core.Resource):

    group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    role: str | core.StringOut = core.attr(str)

    user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        role: str | core.StringOut,
        workspace_id: str | core.StringOut,
        group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        user_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoleAssociation.Args(
                role=role,
                workspace_id=workspace_id,
                group_ids=group_ids,
                user_ids=user_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        role: str | core.StringOut = core.arg()

        user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        workspace_id: str | core.StringOut = core.arg()
