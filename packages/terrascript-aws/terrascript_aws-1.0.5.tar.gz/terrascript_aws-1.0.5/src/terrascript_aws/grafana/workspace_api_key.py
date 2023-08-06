import terrascript.core as core


@core.resource(type="aws_grafana_workspace_api_key", namespace="grafana")
class WorkspaceApiKey(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The key token in JSON format. Use this value as a bearer token to authenticate HTTP requests to the
    workspace.
    """
    key: str | core.StringOut = core.attr(str, computed=True)

    key_name: str | core.StringOut = core.attr(str)

    key_role: str | core.StringOut = core.attr(str)

    seconds_to_live: int | core.IntOut = core.attr(int)

    workspace_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key_name: str | core.StringOut,
        key_role: str | core.StringOut,
        seconds_to_live: int | core.IntOut,
        workspace_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=WorkspaceApiKey.Args(
                key_name=key_name,
                key_role=key_role,
                seconds_to_live=seconds_to_live,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_name: str | core.StringOut = core.arg()

        key_role: str | core.StringOut = core.arg()

        seconds_to_live: int | core.IntOut = core.arg()

        workspace_id: str | core.StringOut = core.arg()
