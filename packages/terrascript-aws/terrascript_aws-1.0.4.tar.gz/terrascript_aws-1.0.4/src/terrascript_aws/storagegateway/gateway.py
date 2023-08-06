import terrascript.core as core


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


@core.resource(type="aws_storagegateway_gateway", namespace="storagegateway")
class Gateway(core.Resource):
    """
    (Optional) Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Add
    itional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/sto
    ragegateway/latest/userguide/get-activation-key.html).
    """

    activation_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of the gateway.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The average download bandwidth rate limit in bits per second. This is supported for the `
    CACHED`, `STORED`, and `VTL` gateway types.
    """
    average_download_rate_limit_in_bits_per_sec: int | core.IntOut | None = core.attr(
        int, default=None
    )

    """
    (Optional) The average upload bandwidth rate limit in bits per second. This is supported for the `CA
    CHED`, `STORED`, and `VTL` gateway types.
    """
    average_upload_rate_limit_in_bits_per_sec: int | core.IntOut | None = core.attr(
        int, default=None
    )

    """
    (Optional) The Amazon Resource Name (ARN) of the Amazon CloudWatch log group to use to monitor and l
    og events in the gateway.
    """
    cloudwatch_log_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the Amazon EC2 instance that was used to launch the gateway.
    """
    ec2_instance_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of endpoint for your gateway.
    """
    endpoint_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the gateway.
    """
    gateway_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Gateway IP address to retrieve activation key during resource creation. Conflicts with `a
    ctivation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional in
    formation is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegatewa
    y/latest/userguide/get-activation-key.html).
    """
    gateway_ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Name of the gateway.
    """
    gateway_name: str | core.StringOut = core.attr(str)

    """
    An array that contains descriptions of the gateway network interfaces. See [Gateway Network Interfac
    e](#gateway-network-interface).
    """
    gateway_network_interface: list[GatewayNetworkInterface] | core.ArrayOut[
        GatewayNetworkInterface
    ] = core.attr(GatewayNetworkInterface, computed=True, kind=core.Kind.array)

    """
    (Required) Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:
    mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for ex
    ample, for scheduling snapshots and your gateway's maintenance schedule.
    """
    gateway_timezone: str | core.StringOut = core.attr(str)

    """
    (Optional) Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_FSX_SMB
    , `FILE_S3`, `STORED`, `VTL`.
    """
    gateway_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) VPC endpoint address to be used when activating your gateway. This should be used when yo
    ur instance is in a private subnet. Requires HTTP access from client computer running terraform. Mor
    e info on what ports are required by your VPC Endpoint Security group in [Activating a Gateway in a
    Virtual Private Cloud](https://docs.aws.amazon.com/storagegateway/latest/userguide/gateway-private-l
    ink.html).
    """
    gateway_vpc_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    """
    The type of hypervisor environment used by the host.
    """
    host_environment: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The gateway's weekly maintenance start time information, including day and time of the we
    ek. The maintenance time is the time in your gateway's time zone. More details below.
    """
    maintenance_start_time: MaintenanceStartTime | None = core.attr(
        MaintenanceStartTime, default=None, computed=True
    )

    """
    (Optional) Type of medium changer to use for tape gateway. Terraform cannot detect drift of this arg
    ument. Valid values: `STK-L700`, `AWS-Gateway-VTL`, `IBM-03584L32-0402`.
    """
    medium_changer_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Nested argument with Active Directory domain join information for Server Message Block (S
    MB) file shares. Only valid for `FILE_S3` and `FILE_FSX_SMB` gateway types. Must be set before creat
    ing `ActiveDirectory` authentication SMB file shares. More details below.
    """
    smb_active_directory_settings: SmbActiveDirectorySettings | None = core.attr(
        SmbActiveDirectorySettings, default=None
    )

    """
    (Optional) Specifies whether the shares on this gateway appear when listing shares.
    """
    smb_file_share_visibility: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` and `
    FILE_FSX_SMB` gateway types. Must be set before creating `GuestAccess` authentication SMB file share
    s. Terraform can only detect drift of the existence of a guest password, not its actual value from t
    he gateway. Terraform can however update the password with changing the argument.
    """
    smb_guest_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the type of security strategy. Valid values are: `ClientSpecified`, `MandatoryS
    igning`, and `MandatoryEncryption`. See [Setting a Security Level for Your Gateway](https://docs.aws
    .amazon.com/storagegateway/latest/userguide/managing-gateway-file.html#security-strategy) for more i
    nformation.
    """
    smb_security_strategy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argumen
    t. Valid values: `IBM-ULT3580-TD5`.
    """
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
