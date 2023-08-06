import terrascript.core as core


@core.schema
class WorkspaceProperties(core.Schema):

    compute_type_name: str | core.StringOut = core.attr(str, computed=True)

    root_volume_size_gib: int | core.IntOut = core.attr(int, computed=True)

    running_mode: str | core.StringOut = core.attr(str, computed=True)

    running_mode_auto_stop_timeout_in_minutes: int | core.IntOut = core.attr(int, computed=True)

    user_volume_size_gib: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        compute_type_name: str | core.StringOut,
        root_volume_size_gib: int | core.IntOut,
        running_mode: str | core.StringOut,
        running_mode_auto_stop_timeout_in_minutes: int | core.IntOut,
        user_volume_size_gib: int | core.IntOut,
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
        compute_type_name: str | core.StringOut = core.arg()

        root_volume_size_gib: int | core.IntOut = core.arg()

        running_mode: str | core.StringOut = core.arg()

        running_mode_auto_stop_timeout_in_minutes: int | core.IntOut = core.arg()

        user_volume_size_gib: int | core.IntOut = core.arg()


@core.data(type="aws_workspaces_workspace", namespace="workspaces")
class DsWorkspace(core.Data):
    """
    (Optional) The ID of the bundle for the WorkSpace.
    """

    bundle_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the WorkSpace, as seen by the operating system.
    """
    computer_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the directory for the WorkSpace. You have to specify `user_name` along with `di
    rectory_id`. You cannot combine this parameter with `workspace_id`.
    """
    directory_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The workspaces ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IP address of the WorkSpace.
    """
    ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether the data stored on the root volume is encrypted.
    """
    root_volume_encryption_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The operational state of the WorkSpace.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The tags for the WorkSpace.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_volume_encryption_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    volume_encryption_key: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the WorkSpace. You cannot combine this parameter with `directory_id`.
    """
    workspace_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    workspace_properties: list[WorkspaceProperties] | core.ArrayOut[
        WorkspaceProperties
    ] = core.attr(WorkspaceProperties, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        directory_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_name: str | core.StringOut | None = None,
        workspace_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsWorkspace.Args(
                directory_id=directory_id,
                tags=tags,
                user_name=user_name,
                workspace_id=workspace_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut | None = core.arg(default=None)

        workspace_id: str | core.StringOut | None = core.arg(default=None)
