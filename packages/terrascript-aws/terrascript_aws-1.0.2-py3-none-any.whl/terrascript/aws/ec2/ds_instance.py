import terrascript.core as core


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        device_name: str | core.StringOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        kms_key_id: str | core.StringOut,
        snapshot_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_id: str | core.StringOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
                throughput=throughput,
                volume_id=volume_id,
                volume_size=volume_size,
                volume_type=volume_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut = core.arg()

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut = core.arg()

        volume_id: str | core.StringOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.schema
class CreditSpecification(core.Schema):

    cpu_credits: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cpu_credits: str | core.StringOut,
    ):
        super().__init__(
            args=CreditSpecification.Args(
                cpu_credits=cpu_credits,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_credits: str | core.StringOut = core.arg()


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: str | core.StringOut = core.attr(str)

    no_device: bool | core.BoolOut | None = core.attr(bool, default=None)

    virtual_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        no_device: bool | core.BoolOut | None = None,
        virtual_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        no_device: bool | core.BoolOut | None = core.arg(default=None)

        virtual_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EnclaveOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=EnclaveOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        auto_recovery: str | core.StringOut,
    ):
        super().__init__(
            args=MaintenanceOptions.Args(
                auto_recovery=auto_recovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_recovery: str | core.StringOut = core.arg()


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_resource_name_dns_aaaa_record: bool | core.BoolOut = core.attr(bool, computed=True)

    hostname_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enable_resource_name_dns_a_record: bool | core.BoolOut,
        enable_resource_name_dns_aaaa_record: bool | core.BoolOut,
        hostname_type: str | core.StringOut,
    ):
        super().__init__(
            args=PrivateDnsNameOptions.Args(
                enable_resource_name_dns_a_record=enable_resource_name_dns_a_record,
                enable_resource_name_dns_aaaa_record=enable_resource_name_dns_aaaa_record,
                hostname_type=hostname_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_resource_name_dns_a_record: bool | core.BoolOut = core.arg()

        enable_resource_name_dns_aaaa_record: bool | core.BoolOut = core.arg()

        hostname_type: str | core.StringOut = core.arg()


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut = core.attr(str, computed=True)

    http_put_response_hop_limit: int | core.IntOut = core.attr(int, computed=True)

    http_tokens: str | core.StringOut = core.attr(str, computed=True)

    instance_metadata_tags: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut,
        http_put_response_hop_limit: int | core.IntOut,
        http_tokens: str | core.StringOut,
        instance_metadata_tags: str | core.StringOut,
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
                instance_metadata_tags=instance_metadata_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: str | core.StringOut = core.arg()

        http_put_response_hop_limit: int | core.IntOut = core.arg()

        http_tokens: str | core.StringOut = core.arg()

        instance_metadata_tags: str | core.StringOut = core.arg()


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        device_name: str | core.StringOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        kms_key_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_id: str | core.StringOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                throughput=throughput,
                volume_id=volume_id,
                volume_size=volume_size,
                volume_type=volume_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut = core.arg()

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        throughput: int | core.IntOut = core.arg()

        volume_id: str | core.StringOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.data(type="aws_instance", namespace="aws_ec2")
class DsInstance(core.Data):

    ami: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    associate_public_ip_address: bool | core.BoolOut = core.attr(bool, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    credit_specification: list[CreditSpecification] | core.ArrayOut[
        CreditSpecification
    ] = core.attr(CreditSpecification, computed=True, kind=core.Kind.array)

    disable_api_stop: bool | core.BoolOut = core.attr(bool, computed=True)

    disable_api_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] = core.attr(
        EbsBlockDevice, computed=True, kind=core.Kind.array
    )

    ebs_optimized: bool | core.BoolOut = core.attr(bool, computed=True)

    enclave_options: list[EnclaveOptions] | core.ArrayOut[EnclaveOptions] = core.attr(
        EnclaveOptions, computed=True, kind=core.Kind.array
    )

    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] = core.attr(EphemeralBlockDevice, computed=True, kind=core.Kind.array)

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    get_password_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    get_user_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    host_id: str | core.StringOut = core.attr(str, computed=True)

    iam_instance_profile: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut | None = core.attr(str, default=None)

    instance_state: str | core.StringOut = core.attr(str, computed=True)

    instance_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    instance_type: str | core.StringOut = core.attr(str, computed=True)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    key_name: str | core.StringOut = core.attr(str, computed=True)

    maintenance_options: list[MaintenanceOptions] | core.ArrayOut[MaintenanceOptions] = core.attr(
        MaintenanceOptions, computed=True, kind=core.Kind.array
    )

    metadata_options: list[MetadataOptions] | core.ArrayOut[MetadataOptions] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    monitoring: bool | core.BoolOut = core.attr(bool, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    password_data: str | core.StringOut = core.attr(str, computed=True)

    placement_group: str | core.StringOut = core.attr(str, computed=True)

    placement_partition_number: int | core.IntOut = core.attr(int, computed=True)

    private_dns: str | core.StringOut = core.attr(str, computed=True)

    private_dns_name_options: list[PrivateDnsNameOptions] | core.ArrayOut[
        PrivateDnsNameOptions
    ] = core.attr(PrivateDnsNameOptions, computed=True, kind=core.Kind.array)

    private_ip: str | core.StringOut = core.attr(str, computed=True)

    public_dns: str | core.StringOut = core.attr(str, computed=True)

    public_ip: str | core.StringOut = core.attr(str, computed=True)

    root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] = core.attr(
        RootBlockDevice, computed=True, kind=core.Kind.array
    )

    secondary_private_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_dest_check: bool | core.BoolOut = core.attr(bool, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tenancy: str | core.StringOut = core.attr(str, computed=True)

    user_data: str | core.StringOut = core.attr(str, computed=True)

    user_data_base64: str | core.StringOut = core.attr(str, computed=True)

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        get_password_data: bool | core.BoolOut | None = None,
        get_user_data: bool | core.BoolOut | None = None,
        instance_id: str | core.StringOut | None = None,
        instance_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstance.Args(
                filter=filter,
                get_password_data=get_password_data,
                get_user_data=get_user_data,
                instance_id=instance_id,
                instance_tags=instance_tags,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        get_password_data: bool | core.BoolOut | None = core.arg(default=None)

        get_user_data: bool | core.BoolOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        instance_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
