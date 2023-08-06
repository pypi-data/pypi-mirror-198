import terrascript.core as core


@core.schema
class WorkspaceProperties(core.Schema):

    compute_type_name: str | core.StringOut | None = core.attr(str, default=None)

    root_volume_size_gib: int | core.IntOut | None = core.attr(int, default=None)

    running_mode: str | core.StringOut | None = core.attr(str, default=None)

    running_mode_auto_stop_timeout_in_minutes: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    user_volume_size_gib: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        compute_type_name: str | core.StringOut | None = None,
        root_volume_size_gib: int | core.IntOut | None = None,
        running_mode: str | core.StringOut | None = None,
        running_mode_auto_stop_timeout_in_minutes: int | core.IntOut | None = None,
        user_volume_size_gib: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=WorkspaceProperties.Args(
                compute_type_name=compute_type_name,
                root_volume_size_gib=root_volume_size_gib,
                running_mode=running_mode,
                running_mode_auto_stop_timeout_in_minutes=running_mode_auto_stop_timeout_in_minutes,
                user_volume_size_gib=user_volume_size_gib,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_type_name: str | core.StringOut | None = core.arg(default=None)

        root_volume_size_gib: int | core.IntOut | None = core.arg(default=None)

        running_mode: str | core.StringOut | None = core.arg(default=None)

        running_mode_auto_stop_timeout_in_minutes: int | core.IntOut | None = core.arg(default=None)

        user_volume_size_gib: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_workspaces_workspace", namespace="aws_workspaces")
class Workspace(core.Resource):

    bundle_id: str | core.StringOut = core.attr(str)

    computer_name: str | core.StringOut = core.attr(str, computed=True)

    directory_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: str | core.StringOut = core.attr(str, computed=True)

    root_volume_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    state: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: str | core.StringOut = core.attr(str)

    user_volume_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    volume_encryption_key: str | core.StringOut | None = core.attr(str, default=None)

    workspace_properties: WorkspaceProperties | None = core.attr(
        WorkspaceProperties, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bundle_id: str | core.StringOut,
        directory_id: str | core.StringOut,
        user_name: str | core.StringOut,
        root_volume_encryption_enabled: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_volume_encryption_enabled: bool | core.BoolOut | None = None,
        volume_encryption_key: str | core.StringOut | None = None,
        workspace_properties: WorkspaceProperties | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workspace.Args(
                bundle_id=bundle_id,
                directory_id=directory_id,
                user_name=user_name,
                root_volume_encryption_enabled=root_volume_encryption_enabled,
                tags=tags,
                tags_all=tags_all,
                user_volume_encryption_enabled=user_volume_encryption_enabled,
                volume_encryption_key=volume_encryption_key,
                workspace_properties=workspace_properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bundle_id: str | core.StringOut = core.arg()

        directory_id: str | core.StringOut = core.arg()

        root_volume_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()

        user_volume_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        volume_encryption_key: str | core.StringOut | None = core.arg(default=None)

        workspace_properties: WorkspaceProperties | None = core.arg(default=None)
