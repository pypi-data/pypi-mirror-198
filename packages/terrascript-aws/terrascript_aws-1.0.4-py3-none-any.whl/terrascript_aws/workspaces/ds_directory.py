import terrascript.core as core


@core.schema
class WorkspaceCreationProperties(core.Schema):

    custom_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    default_ou: str | core.StringOut = core.attr(str, computed=True)

    enable_internet_access: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_maintenance_mode: bool | core.BoolOut = core.attr(bool, computed=True)

    user_enabled_as_local_administrator: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        custom_security_group_id: str | core.StringOut,
        default_ou: str | core.StringOut,
        enable_internet_access: bool | core.BoolOut,
        enable_maintenance_mode: bool | core.BoolOut,
        user_enabled_as_local_administrator: bool | core.BoolOut,
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
        custom_security_group_id: str | core.StringOut = core.arg()

        default_ou: str | core.StringOut = core.arg()

        enable_internet_access: bool | core.BoolOut = core.arg()

        enable_maintenance_mode: bool | core.BoolOut = core.arg()

        user_enabled_as_local_administrator: bool | core.BoolOut = core.arg()


@core.schema
class WorkspaceAccessProperties(core.Schema):

    device_type_android: str | core.StringOut = core.attr(str, computed=True)

    device_type_chromeos: str | core.StringOut = core.attr(str, computed=True)

    device_type_ios: str | core.StringOut = core.attr(str, computed=True)

    device_type_linux: str | core.StringOut = core.attr(str, computed=True)

    device_type_osx: str | core.StringOut = core.attr(str, computed=True)

    device_type_web: str | core.StringOut = core.attr(str, computed=True)

    device_type_windows: str | core.StringOut = core.attr(str, computed=True)

    device_type_zeroclient: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_type_android: str | core.StringOut,
        device_type_chromeos: str | core.StringOut,
        device_type_ios: str | core.StringOut,
        device_type_linux: str | core.StringOut,
        device_type_osx: str | core.StringOut,
        device_type_web: str | core.StringOut,
        device_type_windows: str | core.StringOut,
        device_type_zeroclient: str | core.StringOut,
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
        device_type_android: str | core.StringOut = core.arg()

        device_type_chromeos: str | core.StringOut = core.arg()

        device_type_ios: str | core.StringOut = core.arg()

        device_type_linux: str | core.StringOut = core.arg()

        device_type_osx: str | core.StringOut = core.arg()

        device_type_web: str | core.StringOut = core.arg()

        device_type_windows: str | core.StringOut = core.arg()

        device_type_zeroclient: str | core.StringOut = core.arg()


@core.schema
class SelfServicePermissions(core.Schema):

    change_compute_type: bool | core.BoolOut = core.attr(bool, computed=True)

    increase_volume_size: bool | core.BoolOut = core.attr(bool, computed=True)

    rebuild_workspace: bool | core.BoolOut = core.attr(bool, computed=True)

    restart_workspace: bool | core.BoolOut = core.attr(bool, computed=True)

    switch_running_mode: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        change_compute_type: bool | core.BoolOut,
        increase_volume_size: bool | core.BoolOut,
        rebuild_workspace: bool | core.BoolOut,
        restart_workspace: bool | core.BoolOut,
        switch_running_mode: bool | core.BoolOut,
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
        change_compute_type: bool | core.BoolOut = core.arg()

        increase_volume_size: bool | core.BoolOut = core.arg()

        rebuild_workspace: bool | core.BoolOut = core.arg()

        restart_workspace: bool | core.BoolOut = core.arg()

        switch_running_mode: bool | core.BoolOut = core.arg()


@core.data(type="aws_workspaces_directory", namespace="workspaces")
class DsDirectory(core.Data):
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
    ip_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The registration code for the directory. This is the code that users enter in their Amazon WorkSpace
    s client application to connect to the directory.
    """
    registration_code: str | core.StringOut = core.attr(str, computed=True)

    self_service_permissions: list[SelfServicePermissions] | core.ArrayOut[
        SelfServicePermissions
    ] = core.attr(SelfServicePermissions, computed=True, kind=core.Kind.array)

    """
    The identifiers of the subnets where the directory resides.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    workspace_access_properties: list[WorkspaceAccessProperties] | core.ArrayOut[
        WorkspaceAccessProperties
    ] = core.attr(WorkspaceAccessProperties, computed=True, kind=core.Kind.array)

    workspace_creation_properties: list[WorkspaceCreationProperties] | core.ArrayOut[
        WorkspaceCreationProperties
    ] = core.attr(WorkspaceCreationProperties, computed=True, kind=core.Kind.array)

    """
    The identifier of the security group that is assigned to new WorkSpaces. Defined below.
    """
    workspace_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        directory_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDirectory.Args(
                directory_id=directory_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
