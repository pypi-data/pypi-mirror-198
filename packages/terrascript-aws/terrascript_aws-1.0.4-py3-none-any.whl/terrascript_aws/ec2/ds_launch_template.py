import terrascript.core as core


@core.schema
class CapacityReservationTarget(core.Schema):

    capacity_reservation_id: str | core.StringOut = core.attr(str, computed=True)

    capacity_reservation_resource_group_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        capacity_reservation_id: str | core.StringOut,
        capacity_reservation_resource_group_arn: str | core.StringOut,
    ):
        super().__init__(
            args=CapacityReservationTarget.Args(
                capacity_reservation_id=capacity_reservation_id,
                capacity_reservation_resource_group_arn=capacity_reservation_resource_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_id: str | core.StringOut = core.arg()

        capacity_reservation_resource_group_arn: str | core.StringOut = core.arg()


@core.schema
class CapacityReservationSpecification(core.Schema):

    capacity_reservation_preference: str | core.StringOut = core.attr(str, computed=True)

    capacity_reservation_target: list[CapacityReservationTarget] | core.ArrayOut[
        CapacityReservationTarget
    ] = core.attr(CapacityReservationTarget, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        capacity_reservation_preference: str | core.StringOut,
        capacity_reservation_target: list[CapacityReservationTarget]
        | core.ArrayOut[CapacityReservationTarget],
    ):
        super().__init__(
            args=CapacityReservationSpecification.Args(
                capacity_reservation_preference=capacity_reservation_preference,
                capacity_reservation_target=capacity_reservation_target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_preference: str | core.StringOut = core.arg()

        capacity_reservation_target: list[CapacityReservationTarget] | core.ArrayOut[
            CapacityReservationTarget
        ] = core.arg()


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
class Ebs(core.Schema):

    delete_on_termination: str | core.StringOut = core.attr(str, computed=True)

    encrypted: str | core.StringOut = core.attr(str, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: str | core.StringOut,
        encrypted: str | core.StringOut,
        iops: int | core.IntOut,
        kms_key_id: str | core.StringOut,
        snapshot_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
    ):
        super().__init__(
            args=Ebs.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: str | core.StringOut = core.arg()

        encrypted: str | core.StringOut = core.arg()

        iops: int | core.IntOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()

        throughput: int | core.IntOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.schema
class BlockDeviceMappings(core.Schema):

    device_name: str | core.StringOut = core.attr(str, computed=True)

    ebs: list[Ebs] | core.ArrayOut[Ebs] = core.attr(Ebs, computed=True, kind=core.Kind.array)

    no_device: str | core.StringOut = core.attr(str, computed=True)

    virtual_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        ebs: list[Ebs] | core.ArrayOut[Ebs],
        no_device: str | core.StringOut,
        virtual_name: str | core.StringOut,
    ):
        super().__init__(
            args=BlockDeviceMappings.Args(
                device_name=device_name,
                ebs=ebs,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        ebs: list[Ebs] | core.ArrayOut[Ebs] = core.arg()

        no_device: str | core.StringOut = core.arg()

        virtual_name: str | core.StringOut = core.arg()


@core.schema
class CpuOptions(core.Schema):

    core_count: int | core.IntOut = core.attr(int, computed=True)

    threads_per_core: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        core_count: int | core.IntOut,
        threads_per_core: int | core.IntOut,
    ):
        super().__init__(
            args=CpuOptions.Args(
                core_count=core_count,
                threads_per_core=threads_per_core,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        core_count: int | core.IntOut = core.arg()

        threads_per_core: int | core.IntOut = core.arg()


@core.schema
class ElasticGpuSpecifications(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=ElasticGpuSpecifications.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


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
class Monitoring(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=Monitoring.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class IamInstanceProfile(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=IamInstanceProfile.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Placement(core.Schema):

    affinity: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    group_name: str | core.StringOut = core.attr(str, computed=True)

    host_id: str | core.StringOut = core.attr(str, computed=True)

    host_resource_group_arn: str | core.StringOut = core.attr(str, computed=True)

    partition_number: int | core.IntOut = core.attr(int, computed=True)

    spread_domain: str | core.StringOut = core.attr(str, computed=True)

    tenancy: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        affinity: str | core.StringOut,
        availability_zone: str | core.StringOut,
        group_name: str | core.StringOut,
        host_id: str | core.StringOut,
        host_resource_group_arn: str | core.StringOut,
        partition_number: int | core.IntOut,
        spread_domain: str | core.StringOut,
        tenancy: str | core.StringOut,
    ):
        super().__init__(
            args=Placement.Args(
                affinity=affinity,
                availability_zone=availability_zone,
                group_name=group_name,
                host_id=host_id,
                host_resource_group_arn=host_resource_group_arn,
                partition_number=partition_number,
                spread_domain=spread_domain,
                tenancy=tenancy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        affinity: str | core.StringOut = core.arg()

        availability_zone: str | core.StringOut = core.arg()

        group_name: str | core.StringOut = core.arg()

        host_id: str | core.StringOut = core.arg()

        host_resource_group_arn: str | core.StringOut = core.arg()

        partition_number: int | core.IntOut = core.arg()

        spread_domain: str | core.StringOut = core.arg()

        tenancy: str | core.StringOut = core.arg()


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
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut = core.attr(str, computed=True)

    http_protocol_ipv6: str | core.StringOut = core.attr(str, computed=True)

    http_put_response_hop_limit: int | core.IntOut = core.attr(int, computed=True)

    http_tokens: str | core.StringOut = core.attr(str, computed=True)

    instance_metadata_tags: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut,
        http_protocol_ipv6: str | core.StringOut,
        http_put_response_hop_limit: int | core.IntOut,
        http_tokens: str | core.StringOut,
        instance_metadata_tags: str | core.StringOut,
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_protocol_ipv6=http_protocol_ipv6,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
                instance_metadata_tags=instance_metadata_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: str | core.StringOut = core.arg()

        http_protocol_ipv6: str | core.StringOut = core.arg()

        http_put_response_hop_limit: int | core.IntOut = core.arg()

        http_tokens: str | core.StringOut = core.arg()

        instance_metadata_tags: str | core.StringOut = core.arg()


@core.schema
class TagSpecifications(core.Schema):

    resource_type: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        resource_type: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=TagSpecifications.Args(
                resource_type=resource_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_type: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class LicenseSpecification(core.Schema):

    license_configuration_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        license_configuration_arn: str | core.StringOut,
    ):
        super().__init__(
            args=LicenseSpecification.Args(
                license_configuration_arn=license_configuration_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        license_configuration_arn: str | core.StringOut = core.arg()


@core.schema
class ElasticInferenceAccelerator(core.Schema):

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=ElasticInferenceAccelerator.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class HibernationOptions(core.Schema):

    configured: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        configured: bool | core.BoolOut,
    ):
        super().__init__(
            args=HibernationOptions.Args(
                configured=configured,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configured: bool | core.BoolOut = core.arg()


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
class SpotOptions(core.Schema):

    block_duration_minutes: int | core.IntOut = core.attr(int, computed=True)

    instance_interruption_behavior: str | core.StringOut = core.attr(str, computed=True)

    max_price: str | core.StringOut = core.attr(str, computed=True)

    spot_instance_type: str | core.StringOut = core.attr(str, computed=True)

    valid_until: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        block_duration_minutes: int | core.IntOut,
        instance_interruption_behavior: str | core.StringOut,
        max_price: str | core.StringOut,
        spot_instance_type: str | core.StringOut,
        valid_until: str | core.StringOut,
    ):
        super().__init__(
            args=SpotOptions.Args(
                block_duration_minutes=block_duration_minutes,
                instance_interruption_behavior=instance_interruption_behavior,
                max_price=max_price,
                spot_instance_type=spot_instance_type,
                valid_until=valid_until,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_duration_minutes: int | core.IntOut = core.arg()

        instance_interruption_behavior: str | core.StringOut = core.arg()

        max_price: str | core.StringOut = core.arg()

        spot_instance_type: str | core.StringOut = core.arg()

        valid_until: str | core.StringOut = core.arg()


@core.schema
class InstanceMarketOptions(core.Schema):

    market_type: str | core.StringOut = core.attr(str, computed=True)

    spot_options: list[SpotOptions] | core.ArrayOut[SpotOptions] = core.attr(
        SpotOptions, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        market_type: str | core.StringOut,
        spot_options: list[SpotOptions] | core.ArrayOut[SpotOptions],
    ):
        super().__init__(
            args=InstanceMarketOptions.Args(
                market_type=market_type,
                spot_options=spot_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        market_type: str | core.StringOut = core.arg()

        spot_options: list[SpotOptions] | core.ArrayOut[SpotOptions] = core.arg()


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
class TotalLocalStorageGb(core.Schema):

    max: float | core.FloatOut = core.attr(float, computed=True)

    min: float | core.FloatOut = core.attr(float, computed=True)

    def __init__(
        self,
        *,
        max: float | core.FloatOut,
        min: float | core.FloatOut,
    ):
        super().__init__(
            args=TotalLocalStorageGb.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: float | core.FloatOut = core.arg()

        min: float | core.FloatOut = core.arg()


@core.schema
class MemoryMib(core.Schema):

    max: int | core.IntOut = core.attr(int, computed=True)

    min: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        max: int | core.IntOut,
        min: int | core.IntOut,
    ):
        super().__init__(
            args=MemoryMib.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut = core.arg()

        min: int | core.IntOut = core.arg()


@core.schema
class NetworkInterfaceCount(core.Schema):

    max: int | core.IntOut = core.attr(int, computed=True)

    min: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        max: int | core.IntOut,
        min: int | core.IntOut,
    ):
        super().__init__(
            args=NetworkInterfaceCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut = core.arg()

        min: int | core.IntOut = core.arg()


@core.schema
class BaselineEbsBandwidthMbps(core.Schema):

    max: int | core.IntOut = core.attr(int, computed=True)

    min: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        max: int | core.IntOut,
        min: int | core.IntOut,
    ):
        super().__init__(
            args=BaselineEbsBandwidthMbps.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut = core.arg()

        min: int | core.IntOut = core.arg()


@core.schema
class MemoryGibPerVcpu(core.Schema):

    max: float | core.FloatOut = core.attr(float, computed=True)

    min: float | core.FloatOut = core.attr(float, computed=True)

    def __init__(
        self,
        *,
        max: float | core.FloatOut,
        min: float | core.FloatOut,
    ):
        super().__init__(
            args=MemoryGibPerVcpu.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: float | core.FloatOut = core.arg()

        min: float | core.FloatOut = core.arg()


@core.schema
class VcpuCount(core.Schema):

    max: int | core.IntOut = core.attr(int, computed=True)

    min: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        max: int | core.IntOut,
        min: int | core.IntOut,
    ):
        super().__init__(
            args=VcpuCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut = core.arg()

        min: int | core.IntOut = core.arg()


@core.schema
class AcceleratorTotalMemoryMib(core.Schema):

    max: int | core.IntOut = core.attr(int, computed=True)

    min: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        max: int | core.IntOut,
        min: int | core.IntOut,
    ):
        super().__init__(
            args=AcceleratorTotalMemoryMib.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut = core.arg()

        min: int | core.IntOut = core.arg()


@core.schema
class AcceleratorCount(core.Schema):

    max: int | core.IntOut = core.attr(int, computed=True)

    min: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        max: int | core.IntOut,
        min: int | core.IntOut,
    ):
        super().__init__(
            args=AcceleratorCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut = core.arg()

        min: int | core.IntOut = core.arg()


@core.schema
class InstanceRequirements(core.Schema):

    accelerator_count: list[AcceleratorCount] | core.ArrayOut[AcceleratorCount] = core.attr(
        AcceleratorCount, computed=True, kind=core.Kind.array
    )

    accelerator_manufacturers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    accelerator_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    accelerator_total_memory_mib: list[AcceleratorTotalMemoryMib] | core.ArrayOut[
        AcceleratorTotalMemoryMib
    ] = core.attr(AcceleratorTotalMemoryMib, computed=True, kind=core.Kind.array)

    accelerator_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    bare_metal: str | core.StringOut = core.attr(str, computed=True)

    baseline_ebs_bandwidth_mbps: list[BaselineEbsBandwidthMbps] | core.ArrayOut[
        BaselineEbsBandwidthMbps
    ] = core.attr(BaselineEbsBandwidthMbps, computed=True, kind=core.Kind.array)

    burstable_performance: str | core.StringOut = core.attr(str, computed=True)

    cpu_manufacturers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    excluded_instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    instance_generations: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    local_storage: str | core.StringOut = core.attr(str, computed=True)

    local_storage_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    memory_gib_per_vcpu: list[MemoryGibPerVcpu] | core.ArrayOut[MemoryGibPerVcpu] = core.attr(
        MemoryGibPerVcpu, computed=True, kind=core.Kind.array
    )

    memory_mib: list[MemoryMib] | core.ArrayOut[MemoryMib] = core.attr(
        MemoryMib, computed=True, kind=core.Kind.array
    )

    network_interface_count: list[NetworkInterfaceCount] | core.ArrayOut[
        NetworkInterfaceCount
    ] = core.attr(NetworkInterfaceCount, computed=True, kind=core.Kind.array)

    on_demand_max_price_percentage_over_lowest_price: int | core.IntOut = core.attr(
        int, computed=True
    )

    require_hibernate_support: bool | core.BoolOut = core.attr(bool, computed=True)

    spot_max_price_percentage_over_lowest_price: int | core.IntOut = core.attr(int, computed=True)

    total_local_storage_gb: list[TotalLocalStorageGb] | core.ArrayOut[
        TotalLocalStorageGb
    ] = core.attr(TotalLocalStorageGb, computed=True, kind=core.Kind.array)

    vcpu_count: list[VcpuCount] | core.ArrayOut[VcpuCount] = core.attr(
        VcpuCount, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        accelerator_count: list[AcceleratorCount] | core.ArrayOut[AcceleratorCount],
        accelerator_manufacturers: list[str] | core.ArrayOut[core.StringOut],
        accelerator_names: list[str] | core.ArrayOut[core.StringOut],
        accelerator_total_memory_mib: list[AcceleratorTotalMemoryMib]
        | core.ArrayOut[AcceleratorTotalMemoryMib],
        accelerator_types: list[str] | core.ArrayOut[core.StringOut],
        bare_metal: str | core.StringOut,
        baseline_ebs_bandwidth_mbps: list[BaselineEbsBandwidthMbps]
        | core.ArrayOut[BaselineEbsBandwidthMbps],
        burstable_performance: str | core.StringOut,
        cpu_manufacturers: list[str] | core.ArrayOut[core.StringOut],
        excluded_instance_types: list[str] | core.ArrayOut[core.StringOut],
        instance_generations: list[str] | core.ArrayOut[core.StringOut],
        local_storage: str | core.StringOut,
        local_storage_types: list[str] | core.ArrayOut[core.StringOut],
        memory_gib_per_vcpu: list[MemoryGibPerVcpu] | core.ArrayOut[MemoryGibPerVcpu],
        memory_mib: list[MemoryMib] | core.ArrayOut[MemoryMib],
        network_interface_count: list[NetworkInterfaceCount] | core.ArrayOut[NetworkInterfaceCount],
        on_demand_max_price_percentage_over_lowest_price: int | core.IntOut,
        require_hibernate_support: bool | core.BoolOut,
        spot_max_price_percentage_over_lowest_price: int | core.IntOut,
        total_local_storage_gb: list[TotalLocalStorageGb] | core.ArrayOut[TotalLocalStorageGb],
        vcpu_count: list[VcpuCount] | core.ArrayOut[VcpuCount],
    ):
        super().__init__(
            args=InstanceRequirements.Args(
                accelerator_count=accelerator_count,
                accelerator_manufacturers=accelerator_manufacturers,
                accelerator_names=accelerator_names,
                accelerator_total_memory_mib=accelerator_total_memory_mib,
                accelerator_types=accelerator_types,
                bare_metal=bare_metal,
                baseline_ebs_bandwidth_mbps=baseline_ebs_bandwidth_mbps,
                burstable_performance=burstable_performance,
                cpu_manufacturers=cpu_manufacturers,
                excluded_instance_types=excluded_instance_types,
                instance_generations=instance_generations,
                local_storage=local_storage,
                local_storage_types=local_storage_types,
                memory_gib_per_vcpu=memory_gib_per_vcpu,
                memory_mib=memory_mib,
                network_interface_count=network_interface_count,
                on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
                require_hibernate_support=require_hibernate_support,
                spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
                total_local_storage_gb=total_local_storage_gb,
                vcpu_count=vcpu_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accelerator_count: list[AcceleratorCount] | core.ArrayOut[AcceleratorCount] = core.arg()

        accelerator_manufacturers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        accelerator_names: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        accelerator_total_memory_mib: list[AcceleratorTotalMemoryMib] | core.ArrayOut[
            AcceleratorTotalMemoryMib
        ] = core.arg()

        accelerator_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        bare_metal: str | core.StringOut = core.arg()

        baseline_ebs_bandwidth_mbps: list[BaselineEbsBandwidthMbps] | core.ArrayOut[
            BaselineEbsBandwidthMbps
        ] = core.arg()

        burstable_performance: str | core.StringOut = core.arg()

        cpu_manufacturers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        excluded_instance_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        instance_generations: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        local_storage: str | core.StringOut = core.arg()

        local_storage_types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        memory_gib_per_vcpu: list[MemoryGibPerVcpu] | core.ArrayOut[MemoryGibPerVcpu] = core.arg()

        memory_mib: list[MemoryMib] | core.ArrayOut[MemoryMib] = core.arg()

        network_interface_count: list[NetworkInterfaceCount] | core.ArrayOut[
            NetworkInterfaceCount
        ] = core.arg()

        on_demand_max_price_percentage_over_lowest_price: int | core.IntOut = core.arg()

        require_hibernate_support: bool | core.BoolOut = core.arg()

        spot_max_price_percentage_over_lowest_price: int | core.IntOut = core.arg()

        total_local_storage_gb: list[TotalLocalStorageGb] | core.ArrayOut[
            TotalLocalStorageGb
        ] = core.arg()

        vcpu_count: list[VcpuCount] | core.ArrayOut[VcpuCount] = core.arg()


@core.schema
class NetworkInterfaces(core.Schema):

    associate_carrier_ip_address: str | core.StringOut = core.attr(str, computed=True)

    associate_public_ip_address: str | core.StringOut = core.attr(str, computed=True)

    delete_on_termination: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    device_index: int | core.IntOut = core.attr(int, computed=True)

    interface_type: str | core.StringOut = core.attr(str, computed=True)

    ipv4_address_count: int | core.IntOut = core.attr(int, computed=True)

    ipv4_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ipv4_prefix_count: int | core.IntOut = core.attr(int, computed=True)

    ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ipv6_address_count: int | core.IntOut = core.attr(int, computed=True)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    ipv6_prefix_count: int | core.IntOut = core.attr(int, computed=True)

    ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    network_card_index: int | core.IntOut = core.attr(int, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    private_ip_address: str | core.StringOut = core.attr(str, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        associate_carrier_ip_address: str | core.StringOut,
        associate_public_ip_address: str | core.StringOut,
        delete_on_termination: str | core.StringOut,
        description: str | core.StringOut,
        device_index: int | core.IntOut,
        interface_type: str | core.StringOut,
        ipv4_address_count: int | core.IntOut,
        ipv4_addresses: list[str] | core.ArrayOut[core.StringOut],
        ipv4_prefix_count: int | core.IntOut,
        ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut],
        ipv6_address_count: int | core.IntOut,
        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut],
        ipv6_prefix_count: int | core.IntOut,
        ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut],
        network_card_index: int | core.IntOut,
        network_interface_id: str | core.StringOut,
        private_ip_address: str | core.StringOut,
        security_groups: list[str] | core.ArrayOut[core.StringOut],
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkInterfaces.Args(
                associate_carrier_ip_address=associate_carrier_ip_address,
                associate_public_ip_address=associate_public_ip_address,
                delete_on_termination=delete_on_termination,
                description=description,
                device_index=device_index,
                interface_type=interface_type,
                ipv4_address_count=ipv4_address_count,
                ipv4_addresses=ipv4_addresses,
                ipv4_prefix_count=ipv4_prefix_count,
                ipv4_prefixes=ipv4_prefixes,
                ipv6_address_count=ipv6_address_count,
                ipv6_addresses=ipv6_addresses,
                ipv6_prefix_count=ipv6_prefix_count,
                ipv6_prefixes=ipv6_prefixes,
                network_card_index=network_card_index,
                network_interface_id=network_interface_id,
                private_ip_address=private_ip_address,
                security_groups=security_groups,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        associate_carrier_ip_address: str | core.StringOut = core.arg()

        associate_public_ip_address: str | core.StringOut = core.arg()

        delete_on_termination: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()

        device_index: int | core.IntOut = core.arg()

        interface_type: str | core.StringOut = core.arg()

        ipv4_address_count: int | core.IntOut = core.arg()

        ipv4_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        ipv4_prefix_count: int | core.IntOut = core.arg()

        ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        ipv6_address_count: int | core.IntOut = core.arg()

        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        ipv6_prefix_count: int | core.IntOut = core.arg()

        ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        network_card_index: int | core.IntOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()

        private_ip_address: str | core.StringOut = core.arg()

        security_groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.data(type="aws_launch_template", namespace="ec2")
class DsLaunchTemplate(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    block_device_mappings: list[BlockDeviceMappings] | core.ArrayOut[
        BlockDeviceMappings
    ] = core.attr(BlockDeviceMappings, computed=True, kind=core.Kind.array)

    capacity_reservation_specification: list[CapacityReservationSpecification] | core.ArrayOut[
        CapacityReservationSpecification
    ] = core.attr(CapacityReservationSpecification, computed=True, kind=core.Kind.array)

    cpu_options: list[CpuOptions] | core.ArrayOut[CpuOptions] = core.attr(
        CpuOptions, computed=True, kind=core.Kind.array
    )

    credit_specification: list[CreditSpecification] | core.ArrayOut[
        CreditSpecification
    ] = core.attr(CreditSpecification, computed=True, kind=core.Kind.array)

    default_version: int | core.IntOut = core.attr(int, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    disable_api_stop: bool | core.BoolOut = core.attr(bool, computed=True)

    disable_api_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    ebs_optimized: str | core.StringOut = core.attr(str, computed=True)

    elastic_gpu_specifications: list[ElasticGpuSpecifications] | core.ArrayOut[
        ElasticGpuSpecifications
    ] = core.attr(ElasticGpuSpecifications, computed=True, kind=core.Kind.array)

    elastic_inference_accelerator: list[ElasticInferenceAccelerator] | core.ArrayOut[
        ElasticInferenceAccelerator
    ] = core.attr(ElasticInferenceAccelerator, computed=True, kind=core.Kind.array)

    enclave_options: list[EnclaveOptions] | core.ArrayOut[EnclaveOptions] = core.attr(
        EnclaveOptions, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block(s) for filtering. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    hibernation_options: list[HibernationOptions] | core.ArrayOut[HibernationOptions] = core.attr(
        HibernationOptions, computed=True, kind=core.Kind.array
    )

    iam_instance_profile: list[IamInstanceProfile] | core.ArrayOut[IamInstanceProfile] = core.attr(
        IamInstanceProfile, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ID of the specific launch template to retrieve.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    image_id: str | core.StringOut = core.attr(str, computed=True)

    instance_initiated_shutdown_behavior: str | core.StringOut = core.attr(str, computed=True)

    instance_market_options: list[InstanceMarketOptions] | core.ArrayOut[
        InstanceMarketOptions
    ] = core.attr(InstanceMarketOptions, computed=True, kind=core.Kind.array)

    instance_requirements: list[InstanceRequirements] | core.ArrayOut[
        InstanceRequirements
    ] = core.attr(InstanceRequirements, computed=True, kind=core.Kind.array)

    instance_type: str | core.StringOut = core.attr(str, computed=True)

    kernel_id: str | core.StringOut = core.attr(str, computed=True)

    key_name: str | core.StringOut = core.attr(str, computed=True)

    latest_version: int | core.IntOut = core.attr(int, computed=True)

    license_specification: list[LicenseSpecification] | core.ArrayOut[
        LicenseSpecification
    ] = core.attr(LicenseSpecification, computed=True, kind=core.Kind.array)

    maintenance_options: list[MaintenanceOptions] | core.ArrayOut[MaintenanceOptions] = core.attr(
        MaintenanceOptions, computed=True, kind=core.Kind.array
    )

    metadata_options: list[MetadataOptions] | core.ArrayOut[MetadataOptions] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    monitoring: list[Monitoring] | core.ArrayOut[Monitoring] = core.attr(
        Monitoring, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The name of the launch template.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    network_interfaces: list[NetworkInterfaces] | core.ArrayOut[NetworkInterfaces] = core.attr(
        NetworkInterfaces, computed=True, kind=core.Kind.array
    )

    placement: list[Placement] | core.ArrayOut[Placement] = core.attr(
        Placement, computed=True, kind=core.Kind.array
    )

    private_dns_name_options: list[PrivateDnsNameOptions] | core.ArrayOut[
        PrivateDnsNameOptions
    ] = core.attr(PrivateDnsNameOptions, computed=True, kind=core.Kind.array)

    ram_disk_id: str | core.StringOut = core.attr(str, computed=True)

    security_group_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tag_specifications: list[TagSpecifications] | core.ArrayOut[TagSpecifications] = core.attr(
        TagSpecifications, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags, each pair of which must exactly match a pair on the desired Launch Templat
    e.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_data: str | core.StringOut = core.attr(str, computed=True)

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLaunchTemplate.Args(
                filter=filter,
                id=id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
