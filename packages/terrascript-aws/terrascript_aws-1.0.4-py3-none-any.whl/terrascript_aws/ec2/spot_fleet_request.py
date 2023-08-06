import terrascript.core as core


@core.schema
class CapacityRebalance(core.Schema):

    replacement_strategy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        replacement_strategy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CapacityRebalance.Args(
                replacement_strategy=replacement_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replacement_strategy: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SpotMaintenanceStrategies(core.Schema):

    capacity_rebalance: CapacityRebalance | None = core.attr(CapacityRebalance, default=None)

    def __init__(
        self,
        *,
        capacity_rebalance: CapacityRebalance | None = None,
    ):
        super().__init__(
            args=SpotMaintenanceStrategies.Args(
                capacity_rebalance=capacity_rebalance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_rebalance: CapacityRebalance | None = core.arg(default=None)


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_name: str | core.StringOut = core.attr(str)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        delete_on_termination: bool | core.BoolOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
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
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: str | core.StringOut = core.attr(str)

    virtual_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        virtual_name: str | core.StringOut,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        virtual_name: str | core.StringOut = core.arg()


@core.schema
class LaunchSpecification(core.Schema):

    ami: str | core.StringOut = core.attr(str)

    associate_public_ip_address: bool | core.BoolOut | None = core.attr(bool, default=None)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None)

    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    iam_instance_profile: str | core.StringOut | None = core.attr(str, default=None)

    iam_instance_profile_arn: str | core.StringOut | None = core.attr(str, default=None)

    instance_type: str | core.StringOut = core.attr(str)

    key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    monitoring: bool | core.BoolOut | None = core.attr(bool, default=None)

    placement_group: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    placement_tenancy: str | core.StringOut | None = core.attr(str, default=None)

    root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] | None = core.attr(
        RootBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    spot_price: str | core.StringOut | None = core.attr(str, default=None)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    user_data: str | core.StringOut | None = core.attr(str, default=None)

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    weighted_capacity: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        ami: str | core.StringOut,
        instance_type: str | core.StringOut,
        associate_public_ip_address: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = None,
        ebs_optimized: bool | core.BoolOut | None = None,
        ephemeral_block_device: list[EphemeralBlockDevice]
        | core.ArrayOut[EphemeralBlockDevice]
        | None = None,
        iam_instance_profile: str | core.StringOut | None = None,
        iam_instance_profile_arn: str | core.StringOut | None = None,
        key_name: str | core.StringOut | None = None,
        monitoring: bool | core.BoolOut | None = None,
        placement_group: str | core.StringOut | None = None,
        placement_tenancy: str | core.StringOut | None = None,
        root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] | None = None,
        spot_price: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_data: str | core.StringOut | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        weighted_capacity: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchSpecification.Args(
                ami=ami,
                instance_type=instance_type,
                associate_public_ip_address=associate_public_ip_address,
                availability_zone=availability_zone,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                ephemeral_block_device=ephemeral_block_device,
                iam_instance_profile=iam_instance_profile,
                iam_instance_profile_arn=iam_instance_profile_arn,
                key_name=key_name,
                monitoring=monitoring,
                placement_group=placement_group,
                placement_tenancy=placement_tenancy,
                root_block_device=root_block_device,
                spot_price=spot_price,
                subnet_id=subnet_id,
                tags=tags,
                user_data=user_data,
                vpc_security_group_ids=vpc_security_group_ids,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami: str | core.StringOut = core.arg()

        associate_public_ip_address: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.arg(
            default=None
        )

        ebs_optimized: bool | core.BoolOut | None = core.arg(default=None)

        ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
            EphemeralBlockDevice
        ] | None = core.arg(default=None)

        iam_instance_profile: str | core.StringOut | None = core.arg(default=None)

        iam_instance_profile_arn: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        key_name: str | core.StringOut | None = core.arg(default=None)

        monitoring: bool | core.BoolOut | None = core.arg(default=None)

        placement_group: str | core.StringOut | None = core.arg(default=None)

        placement_tenancy: str | core.StringOut | None = core.arg(default=None)

        root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] | None = core.arg(
            default=None
        )

        spot_price: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_data: str | core.StringOut | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        weighted_capacity: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LaunchTemplateSpecification(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplateSpecification.Args(
                id=id,
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class VcpuCount(core.Schema):

    max: int | core.IntOut | None = core.attr(int, default=None)

    min: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: int | core.IntOut | None = None,
        min: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=VcpuCount.Args(
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

    min: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: int | core.IntOut | None = None,
        min: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=MemoryMib.Args(
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

    memory_mib: MemoryMib | None = core.attr(MemoryMib, default=None)

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

    vcpu_count: VcpuCount | None = core.attr(VcpuCount, default=None)

    def __init__(
        self,
        *,
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
        memory_mib: MemoryMib | None = None,
        network_interface_count: NetworkInterfaceCount | None = None,
        on_demand_max_price_percentage_over_lowest_price: int | core.IntOut | None = None,
        require_hibernate_support: bool | core.BoolOut | None = None,
        spot_max_price_percentage_over_lowest_price: int | core.IntOut | None = None,
        total_local_storage_gb: TotalLocalStorageGb | None = None,
        vcpu_count: VcpuCount | None = None,
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

        memory_mib: MemoryMib | None = core.arg(default=None)

        network_interface_count: NetworkInterfaceCount | None = core.arg(default=None)

        on_demand_max_price_percentage_over_lowest_price: int | core.IntOut | None = core.arg(
            default=None
        )

        require_hibernate_support: bool | core.BoolOut | None = core.arg(default=None)

        spot_max_price_percentage_over_lowest_price: int | core.IntOut | None = core.arg(
            default=None
        )

        total_local_storage_gb: TotalLocalStorageGb | None = core.arg(default=None)

        vcpu_count: VcpuCount | None = core.arg(default=None)


@core.schema
class Overrides(core.Schema):

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    instance_requirements: InstanceRequirements | None = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    priority: float | core.FloatOut | None = core.attr(float, default=None, computed=True)

    spot_price: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    weighted_capacity: float | core.FloatOut | None = core.attr(float, default=None, computed=True)

    def __init__(
        self,
        *,
        availability_zone: str | core.StringOut | None = None,
        instance_requirements: InstanceRequirements | None = None,
        instance_type: str | core.StringOut | None = None,
        priority: float | core.FloatOut | None = None,
        spot_price: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        weighted_capacity: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=Overrides.Args(
                availability_zone=availability_zone,
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                priority=priority,
                spot_price=spot_price,
                subnet_id=subnet_id,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        instance_requirements: InstanceRequirements | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        priority: float | core.FloatOut | None = core.arg(default=None)

        spot_price: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        weighted_capacity: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class LaunchTemplateConfig(core.Schema):

    launch_template_specification: LaunchTemplateSpecification = core.attr(
        LaunchTemplateSpecification
    )

    overrides: list[Overrides] | core.ArrayOut[Overrides] | None = core.attr(
        Overrides, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        launch_template_specification: LaunchTemplateSpecification,
        overrides: list[Overrides] | core.ArrayOut[Overrides] | None = None,
    ):
        super().__init__(
            args=LaunchTemplateConfig.Args(
                launch_template_specification=launch_template_specification,
                overrides=overrides,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_specification: LaunchTemplateSpecification = core.arg()

        overrides: list[Overrides] | core.ArrayOut[Overrides] | None = core.arg(default=None)


@core.resource(type="aws_spot_fleet_request", namespace="ec2")
class SpotFleetRequest(core.Resource):
    """
    Indicates how to allocate the target capacity across
    """

    allocation_strategy: str | core.StringOut | None = core.attr(str, default=None)

    client_token: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether running Spot
    """
    excess_capacity_termination_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The type of fleet request. Indicates whether the Spot Fleet only requests the target
    """
    fleet_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Grants the Spot fleet permission to terminate
    """
    iam_fleet_role: str | core.StringOut = core.attr(str)

    """
    The ID of the launch template. Conflicts with `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates whether a Spot
    """
    instance_interruption_behaviour: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional; Default: 1)
    """
    instance_pools_to_use_count: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Used to define the launch configuration of the
    """
    launch_specification: list[LaunchSpecification] | core.ArrayOut[
        LaunchSpecification
    ] | None = core.attr(LaunchSpecification, default=None, kind=core.Kind.array)

    """
    (Optional) Launch template configuration block. See [Launch Template Configs](#launch-template-confi
    gs) below for more details. Conflicts with `launch_specification`. At least one of `launch_specifica
    tion` or `launch_template_config` is required.
    """
    launch_template_config: list[LaunchTemplateConfig] | core.ArrayOut[
        LaunchTemplateConfig
    ] | None = core.attr(LaunchTemplateConfig, default=None, kind=core.Kind.array)

    load_balancers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The order of the launch template overrides to use in fulfilling On-Demand capacity. the possible val
    ues are: `lowestPrice` and `prioritized`. the default is `lowestPrice`.
    """
    on_demand_allocation_strategy: str | core.StringOut | None = core.attr(str, default=None)

    """
    The maximum amount per hour for On-Demand Instances that you're willing to pay. When the maximum amo
    unt you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the
    target capacity.
    """
    on_demand_max_total_price: str | core.StringOut | None = core.attr(str, default=None)

    """
    The number of On-Demand units to request. If the request type is `maintain`, you can specify a targe
    t capacity of 0 and add capacity later.
    """
    on_demand_target_capacity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Indicates whether Spot fleet should replace unhealthy instances. Default `false`.
    """
    replace_unhealthy_instances: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Nested argument containing maintenance strategies for managing your Spot Instances that a
    re at an elevated risk of being interrupted. Defined below.
    """
    spot_maintenance_strategies: SpotMaintenanceStrategies | None = core.attr(
        SpotMaintenanceStrategies, default=None
    )

    """
    (Optional; Default: On-demand price) The maximum bid price per unit hour.
    """
    spot_price: str | core.StringOut | None = core.attr(str, default=None)

    """
    The state of the Spot fleet request.
    """
    spot_request_state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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
    The number of units to request. You can choose to set the
    """
    target_capacity: int | core.IntOut = core.attr(int)

    target_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Indicates whether running Spot
    """
    terminate_instances_on_delete: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether running Spot
    """
    terminate_instances_with_expiration: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3
    339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the r
    equest immediately.
    """
    valid_from: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc333
    9#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance reques
    ts are placed or enabled to fulfill the request.
    """
    valid_until: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional; Default: false) If set, Terraform will
    """
    wait_for_fulfillment: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        iam_fleet_role: str | core.StringOut,
        target_capacity: int | core.IntOut,
        allocation_strategy: str | core.StringOut | None = None,
        excess_capacity_termination_policy: str | core.StringOut | None = None,
        fleet_type: str | core.StringOut | None = None,
        instance_interruption_behaviour: str | core.StringOut | None = None,
        instance_pools_to_use_count: int | core.IntOut | None = None,
        launch_specification: list[LaunchSpecification]
        | core.ArrayOut[LaunchSpecification]
        | None = None,
        launch_template_config: list[LaunchTemplateConfig]
        | core.ArrayOut[LaunchTemplateConfig]
        | None = None,
        load_balancers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        on_demand_allocation_strategy: str | core.StringOut | None = None,
        on_demand_max_total_price: str | core.StringOut | None = None,
        on_demand_target_capacity: int | core.IntOut | None = None,
        replace_unhealthy_instances: bool | core.BoolOut | None = None,
        spot_maintenance_strategies: SpotMaintenanceStrategies | None = None,
        spot_price: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        terminate_instances_on_delete: str | core.StringOut | None = None,
        terminate_instances_with_expiration: bool | core.BoolOut | None = None,
        valid_from: str | core.StringOut | None = None,
        valid_until: str | core.StringOut | None = None,
        wait_for_fulfillment: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SpotFleetRequest.Args(
                iam_fleet_role=iam_fleet_role,
                target_capacity=target_capacity,
                allocation_strategy=allocation_strategy,
                excess_capacity_termination_policy=excess_capacity_termination_policy,
                fleet_type=fleet_type,
                instance_interruption_behaviour=instance_interruption_behaviour,
                instance_pools_to_use_count=instance_pools_to_use_count,
                launch_specification=launch_specification,
                launch_template_config=launch_template_config,
                load_balancers=load_balancers,
                on_demand_allocation_strategy=on_demand_allocation_strategy,
                on_demand_max_total_price=on_demand_max_total_price,
                on_demand_target_capacity=on_demand_target_capacity,
                replace_unhealthy_instances=replace_unhealthy_instances,
                spot_maintenance_strategies=spot_maintenance_strategies,
                spot_price=spot_price,
                tags=tags,
                tags_all=tags_all,
                target_group_arns=target_group_arns,
                terminate_instances_on_delete=terminate_instances_on_delete,
                terminate_instances_with_expiration=terminate_instances_with_expiration,
                valid_from=valid_from,
                valid_until=valid_until,
                wait_for_fulfillment=wait_for_fulfillment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocation_strategy: str | core.StringOut | None = core.arg(default=None)

        excess_capacity_termination_policy: str | core.StringOut | None = core.arg(default=None)

        fleet_type: str | core.StringOut | None = core.arg(default=None)

        iam_fleet_role: str | core.StringOut = core.arg()

        instance_interruption_behaviour: str | core.StringOut | None = core.arg(default=None)

        instance_pools_to_use_count: int | core.IntOut | None = core.arg(default=None)

        launch_specification: list[LaunchSpecification] | core.ArrayOut[
            LaunchSpecification
        ] | None = core.arg(default=None)

        launch_template_config: list[LaunchTemplateConfig] | core.ArrayOut[
            LaunchTemplateConfig
        ] | None = core.arg(default=None)

        load_balancers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        on_demand_allocation_strategy: str | core.StringOut | None = core.arg(default=None)

        on_demand_max_total_price: str | core.StringOut | None = core.arg(default=None)

        on_demand_target_capacity: int | core.IntOut | None = core.arg(default=None)

        replace_unhealthy_instances: bool | core.BoolOut | None = core.arg(default=None)

        spot_maintenance_strategies: SpotMaintenanceStrategies | None = core.arg(default=None)

        spot_price: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_capacity: int | core.IntOut = core.arg()

        target_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        terminate_instances_on_delete: str | core.StringOut | None = core.arg(default=None)

        terminate_instances_with_expiration: bool | core.BoolOut | None = core.arg(default=None)

        valid_from: str | core.StringOut | None = core.arg(default=None)

        valid_until: str | core.StringOut | None = core.arg(default=None)

        wait_for_fulfillment: bool | core.BoolOut | None = core.arg(default=None)
