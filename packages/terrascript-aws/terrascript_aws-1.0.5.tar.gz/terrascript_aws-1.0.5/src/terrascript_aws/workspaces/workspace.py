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


@core.resource(type="aws_workspaces_workspace", namespace="workspaces")
class Workspace(core.Resource):
    """
    (Required) The ID of the bundle for the WorkSpace.
    """

    bundle_id: str | core.StringOut = core.attr(str)

    """
    The name of the WorkSpace, as seen by the operating system.
    """
    computer_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the directory for the WorkSpace.
    """
    directory_id: str | core.StringOut = core.attr(str)

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
    root_volume_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The operational state of the WorkSpace.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The tags for the WorkSpace. If configured with a provider [`default_tags` configuration b
    lock](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-b
    lock) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
