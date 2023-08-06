import terrascript.core as core


@core.schema
class SpotOptions(core.Schema):

    block_duration_minutes: int | core.IntOut | None = core.attr(int, default=None)

    instance_interruption_behavior: str | core.StringOut | None = core.attr(str, default=None)

    max_price: str | core.StringOut | None = core.attr(str, default=None)

    spot_instance_type: str | core.StringOut | None = core.attr(str, default=None)

    valid_until: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        block_duration_minutes: int | core.IntOut | None = None,
        instance_interruption_behavior: str | core.StringOut | None = None,
        max_price: str | core.StringOut | None = None,
        spot_instance_type: str | core.StringOut | None = None,
        valid_until: str | core.StringOut | None = None,
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
        block_duration_minutes: int | core.IntOut | None = core.arg(default=None)

        instance_interruption_behavior: str | core.StringOut | None = core.arg(default=None)

        max_price: str | core.StringOut | None = core.arg(default=None)

        spot_instance_type: str | core.StringOut | None = core.arg(default=None)

        valid_until: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InstanceMarketOptions(core.Schema):

    market_type: str | core.StringOut | None = core.attr(str, default=None)

    spot_options: SpotOptions | None = core.attr(SpotOptions, default=None)

    def __init__(
        self,
        *,
        market_type: str | core.StringOut | None = None,
        spot_options: SpotOptions | None = None,
    ):
        super().__init__(
            args=InstanceMarketOptions.Args(
                market_type=market_type,
                spot_options=spot_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        market_type: str | core.StringOut | None = core.arg(default=None)

        spot_options: SpotOptions | None = core.arg(default=None)


@core.schema
class Placement(core.Schema):

    affinity: str | core.StringOut | None = core.attr(str, default=None)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    group_name: str | core.StringOut | None = core.attr(str, default=None)

    host_id: str | core.StringOut | None = core.attr(str, default=None)

    host_resource_group_arn: str | core.StringOut | None = core.attr(str, default=None)

    partition_number: int | core.IntOut | None = core.attr(int, default=None)

    spread_domain: str | core.StringOut | None = core.attr(str, default=None)

    tenancy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        affinity: str | core.StringOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        group_name: str | core.StringOut | None = None,
        host_id: str | core.StringOut | None = None,
        host_resource_group_arn: str | core.StringOut | None = None,
        partition_number: int | core.IntOut | None = None,
        spread_domain: str | core.StringOut | None = None,
        tenancy: str | core.StringOut | None = None,
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
        affinity: str | core.StringOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        group_name: str | core.StringOut | None = core.arg(default=None)

        host_id: str | core.StringOut | None = core.arg(default=None)

        host_resource_group_arn: str | core.StringOut | None = core.arg(default=None)

        partition_number: int | core.IntOut | None = core.arg(default=None)

        spread_domain: str | core.StringOut | None = core.arg(default=None)

        tenancy: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Ebs(core.Schema):

    delete_on_termination: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: str | core.StringOut | None = core.attr(str, default=None)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: str | core.StringOut | None = None,
        encrypted: str | core.StringOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
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
        delete_on_termination: str | core.StringOut | None = core.arg(default=None)

        encrypted: str | core.StringOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class BlockDeviceMappings(core.Schema):

    device_name: str | core.StringOut | None = core.attr(str, default=None)

    ebs: Ebs | None = core.attr(Ebs, default=None)

    no_device: str | core.StringOut | None = core.attr(str, default=None)

    virtual_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut | None = None,
        ebs: Ebs | None = None,
        no_device: str | core.StringOut | None = None,
        virtual_name: str | core.StringOut | None = None,
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
        device_name: str | core.StringOut | None = core.arg(default=None)

        ebs: Ebs | None = core.arg(default=None)

        no_device: str | core.StringOut | None = core.arg(default=None)

        virtual_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_resource_name_dns_aaaa_record: bool | core.BoolOut | None = core.attr(bool, default=None)

    hostname_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enable_resource_name_dns_a_record: bool | core.BoolOut | None = None,
        enable_resource_name_dns_aaaa_record: bool | core.BoolOut | None = None,
        hostname_type: str | core.StringOut | None = None,
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
        enable_resource_name_dns_a_record: bool | core.BoolOut | None = core.arg(default=None)

        enable_resource_name_dns_aaaa_record: bool | core.BoolOut | None = core.arg(default=None)

        hostname_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auto_recovery: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=MaintenanceOptions.Args(
                auto_recovery=auto_recovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_recovery: str | core.StringOut | None = core.arg(default=None)


@core.schema
class VcpuCount(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        min: int | core.IntOut,
        max: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=VcpuCount.Args(
                min=min,
                max=max,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut | None = core.arg(default=None)

        min: int | core.IntOut = core.arg()


@core.schema
class BaselineEbsBandwidthMbps(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: int | core.IntOut | None = None,
        min: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=BaselineEbsBandwidthMbps.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut | None = core.arg(default=None)

        min: int | core.IntOut | None = core.arg(default=None)


@core.schema
class MemoryMib(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        min: int | core.IntOut,
        max: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=MemoryMib.Args(
                min=min,
                max=max,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut | None = core.arg(default=None)

        min: int | core.IntOut = core.arg()


@core.schema
class TotalLocalStorageGb(core.Schema):

    max: float | core.FloatOut | None = core.attr(float, default=None)

    min: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        max: float | core.FloatOut | None = None,
        min: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=TotalLocalStorageGb.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: float | core.FloatOut | None = core.arg(default=None)

        min: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class AcceleratorCount(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: int | core.IntOut | None = None,
        min: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AcceleratorCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut | None = core.arg(default=None)

        min: int | core.IntOut | None = core.arg(default=None)


@core.schema
class AcceleratorTotalMemoryMib(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: int | core.IntOut | None = None,
        min: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=AcceleratorTotalMemoryMib.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut | None = core.arg(default=None)

        min: int | core.IntOut | None = core.arg(default=None)


@core.schema
class MemoryGibPerVcpu(core.Schema):

    max: float | core.FloatOut | None = core.attr(float, default=None)

    min: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        max: float | core.FloatOut | None = None,
        min: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=MemoryGibPerVcpu.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: float | core.FloatOut | None = core.arg(default=None)

        min: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class NetworkInterfaceCount(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: int | core.IntOut | None = None,
        min: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NetworkInterfaceCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: int | core.IntOut | None = core.arg(default=None)

        min: int | core.IntOut | None = core.arg(default=None)


@core.schema
class InstanceRequirements(core.Schema):

    accelerator_count: AcceleratorCount | None = core.attr(AcceleratorCount, default=None)

    accelerator_manufacturers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    accelerator_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    accelerator_total_memory_mib: AcceleratorTotalMemoryMib | None = core.attr(
        AcceleratorTotalMemoryMib, default=None
    )

    accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    bare_metal: str | core.StringOut | None = core.attr(str, default=None)

    baseline_ebs_bandwidth_mbps: BaselineEbsBandwidthMbps | None = core.attr(
        BaselineEbsBandwidthMbps, default=None
    )

    burstable_performance: str | core.StringOut | None = core.attr(str, default=None)

    cpu_manufacturers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    excluded_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    instance_generations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    local_storage: str | core.StringOut | None = core.attr(str, default=None)

    local_storage_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    memory_gib_per_vcpu: MemoryGibPerVcpu | None = core.attr(MemoryGibPerVcpu, default=None)

    memory_mib: MemoryMib = core.attr(MemoryMib)

    network_interface_count: NetworkInterfaceCount | None = core.attr(
        NetworkInterfaceCount, default=None
    )

    on_demand_max_price_percentage_over_lowest_price: int | core.IntOut | None = core.attr(
        int, default=None
    )

    require_hibernate_support: bool | core.BoolOut | None = core.attr(bool, default=None)

    spot_max_price_percentage_over_lowest_price: int | core.IntOut | None = core.attr(
        int, default=None
    )

    total_local_storage_gb: TotalLocalStorageGb | None = core.attr(
        TotalLocalStorageGb, default=None
    )

    vcpu_count: VcpuCount = core.attr(VcpuCount)

    def __init__(
        self,
        *,
        memory_mib: MemoryMib,
        vcpu_count: VcpuCount,
        accelerator_count: AcceleratorCount | None = None,
        accelerator_manufacturers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        accelerator_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        accelerator_total_memory_mib: AcceleratorTotalMemoryMib | None = None,
        accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        bare_metal: str | core.StringOut | None = None,
        baseline_ebs_bandwidth_mbps: BaselineEbsBandwidthMbps | None = None,
        burstable_performance: str | core.StringOut | None = None,
        cpu_manufacturers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        excluded_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        instance_generations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        local_storage: str | core.StringOut | None = None,
        local_storage_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        memory_gib_per_vcpu: MemoryGibPerVcpu | None = None,
        network_interface_count: NetworkInterfaceCount | None = None,
        on_demand_max_price_percentage_over_lowest_price: int | core.IntOut | None = None,
        require_hibernate_support: bool | core.BoolOut | None = None,
        spot_max_price_percentage_over_lowest_price: int | core.IntOut | None = None,
        total_local_storage_gb: TotalLocalStorageGb | None = None,
    ):
        super().__init__(
            args=InstanceRequirements.Args(
                memory_mib=memory_mib,
                vcpu_count=vcpu_count,
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
                network_interface_count=network_interface_count,
                on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
                require_hibernate_support=require_hibernate_support,
                spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
                total_local_storage_gb=total_local_storage_gb,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accelerator_count: AcceleratorCount | None = core.arg(default=None)

        accelerator_manufacturers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        accelerator_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        accelerator_total_memory_mib: AcceleratorTotalMemoryMib | None = core.arg(default=None)

        accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        bare_metal: str | core.StringOut | None = core.arg(default=None)

        baseline_ebs_bandwidth_mbps: BaselineEbsBandwidthMbps | None = core.arg(default=None)

        burstable_performance: str | core.StringOut | None = core.arg(default=None)

        cpu_manufacturers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        excluded_instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        instance_generations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        local_storage: str | core.StringOut | None = core.arg(default=None)

        local_storage_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        memory_gib_per_vcpu: MemoryGibPerVcpu | None = core.arg(default=None)

        memory_mib: MemoryMib = core.arg()

        network_interface_count: NetworkInterfaceCount | None = core.arg(default=None)

        on_demand_max_price_percentage_over_lowest_price: int | core.IntOut | None = core.arg(
            default=None
        )

        require_hibernate_support: bool | core.BoolOut | None = core.arg(default=None)

        spot_max_price_percentage_over_lowest_price: int | core.IntOut | None = core.arg(
            default=None
        )

        total_local_storage_gb: TotalLocalStorageGb | None = core.arg(default=None)

        vcpu_count: VcpuCount = core.arg()


@core.schema
class ElasticInferenceAccelerator(core.Schema):

    type: str | core.StringOut = core.attr(str)

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
class CapacityReservationTarget(core.Schema):

    capacity_reservation_id: str | core.StringOut | None = core.attr(str, default=None)

    capacity_reservation_resource_group_arn: str | core.StringOut | None = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        capacity_reservation_id: str | core.StringOut | None = None,
        capacity_reservation_resource_group_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CapacityReservationTarget.Args(
                capacity_reservation_id=capacity_reservation_id,
                capacity_reservation_resource_group_arn=capacity_reservation_resource_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_id: str | core.StringOut | None = core.arg(default=None)

        capacity_reservation_resource_group_arn: str | core.StringOut | None = core.arg(
            default=None
        )


@core.schema
class CapacityReservationSpecification(core.Schema):

    capacity_reservation_preference: str | core.StringOut | None = core.attr(str, default=None)

    capacity_reservation_target: CapacityReservationTarget | None = core.attr(
        CapacityReservationTarget, default=None
    )

    def __init__(
        self,
        *,
        capacity_reservation_preference: str | core.StringOut | None = None,
        capacity_reservation_target: CapacityReservationTarget | None = None,
    ):
        super().__init__(
            args=CapacityReservationSpecification.Args(
                capacity_reservation_preference=capacity_reservation_preference,
                capacity_reservation_target=capacity_reservation_target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_preference: str | core.StringOut | None = core.arg(default=None)

        capacity_reservation_target: CapacityReservationTarget | None = core.arg(default=None)


@core.schema
class HibernationOptions(core.Schema):

    configured: bool | core.BoolOut = core.attr(bool)

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
class LicenseSpecification(core.Schema):

    license_configuration_arn: str | core.StringOut = core.attr(str)

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
class TagSpecifications(core.Schema):

    resource_type: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        resource_type: str | core.StringOut | None = None,
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
        resource_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


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
class Monitoring(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Monitoring.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    http_protocol_ipv6: str | core.StringOut | None = core.attr(str, default=None)

    http_put_response_hop_limit: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    http_tokens: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    instance_metadata_tags: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut | None = None,
        http_protocol_ipv6: str | core.StringOut | None = None,
        http_put_response_hop_limit: int | core.IntOut | None = None,
        http_tokens: str | core.StringOut | None = None,
        instance_metadata_tags: str | core.StringOut | None = None,
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
        http_endpoint: str | core.StringOut | None = core.arg(default=None)

        http_protocol_ipv6: str | core.StringOut | None = core.arg(default=None)

        http_put_response_hop_limit: int | core.IntOut | None = core.arg(default=None)

        http_tokens: str | core.StringOut | None = core.arg(default=None)

        instance_metadata_tags: str | core.StringOut | None = core.arg(default=None)


@core.schema
class IamInstanceProfile(core.Schema):

    arn: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IamInstanceProfile.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NetworkInterfaces(core.Schema):

    associate_carrier_ip_address: str | core.StringOut | None = core.attr(str, default=None)

    associate_public_ip_address: str | core.StringOut | None = core.attr(str, default=None)

    delete_on_termination: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    device_index: int | core.IntOut | None = core.attr(int, default=None)

    interface_type: str | core.StringOut | None = core.attr(str, default=None)

    ipv4_address_count: int | core.IntOut | None = core.attr(int, default=None)

    ipv4_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ipv4_prefix_count: int | core.IntOut | None = core.attr(int, default=None)

    ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ipv6_address_count: int | core.IntOut | None = core.attr(int, default=None)

    ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ipv6_prefix_count: int | core.IntOut | None = core.attr(int, default=None)

    ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    network_card_index: int | core.IntOut | None = core.attr(int, default=None)

    network_interface_id: str | core.StringOut | None = core.attr(str, default=None)

    private_ip_address: str | core.StringOut | None = core.attr(str, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        associate_carrier_ip_address: str | core.StringOut | None = None,
        associate_public_ip_address: str | core.StringOut | None = None,
        delete_on_termination: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        device_index: int | core.IntOut | None = None,
        interface_type: str | core.StringOut | None = None,
        ipv4_address_count: int | core.IntOut | None = None,
        ipv4_addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ipv4_prefix_count: int | core.IntOut | None = None,
        ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ipv6_address_count: int | core.IntOut | None = None,
        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ipv6_prefix_count: int | core.IntOut | None = None,
        ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        network_card_index: int | core.IntOut | None = None,
        network_interface_id: str | core.StringOut | None = None,
        private_ip_address: str | core.StringOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_id: str | core.StringOut | None = None,
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
        associate_carrier_ip_address: str | core.StringOut | None = core.arg(default=None)

        associate_public_ip_address: str | core.StringOut | None = core.arg(default=None)

        delete_on_termination: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        device_index: int | core.IntOut | None = core.arg(default=None)

        interface_type: str | core.StringOut | None = core.arg(default=None)

        ipv4_address_count: int | core.IntOut | None = core.arg(default=None)

        ipv4_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipv4_prefix_count: int | core.IntOut | None = core.arg(default=None)

        ipv4_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipv6_address_count: int | core.IntOut | None = core.arg(default=None)

        ipv6_addresses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        ipv6_prefix_count: int | core.IntOut | None = core.arg(default=None)

        ipv6_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        network_card_index: int | core.IntOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut | None = core.arg(default=None)

        private_ip_address: str | core.StringOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CpuOptions(core.Schema):

    core_count: int | core.IntOut | None = core.attr(int, default=None)

    threads_per_core: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        core_count: int | core.IntOut | None = None,
        threads_per_core: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CpuOptions.Args(
                core_count=core_count,
                threads_per_core=threads_per_core,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        core_count: int | core.IntOut | None = core.arg(default=None)

        threads_per_core: int | core.IntOut | None = core.arg(default=None)


@core.schema
class EnclaveOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=EnclaveOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class CreditSpecification(core.Schema):

    cpu_credits: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu_credits: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CreditSpecification.Args(
                cpu_credits=cpu_credits,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_credits: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_launch_template", namespace="ec2")
class LaunchTemplate(core.Resource):
    """
    The Amazon Resource Name (ARN) of the instance profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specify volumes to attach to the instance besides the volumes specified by the AMI.
    """
    block_device_mappings: list[BlockDeviceMappings] | core.ArrayOut[
        BlockDeviceMappings
    ] | None = core.attr(BlockDeviceMappings, default=None, kind=core.Kind.array)

    """
    (Optional) Targeting for EC2 capacity reservations. See [Capacity Reservation Specification](#capaci
    ty-reservation-specification) below for more details.
    """
    capacity_reservation_specification: CapacityReservationSpecification | None = core.attr(
        CapacityReservationSpecification, default=None
    )

    """
    (Optional) The CPU options for the instance. See [CPU Options](#cpu-options) below for more details.
    """
    cpu_options: CpuOptions | None = core.attr(CpuOptions, default=None)

    """
    (Optional) Customize the credit specification of the instance. See [Credit
    """
    credit_specification: CreditSpecification | None = core.attr(CreditSpecification, default=None)

    """
    (Optional) Default Version of the launch template.
    """
    default_version: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Description of the launch template.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If true, enables [EC2 Instance Stop Protection](https://docs.aws.amazon.com/AWSEC2/latest
    /UserGuide/Stop_Start.html#Using_StopProtection).
    """
    disable_api_stop: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If `true`, enables [EC2 Instance
    """
    disable_api_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If `true`, the launched EC2 instance will be EBS-optimized.
    """
    ebs_optimized: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The elastic GPU to attach to the instance. See [Elastic GPU](#elastic-gpu)
    """
    elastic_gpu_specifications: list[ElasticGpuSpecifications] | core.ArrayOut[
        ElasticGpuSpecifications
    ] | None = core.attr(ElasticGpuSpecifications, default=None, kind=core.Kind.array)

    """
    (Optional) Configuration block containing an Elastic Inference Accelerator to attach to the instance
    . See [Elastic Inference Accelerator](#elastic-inference-accelerator) below for more details.
    """
    elastic_inference_accelerator: ElasticInferenceAccelerator | None = core.attr(
        ElasticInferenceAccelerator, default=None
    )

    """
    (Optional) Enable Nitro Enclaves on launched instances. See [Enclave Options](#enclave-options) belo
    w for more details.
    """
    enclave_options: EnclaveOptions | None = core.attr(EnclaveOptions, default=None)

    """
    (Optional) The hibernation options for the instance. See [Hibernation Options](#hibernation-options)
    below for more details.
    """
    hibernation_options: HibernationOptions | None = core.attr(HibernationOptions, default=None)

    """
    (Optional) The IAM Instance Profile to launch the instance with. See [Instance Profile](#instance-pr
    ofile)
    """
    iam_instance_profile: IamInstanceProfile | None = core.attr(IamInstanceProfile, default=None)

    """
    The ID of the launch template.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The AMI from which to launch the instance.
    """
    image_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Shutdown behavior for the instance. Can be `stop` or `terminate`.
    """
    instance_initiated_shutdown_behavior: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The market (purchasing) option for the instance. See [Market Options](#market-options)
    """
    instance_market_options: InstanceMarketOptions | None = core.attr(
        InstanceMarketOptions, default=None
    )

    """
    (Optional) The attribute requirements for the type of instance. If present then `instance_type` cann
    ot be present.
    """
    instance_requirements: InstanceRequirements | None = core.attr(
        InstanceRequirements, default=None
    )

    """
    (Optional) The type of the instance. If present then `instance_requirements` cannot be present.
    """
    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The kernel ID.
    """
    kernel_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The key name to use for the instance.
    """
    key_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The latest version of the launch template.
    """
    latest_version: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) A list of license specifications to associate with. See [License Specification](#license-
    specification) below for more details.
    """
    license_specification: list[LicenseSpecification] | core.ArrayOut[
        LicenseSpecification
    ] | None = core.attr(LicenseSpecification, default=None, kind=core.Kind.array)

    """
    (Optional) The maintenance options for the instance. See [Maintenance Options](#maintenance-options)
    below for more details.
    """
    maintenance_options: MaintenanceOptions | None = core.attr(MaintenanceOptions, default=None)

    """
    (Optional) Customize the metadata options for the instance. See [Metadata Options](#metadata-options
    ) below for more details.
    """
    metadata_options: MetadataOptions | None = core.attr(
        MetadataOptions, default=None, computed=True
    )

    """
    (Optional) The monitoring option for the instance. See [Monitoring](#monitoring) below for more deta
    ils.
    """
    monitoring: Monitoring | None = core.attr(Monitoring, default=None)

    """
    (Optional) The name of the launch template. If you leave this blank, Terraform will auto-generate a
    unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Customize network interfaces to be attached at instance boot time. See [Network
    """
    network_interfaces: list[NetworkInterfaces] | core.ArrayOut[
        NetworkInterfaces
    ] | None = core.attr(NetworkInterfaces, default=None, kind=core.Kind.array)

    """
    (Optional) The placement of the instance. See [Placement](#placement) below for more details.
    """
    placement: Placement | None = core.attr(Placement, default=None)

    """
    (Optional) The options for the instance hostname. The default values are inherited from the subnet.
    See [Private DNS Name Options](#private-dns-name-options) below for more details.
    """
    private_dns_name_options: PrivateDnsNameOptions | None = core.attr(
        PrivateDnsNameOptions, default=None
    )

    """
    (Optional) The ID of the RAM disk.
    """
    ram_disk_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of security group names to associate with. If you are creating Instances in a VPC,
    use
    """
    security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The tags to apply to the resources during launch. See [Tag Specifications](#tag-specifica
    tions) below for more details.
    """
    tag_specifications: list[TagSpecifications] | core.ArrayOut[
        TagSpecifications
    ] | None = core.attr(TagSpecifications, default=None, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the launch template. If configured with a provider [`default_t
    ags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_
    tags-configuration-block) present, tags with matching keys will overwrite those defined at the provi
    der-level.
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
    (Optional) Whether to update Default Version each update. Conflicts with `default_version`.
    """
    update_default_version: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The base64-encoded user data to provide when launching the instance.
    """
    user_data: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of security group IDs to associate with. Conflicts with `network_interfaces.securi
    ty_groups`
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        block_device_mappings: list[BlockDeviceMappings]
        | core.ArrayOut[BlockDeviceMappings]
        | None = None,
        capacity_reservation_specification: CapacityReservationSpecification | None = None,
        cpu_options: CpuOptions | None = None,
        credit_specification: CreditSpecification | None = None,
        default_version: int | core.IntOut | None = None,
        description: str | core.StringOut | None = None,
        disable_api_stop: bool | core.BoolOut | None = None,
        disable_api_termination: bool | core.BoolOut | None = None,
        ebs_optimized: str | core.StringOut | None = None,
        elastic_gpu_specifications: list[ElasticGpuSpecifications]
        | core.ArrayOut[ElasticGpuSpecifications]
        | None = None,
        elastic_inference_accelerator: ElasticInferenceAccelerator | None = None,
        enclave_options: EnclaveOptions | None = None,
        hibernation_options: HibernationOptions | None = None,
        iam_instance_profile: IamInstanceProfile | None = None,
        image_id: str | core.StringOut | None = None,
        instance_initiated_shutdown_behavior: str | core.StringOut | None = None,
        instance_market_options: InstanceMarketOptions | None = None,
        instance_requirements: InstanceRequirements | None = None,
        instance_type: str | core.StringOut | None = None,
        kernel_id: str | core.StringOut | None = None,
        key_name: str | core.StringOut | None = None,
        license_specification: list[LicenseSpecification]
        | core.ArrayOut[LicenseSpecification]
        | None = None,
        maintenance_options: MaintenanceOptions | None = None,
        metadata_options: MetadataOptions | None = None,
        monitoring: Monitoring | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        network_interfaces: list[NetworkInterfaces]
        | core.ArrayOut[NetworkInterfaces]
        | None = None,
        placement: Placement | None = None,
        private_dns_name_options: PrivateDnsNameOptions | None = None,
        ram_disk_id: str | core.StringOut | None = None,
        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tag_specifications: list[TagSpecifications]
        | core.ArrayOut[TagSpecifications]
        | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        update_default_version: bool | core.BoolOut | None = None,
        user_data: str | core.StringOut | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LaunchTemplate.Args(
                block_device_mappings=block_device_mappings,
                capacity_reservation_specification=capacity_reservation_specification,
                cpu_options=cpu_options,
                credit_specification=credit_specification,
                default_version=default_version,
                description=description,
                disable_api_stop=disable_api_stop,
                disable_api_termination=disable_api_termination,
                ebs_optimized=ebs_optimized,
                elastic_gpu_specifications=elastic_gpu_specifications,
                elastic_inference_accelerator=elastic_inference_accelerator,
                enclave_options=enclave_options,
                hibernation_options=hibernation_options,
                iam_instance_profile=iam_instance_profile,
                image_id=image_id,
                instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
                instance_market_options=instance_market_options,
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                kernel_id=kernel_id,
                key_name=key_name,
                license_specification=license_specification,
                maintenance_options=maintenance_options,
                metadata_options=metadata_options,
                monitoring=monitoring,
                name=name,
                name_prefix=name_prefix,
                network_interfaces=network_interfaces,
                placement=placement,
                private_dns_name_options=private_dns_name_options,
                ram_disk_id=ram_disk_id,
                security_group_names=security_group_names,
                tag_specifications=tag_specifications,
                tags=tags,
                tags_all=tags_all,
                update_default_version=update_default_version,
                user_data=user_data,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_device_mappings: list[BlockDeviceMappings] | core.ArrayOut[
            BlockDeviceMappings
        ] | None = core.arg(default=None)

        capacity_reservation_specification: CapacityReservationSpecification | None = core.arg(
            default=None
        )

        cpu_options: CpuOptions | None = core.arg(default=None)

        credit_specification: CreditSpecification | None = core.arg(default=None)

        default_version: int | core.IntOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disable_api_stop: bool | core.BoolOut | None = core.arg(default=None)

        disable_api_termination: bool | core.BoolOut | None = core.arg(default=None)

        ebs_optimized: str | core.StringOut | None = core.arg(default=None)

        elastic_gpu_specifications: list[ElasticGpuSpecifications] | core.ArrayOut[
            ElasticGpuSpecifications
        ] | None = core.arg(default=None)

        elastic_inference_accelerator: ElasticInferenceAccelerator | None = core.arg(default=None)

        enclave_options: EnclaveOptions | None = core.arg(default=None)

        hibernation_options: HibernationOptions | None = core.arg(default=None)

        iam_instance_profile: IamInstanceProfile | None = core.arg(default=None)

        image_id: str | core.StringOut | None = core.arg(default=None)

        instance_initiated_shutdown_behavior: str | core.StringOut | None = core.arg(default=None)

        instance_market_options: InstanceMarketOptions | None = core.arg(default=None)

        instance_requirements: InstanceRequirements | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        kernel_id: str | core.StringOut | None = core.arg(default=None)

        key_name: str | core.StringOut | None = core.arg(default=None)

        license_specification: list[LicenseSpecification] | core.ArrayOut[
            LicenseSpecification
        ] | None = core.arg(default=None)

        maintenance_options: MaintenanceOptions | None = core.arg(default=None)

        metadata_options: MetadataOptions | None = core.arg(default=None)

        monitoring: Monitoring | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        network_interfaces: list[NetworkInterfaces] | core.ArrayOut[
            NetworkInterfaces
        ] | None = core.arg(default=None)

        placement: Placement | None = core.arg(default=None)

        private_dns_name_options: PrivateDnsNameOptions | None = core.arg(default=None)

        ram_disk_id: str | core.StringOut | None = core.arg(default=None)

        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tag_specifications: list[TagSpecifications] | core.ArrayOut[
            TagSpecifications
        ] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        update_default_version: bool | core.BoolOut | None = core.arg(default=None)

        user_data: str | core.StringOut | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
