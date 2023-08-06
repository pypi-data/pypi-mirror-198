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


@core.resource(type="aws_fsx_ontap_file_system", namespace="aws_fsx")
class OntapFileSystem(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    automatic_backup_retention_days: int | core.IntOut | None = core.attr(int, default=None)

    daily_automatic_backup_start_time: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    deployment_type: str | core.StringOut = core.attr(str)

    disk_iops_configuration: DiskIopsConfiguration | None = core.attr(
        DiskIopsConfiguration, default=None, computed=True
    )

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    endpoint_ip_address_range: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    fsx_admin_password: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interface_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    preferred_subnet_id: str | core.StringOut = core.attr(str)

    route_table_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    storage_capacity: int | core.IntOut | None = core.attr(int, default=None)

    storage_type: str | core.StringOut | None = core.attr(str, default=None)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_capacity: int | core.IntOut = core.attr(int)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

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
