import terrascript.core as core


@core.schema
class SelfServicePermissions(core.Schema):

    change_compute_type: bool | core.BoolOut | None = core.attr(bool, default=None)

    increase_volume_size: bool | core.BoolOut | None = core.attr(bool, default=None)

    rebuild_workspace: bool | core.BoolOut | None = core.attr(bool, default=None)

    restart_workspace: bool | core.BoolOut | None = core.attr(bool, default=None)

    switch_running_mode: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        change_compute_type: bool | core.BoolOut | None = None,
        increase_volume_size: bool | core.BoolOut | None = None,
        rebuild_workspace: bool | core.BoolOut | None = None,
        restart_workspace: bool | core.BoolOut | None = None,
        switch_running_mode: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=SelfServicePermissions.Args(
                change_compute_type=change_compute_type,
                increase_volume_size=increase_volume_size,
                rebuild_workspace=rebuild_workspace,
                restart_workspace=restart_workspace,
                switch_running_mode=switch_running_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        change_compute_type: bool | core.BoolOut | None = core.arg(default=None)

        increase_volume_size: bool | core.BoolOut | None = core.arg(default=None)

        rebuild_workspace: bool | core.BoolOut | None = core.arg(default=None)

        restart_workspace: bool | core.BoolOut | None = core.arg(default=None)

        switch_running_mode: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class WorkspaceCreationProperties(core.Schema):

    custom_security_group_id: str | core.StringOut | None = core.attr(str, default=None)

    default_ou: str | core.StringOut | None = core.attr(str, default=None)

    enable_internet_access: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_maintenance_mode: bool | core.BoolOut | None = core.attr(bool, default=None)

    user_enabled_as_local_administrator: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        custom_security_group_id: str | core.StringOut | None = None,
        default_ou: str | core.StringOut | None = None,
        enable_internet_access: bool | core.BoolOut | None = None,
        enable_maintenance_mode: bool | core.BoolOut | None = None,
        user_enabled_as_local_administrator: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=WorkspaceCreationProperties.Args(
                custom_security_group_id=custom_security_group_id,
                default_ou=default_ou,
                enable_internet_access=enable_internet_access,
                enable_maintenance_mode=enable_maintenance_mode,
                user_enabled_as_local_administrator=user_enabled_as_local_administrator,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_security_group_id: str | core.StringOut | None = core.arg(default=None)

        default_ou: str | core.StringOut | None = core.arg(default=None)

        enable_internet_access: bool | core.BoolOut | None = core.arg(default=None)

        enable_maintenance_mode: bool | core.BoolOut | None = core.arg(default=None)

        user_enabled_as_local_administrator: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class WorkspaceAccessProperties(core.Schema):

    device_type_android: str | core.StringOut | None = core.attr(str, default=None)

    device_type_chromeos: str | core.StringOut | None = core.attr(str, default=None)

    device_type_ios: str | core.StringOut | None = core.attr(str, default=None)

    device_type_linux: str | core.StringOut | None = core.attr(str, default=None)

    device_type_osx: str | core.StringOut | None = core.attr(str, default=None)

    device_type_web: str | core.StringOut | None = core.attr(str, default=None)

    device_type_windows: str | core.StringOut | None = core.attr(str, default=None)

    device_type_zeroclient: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_type_android: str | core.StringOut | None = None,
        device_type_chromeos: str | core.StringOut | None = None,
        device_type_ios: str | core.StringOut | None = None,
        device_type_linux: str | core.StringOut | None = None,
        device_type_osx: str | core.StringOut | None = None,
        device_type_web: str | core.StringOut | None = None,
        device_type_windows: str | core.StringOut | None = None,
        device_type_zeroclient: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=WorkspaceAccessProperties.Args(
                device_type_android=device_type_android,
                device_type_chromeos=device_type_chromeos,
                device_type_ios=device_type_ios,
                device_type_linux=device_type_linux,
                device_type_osx=device_type_osx,
                device_type_web=device_type_web,
                device_type_windows=device_type_windows,
                device_type_zeroclient=device_type_zeroclient,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_type_android: str | core.StringOut | None = core.arg(default=None)

        device_type_chromeos: str | core.StringOut | None = core.arg(default=None)

        device_type_ios: str | core.StringOut | None = core.arg(default=None)

        device_type_linux: str | core.StringOut | None = core.arg(default=None)

        device_type_osx: str | core.StringOut | None = core.arg(default=None)

        device_type_web: str | core.StringOut | None = core.arg(default=None)

        device_type_windows: str | core.StringOut | None = core.arg(default=None)

        device_type_zeroclient: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_workspaces_directory", namespace="workspaces")
class Directory(core.Resource):
    """
    The directory alias.
    """

    alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The user name for the service account.
    """
    customer_user_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The directory identifier for registration in WorkSpaces service.
    """
    directory_id: str | core.StringOut = core.attr(str)

    """
    The name of the directory.
    """
    directory_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The directory type.
    """
    directory_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The IP addresses of the DNS servers for the directory.
    """
    dns_ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to othe
    r services, such as Amazon EC2, on your behalf.
    """
    iam_role_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The WorkSpaces directory identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifiers of the IP access control groups associated with the directory.
    """
    ip_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The registration code for the directory. This is the code that users enter in their Amazon WorkSpace
    s client application to connect to the directory.
    """
    registration_code: str | core.StringOut = core.attr(str, computed=True)

    self_service_permissions: SelfServicePermissions | None = core.attr(
        SelfServicePermissions, default=None, computed=True
    )

    """
    (Optional) The identifiers of the subnets where the directory resides.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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

    workspace_access_properties: WorkspaceAccessProperties | None = core.attr(
        WorkspaceAccessProperties, default=None, computed=True
    )

    workspace_creation_properties: WorkspaceCreationProperties | None = core.attr(
        WorkspaceCreationProperties, default=None, computed=True
    )

    """
    The identifier of the security group that is assigned to new WorkSpaces.
    """
    workspace_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: str | core.StringOut,
        ip_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_service_permissions: SelfServicePermissions | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        workspace_access_properties: WorkspaceAccessProperties | None = None,
        workspace_creation_properties: WorkspaceCreationProperties | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Directory.Args(
                directory_id=directory_id,
                ip_group_ids=ip_group_ids,
                self_service_permissions=self_service_permissions,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                workspace_access_properties=workspace_access_properties,
                workspace_creation_properties=workspace_creation_properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: str | core.StringOut = core.arg()

        ip_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        self_service_permissions: SelfServicePermissions | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        workspace_access_properties: WorkspaceAccessProperties | None = core.arg(default=None)

        workspace_creation_properties: WorkspaceCreationProperties | None = core.arg(default=None)
