import terrascript.core as core


@core.schema
class DiskIopsConfiguration(core.Schema):

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        iops: int | core.IntOut | None = None,
        mode: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DiskIopsConfiguration.Args(
                iops=iops,
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: int | core.IntOut | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Intercluster(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Intercluster.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Management(core.Schema):

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: str | core.StringOut,
        ip_addresses: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Management.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: str | core.StringOut = core.arg()

        ip_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Endpoints(core.Schema):

    intercluster: list[Intercluster] | core.ArrayOut[Intercluster] = core.attr(
        Intercluster, computed=True, kind=core.Kind.array
    )

    management: list[Management] | core.ArrayOut[Management] = core.attr(
        Management, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        intercluster: list[Intercluster] | core.ArrayOut[Intercluster],
        management: list[Management] | core.ArrayOut[Management],
    ):
        super().__init__(
            args=Endpoints.Args(
                intercluster=intercluster,
                management=management,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intercluster: list[Intercluster] | core.ArrayOut[Intercluster] = core.arg()

        management: list[Management] | core.ArrayOut[Management] = core.arg()


@core.resource(type="aws_fsx_ontap_file_system", namespace="fsx")
class OntapFileSystem(core.Resource):
    """
    Amazon Resource Name of the file system.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of days to retain automatic backups. Setting this to 0 disables automatic back
    ups. You can retain automatic backups for a maximum of 90 days.
    """
    automatic_backup_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) A recurring daily time, in the format HH:MM. HH is the zero-padded hour of the day (0-23)
    , and MM is the zero-padded minute of the hour. For example, 05:00 specifies 5 AM daily. Requires `a
    utomatic_backup_retention_days` to be set.
    """
    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) - The filesystem deployment type. Supports `MULTI_AZ_1` and `SINGLE_AZ_1`.
    """
    deployment_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The SSD IOPS configuration for the Amazon FSx for NetApp ONTAP file system. See [Disk Iop
    s Configuration](#disk-iops-configuration) Below.
    """
    disk_iops_configuration: DiskIopsConfiguration | None = core.attr(
        DiskIopsConfiguration, default=None, computed=True
    )

    """
    DNS name for the file system, e.g., `fs-12345678.fsx.us-west-2.amazonaws.com`
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the IP address range in which the endpoints to access your file system will be
    created. By default, Amazon FSx selects an unused IP address range for you from the 198.19.* range.
    """
    endpoint_ip_address_range: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI,
    REST API, or NetApp SnapMirror. See [Endpoints](#endpoints) below.
    """
    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ONTAP administrative password for the fsxadmin user that you can use to administer yo
    ur file system using the ONTAP CLI and REST API.
    """
    fsx_admin_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    Identifier of the file system, e.g., `fs-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN for the KMS Key to encrypt the file system at rest, Defaults to an AWS managed KMS Ke
    y.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Set of Elastic Network Interface identifiers from which the file system is accessible The first netw
    ork interface returned is the primary network interface.
    """
    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    AWS account identifier that created the file system.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (V
    PC).
    """
    preferred_subnet_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the VPC route tables in which your file system's endpoints will be created. You
    should specify all VPC route tables associated with the subnets in which your clients are located.
    By default, Amazon FSx selects your VPC's default route table.
    """
    route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A list of IDs for the security groups that apply to the specified network interfaces crea
    ted for file system access. These security groups will apply to all network interfaces.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The storage capacity (GiB) of the file system. Valid values between `1024` and `196608`.
    """
    storage_capacity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) - The filesystem storage type. defaults to `SSD`.
    """
    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) A list of IDs for the subnets that the file system will be accessible from. Upto 2 subnet
    s can be provided.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the file system. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-
    level.
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
    (Required) Sets the throughput capacity (in MBps) for the file system that you're creating. Valid va
    lues are `128`, `256`, `512`, `1024`, and `2048`.
    """
    throughput_capacity: int | core.IntOut = core.attr(int)

    """
    Identifier of the Virtual Private Cloud for the file system.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC
    time zone.
    """
    weekly_maintenance_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_type: str | core.StringOut,
        preferred_subnet_id: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        throughput_capacity: int | core.IntOut,
        automatic_backup_retention_days: int | core.IntOut | None = None,
        daily_automatic_backup_start_time: str | core.StringOut | None = None,
        disk_iops_configuration: DiskIopsConfiguration | None = None,
        endpoint_ip_address_range: str | core.StringOut | None = None,
        fsx_admin_password: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        storage_capacity: int | core.IntOut | None = None,
        storage_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        weekly_maintenance_start_time: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OntapFileSystem.Args(
                deployment_type=deployment_type,
                preferred_subnet_id=preferred_subnet_id,
                subnet_ids=subnet_ids,
                throughput_capacity=throughput_capacity,
                automatic_backup_retention_days=automatic_backup_retention_days,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                disk_iops_configuration=disk_iops_configuration,
                endpoint_ip_address_range=endpoint_ip_address_range,
                fsx_admin_password=fsx_admin_password,
                kms_key_id=kms_key_id,
                route_table_ids=route_table_ids,
                security_group_ids=security_group_ids,
                storage_capacity=storage_capacity,
                storage_type=storage_type,
                tags=tags,
                tags_all=tags_all,
                weekly_maintenance_start_time=weekly_maintenance_start_time,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        automatic_backup_retention_days: int | core.IntOut | None = core.arg(default=None)

        daily_automatic_backup_start_time: str | core.StringOut | None = core.arg(default=None)

        deployment_type: str | core.StringOut = core.arg()

        disk_iops_configuration: DiskIopsConfiguration | None = core.arg(default=None)

        endpoint_ip_address_range: str | core.StringOut | None = core.arg(default=None)

        fsx_admin_password: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        preferred_subnet_id: str | core.StringOut = core.arg()

        route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        storage_capacity: int | core.IntOut | None = core.arg(default=None)

        storage_type: str | core.StringOut | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput_capacity: int | core.IntOut = core.arg()

        weekly_maintenance_start_time: str | core.StringOut | None = core.arg(default=None)
