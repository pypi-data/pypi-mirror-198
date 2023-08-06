import terrascript.core as core


@core.schema
class MaintenanceStartTime(core.Schema):

    day_of_month: str | core.StringOut | None = core.attr(str, default=None)

    day_of_week: str | core.StringOut | None = core.attr(str, default=None)

    hour_of_day: int | core.IntOut = core.attr(int)

    minute_of_hour: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        hour_of_day: int | core.IntOut,
        day_of_month: str | core.StringOut | None = None,
        day_of_week: str | core.StringOut | None = None,
        minute_of_hour: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=MaintenanceStartTime.Args(
                hour_of_day=hour_of_day,
                day_of_month=day_of_month,
                day_of_week=day_of_week,
                minute_of_hour=minute_of_hour,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        day_of_month: str | core.StringOut | None = core.arg(default=None)

        day_of_week: str | core.StringOut | None = core.arg(default=None)

        hour_of_day: int | core.IntOut = core.arg()

        minute_of_hour: int | core.IntOut | None = core.arg(default=None)


@core.schema
class GatewayNetworkInterface(core.Schema):

    ipv4_address: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ipv4_address: str | core.StringOut,
    ):
        super().__init__(
            args=GatewayNetworkInterface.Args(
                ipv4_address=ipv4_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ipv4_address: str | core.StringOut = core.arg()


@core.schema
class SmbActiveDirectorySettings(core.Schema):

    active_directory_status: str | core.StringOut = core.attr(str, computed=True)

    domain_controllers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    domain_name: str | core.StringOut = core.attr(str)

    organizational_unit: str | core.StringOut | None = core.attr(str, default=None)

    password: str | core.StringOut = core.attr(str)

    timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        active_directory_status: str | core.StringOut,
        domain_name: str | core.StringOut,
        password: str | core.StringOut,
        username: str | core.StringOut,
        domain_controllers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        organizational_unit: str | core.StringOut | None = None,
        timeout_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SmbActiveDirectorySettings.Args(
                active_directory_status=active_directory_status,
                domain_name=domain_name,
                password=password,
                username=username,
                domain_controllers=domain_controllers,
                organizational_unit=organizational_unit,
                timeout_in_seconds=timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_directory_status: str | core.StringOut = core.arg()

        domain_controllers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        domain_name: str | core.StringOut = core.arg()

        organizational_unit: str | core.StringOut | None = core.arg(default=None)

        password: str | core.StringOut = core.arg()

        timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)

        username: str | core.StringOut = core.arg()


@core.resource(type="aws_storagegateway_gateway", namespace="aws_storagegateway")
class Gateway(core.Resource):

    activation_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    average_download_rate_limit_in_bits_per_sec: int | core.IntOut | None = core.attr(
        int, default=None
    )

    average_upload_rate_limit_in_bits_per_sec: int | core.IntOut | None = core.attr(
        int, default=None
    )

    cloudwatch_log_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    ec2_instance_id: str | core.StringOut = core.attr(str, computed=True)

    endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    gateway_id: str | core.StringOut = core.attr(str, computed=True)

    gateway_ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    gateway_name: str | core.StringOut = core.attr(str)

    gateway_network_interface: list[GatewayNetworkInterface] | core.ArrayOut[
        GatewayNetworkInterface
    ] = core.attr(GatewayNetworkInterface, computed=True, kind=core.Kind.array)

    gateway_timezone: str | core.StringOut = core.attr(str)

    gateway_type: str | core.StringOut | None = core.attr(str, default=None)

    gateway_vpc_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    host_environment: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    maintenance_start_time: MaintenanceStartTime | None = core.attr(
        MaintenanceStartTime, default=None, computed=True
    )

    medium_changer_type: str | core.StringOut | None = core.attr(str, default=None)

    smb_active_directory_settings: SmbActiveDirectorySettings | None = core.attr(
        SmbActiveDirectorySettings, default=None
    )

    smb_file_share_visibility: bool | core.BoolOut | None = core.attr(bool, default=None)

    smb_guest_password: str | core.StringOut | None = core.attr(str, default=None)

    smb_security_strategy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tape_drive_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_name: str | core.StringOut,
        gateway_timezone: str | core.StringOut,
        activation_key: str | core.StringOut | None = None,
        average_download_rate_limit_in_bits_per_sec: int | core.IntOut | None = None,
        average_upload_rate_limit_in_bits_per_sec: int | core.IntOut | None = None,
        cloudwatch_log_group_arn: str | core.StringOut | None = None,
        gateway_ip_address: str | core.StringOut | None = None,
        gateway_type: str | core.StringOut | None = None,
        gateway_vpc_endpoint: str | core.StringOut | None = None,
        maintenance_start_time: MaintenanceStartTime | None = None,
        medium_changer_type: str | core.StringOut | None = None,
        smb_active_directory_settings: SmbActiveDirectorySettings | None = None,
        smb_file_share_visibility: bool | core.BoolOut | None = None,
        smb_guest_password: str | core.StringOut | None = None,
        smb_security_strategy: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tape_drive_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Gateway.Args(
                gateway_name=gateway_name,
                gateway_timezone=gateway_timezone,
                activation_key=activation_key,
                average_download_rate_limit_in_bits_per_sec=average_download_rate_limit_in_bits_per_sec,
                average_upload_rate_limit_in_bits_per_sec=average_upload_rate_limit_in_bits_per_sec,
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                gateway_ip_address=gateway_ip_address,
                gateway_type=gateway_type,
                gateway_vpc_endpoint=gateway_vpc_endpoint,
                maintenance_start_time=maintenance_start_time,
                medium_changer_type=medium_changer_type,
                smb_active_directory_settings=smb_active_directory_settings,
                smb_file_share_visibility=smb_file_share_visibility,
                smb_guest_password=smb_guest_password,
                smb_security_strategy=smb_security_strategy,
                tags=tags,
                tags_all=tags_all,
                tape_drive_type=tape_drive_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activation_key: str | core.StringOut | None = core.arg(default=None)

        average_download_rate_limit_in_bits_per_sec: int | core.IntOut | None = core.arg(
            default=None
        )

        average_upload_rate_limit_in_bits_per_sec: int | core.IntOut | None = core.arg(default=None)

        cloudwatch_log_group_arn: str | core.StringOut | None = core.arg(default=None)

        gateway_ip_address: str | core.StringOut | None = core.arg(default=None)

        gateway_name: str | core.StringOut = core.arg()

        gateway_timezone: str | core.StringOut = core.arg()

        gateway_type: str | core.StringOut | None = core.arg(default=None)

        gateway_vpc_endpoint: str | core.StringOut | None = core.arg(default=None)

        maintenance_start_time: MaintenanceStartTime | None = core.arg(default=None)

        medium_changer_type: str | core.StringOut | None = core.arg(default=None)

        smb_active_directory_settings: SmbActiveDirectorySettings | None = core.arg(default=None)

        smb_file_share_visibility: bool | core.BoolOut | None = core.arg(default=None)

        smb_guest_password: str | core.StringOut | None = core.arg(default=None)

        smb_security_strategy: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tape_drive_type: str | core.StringOut | None = core.arg(default=None)
