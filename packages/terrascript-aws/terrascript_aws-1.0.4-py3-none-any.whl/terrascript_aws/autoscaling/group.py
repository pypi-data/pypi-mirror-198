import terrascript.core as core


@core.schema
class Preferences(core.Schema):

    checkpoint_delay: str | core.StringOut | None = core.attr(str, default=None)

    checkpoint_percentages: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    instance_warmup: str | core.StringOut | None = core.attr(str, default=None)

    min_healthy_percentage: int | core.IntOut | None = core.attr(int, default=None)

    skip_matching: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        checkpoint_delay: str | core.StringOut | None = None,
        checkpoint_percentages: list[int] | core.ArrayOut[core.IntOut] | None = None,
        instance_warmup: str | core.StringOut | None = None,
        min_healthy_percentage: int | core.IntOut | None = None,
        skip_matching: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Preferences.Args(
                checkpoint_delay=checkpoint_delay,
                checkpoint_percentages=checkpoint_percentages,
                instance_warmup=instance_warmup,
                min_healthy_percentage=min_healthy_percentage,
                skip_matching=skip_matching,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        checkpoint_delay: str | core.StringOut | None = core.arg(default=None)

        checkpoint_percentages: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(
            default=None
        )

        instance_warmup: str | core.StringOut | None = core.arg(default=None)

        min_healthy_percentage: int | core.IntOut | None = core.arg(default=None)

        skip_matching: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class InstanceRefresh(core.Schema):

    preferences: Preferences | None = core.attr(Preferences, default=None)

    strategy: str | core.StringOut = core.attr(str)

    triggers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        strategy: str | core.StringOut,
        preferences: Preferences | None = None,
        triggers: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=InstanceRefresh.Args(
                strategy=strategy,
                preferences=preferences,
                triggers=triggers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        preferences: Preferences | None = core.arg(default=None)

        strategy: str | core.StringOut = core.arg()

        triggers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Tag(core.Schema):

    key: str | core.StringOut = core.attr(str)

    propagate_at_launch: bool | core.BoolOut = core.attr(bool)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        propagate_at_launch: bool | core.BoolOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                propagate_at_launch=propagate_at_launch,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        propagate_at_launch: bool | core.BoolOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class InitialLifecycleHook(core.Schema):

    default_result: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    heartbeat_timeout: int | core.IntOut | None = core.attr(int, default=None)

    lifecycle_transition: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    notification_metadata: str | core.StringOut | None = core.attr(str, default=None)

    notification_target_arn: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        lifecycle_transition: str | core.StringOut,
        name: str | core.StringOut,
        default_result: str | core.StringOut | None = None,
        heartbeat_timeout: int | core.IntOut | None = None,
        notification_metadata: str | core.StringOut | None = None,
        notification_target_arn: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InitialLifecycleHook.Args(
                lifecycle_transition=lifecycle_transition,
                name=name,
                default_result=default_result,
                heartbeat_timeout=heartbeat_timeout,
                notification_metadata=notification_metadata,
                notification_target_arn=notification_target_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_result: str | core.StringOut | None = core.arg(default=None)

        heartbeat_timeout: int | core.IntOut | None = core.arg(default=None)

        lifecycle_transition: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        notification_metadata: str | core.StringOut | None = core.arg(default=None)

        notification_target_arn: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
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
class InstanceReusePolicy(core.Schema):

    reuse_on_scale_in: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        reuse_on_scale_in: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=InstanceReusePolicy.Args(
                reuse_on_scale_in=reuse_on_scale_in,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        reuse_on_scale_in: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class WarmPool(core.Schema):

    instance_reuse_policy: InstanceReusePolicy | None = core.attr(InstanceReusePolicy, default=None)

    max_group_prepared_capacity: int | core.IntOut | None = core.attr(int, default=None)

    min_size: int | core.IntOut | None = core.attr(int, default=None)

    pool_state: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_reuse_policy: InstanceReusePolicy | None = None,
        max_group_prepared_capacity: int | core.IntOut | None = None,
        min_size: int | core.IntOut | None = None,
        pool_state: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=WarmPool.Args(
                instance_reuse_policy=instance_reuse_policy,
                max_group_prepared_capacity=max_group_prepared_capacity,
                min_size=min_size,
                pool_state=pool_state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_reuse_policy: InstanceReusePolicy | None = core.arg(default=None)

        max_group_prepared_capacity: int | core.IntOut | None = core.arg(default=None)

        min_size: int | core.IntOut | None = core.arg(default=None)

        pool_state: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InstancesDistribution(core.Schema):

    on_demand_allocation_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    on_demand_base_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    on_demand_percentage_above_base_capacity: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    spot_allocation_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    spot_instance_pools: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    spot_max_price: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        on_demand_allocation_strategy: str | core.StringOut | None = None,
        on_demand_base_capacity: int | core.IntOut | None = None,
        on_demand_percentage_above_base_capacity: int | core.IntOut | None = None,
        spot_allocation_strategy: str | core.StringOut | None = None,
        spot_instance_pools: int | core.IntOut | None = None,
        spot_max_price: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InstancesDistribution.Args(
                on_demand_allocation_strategy=on_demand_allocation_strategy,
                on_demand_base_capacity=on_demand_base_capacity,
                on_demand_percentage_above_base_capacity=on_demand_percentage_above_base_capacity,
                spot_allocation_strategy=spot_allocation_strategy,
                spot_instance_pools=spot_instance_pools,
                spot_max_price=spot_max_price,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_demand_allocation_strategy: str | core.StringOut | None = core.arg(default=None)

        on_demand_base_capacity: int | core.IntOut | None = core.arg(default=None)

        on_demand_percentage_above_base_capacity: int | core.IntOut | None = core.arg(default=None)

        spot_allocation_strategy: str | core.StringOut | None = core.arg(default=None)

        spot_instance_pools: int | core.IntOut | None = core.arg(default=None)

        spot_max_price: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LaunchTemplateSpecification(core.Schema):

    launch_template_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    launch_template_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        launch_template_id: str | core.StringOut | None = None,
        launch_template_name: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplateSpecification.Args(
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: str | core.StringOut | None = core.arg(default=None)

        launch_template_name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)


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
class Override(core.Schema):

    instance_requirements: InstanceRequirements | None = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    launch_template_specification: LaunchTemplateSpecification | None = core.attr(
        LaunchTemplateSpecification, default=None
    )

    weighted_capacity: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_requirements: InstanceRequirements | None = None,
        instance_type: str | core.StringOut | None = None,
        launch_template_specification: LaunchTemplateSpecification | None = None,
        weighted_capacity: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Override.Args(
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                launch_template_specification=launch_template_specification,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_requirements: InstanceRequirements | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        launch_template_specification: LaunchTemplateSpecification | None = core.arg(default=None)

        weighted_capacity: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MixedInstancesPolicyLaunchTemplate(core.Schema):

    launch_template_specification: LaunchTemplateSpecification = core.attr(
        LaunchTemplateSpecification
    )

    override: list[Override] | core.ArrayOut[Override] | None = core.attr(
        Override, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        launch_template_specification: LaunchTemplateSpecification,
        override: list[Override] | core.ArrayOut[Override] | None = None,
    ):
        super().__init__(
            args=MixedInstancesPolicyLaunchTemplate.Args(
                launch_template_specification=launch_template_specification,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_specification: LaunchTemplateSpecification = core.arg()

        override: list[Override] | core.ArrayOut[Override] | None = core.arg(default=None)


@core.schema
class MixedInstancesPolicy(core.Schema):

    instances_distribution: InstancesDistribution | None = core.attr(
        InstancesDistribution, default=None, computed=True
    )

    launch_template: MixedInstancesPolicyLaunchTemplate = core.attr(
        MixedInstancesPolicyLaunchTemplate
    )

    def __init__(
        self,
        *,
        launch_template: MixedInstancesPolicyLaunchTemplate,
        instances_distribution: InstancesDistribution | None = None,
    ):
        super().__init__(
            args=MixedInstancesPolicy.Args(
                launch_template=launch_template,
                instances_distribution=instances_distribution,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instances_distribution: InstancesDistribution | None = core.arg(default=None)

        launch_template: MixedInstancesPolicyLaunchTemplate = core.arg()


@core.resource(type="aws_autoscaling_group", namespace="autoscaling")
class Group(core.Resource):
    """
    The ARN for this Auto Scaling Group
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of one or more availability zones for the group. Used for EC2-Classic, attaching a
    network interface via id from a launch template and default subnets when not specified with `vpc_zo
    ne_identifier` argument. Conflicts with `vpc_zone_identifier`.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Indicates whether capacity rebalance is enabled. Otherwise, capacity rebalance is disable
    d.
    """
    capacity_rebalance: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Reserved.
    """
    context: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The amount of time, in seconds, after a scaling activity completes before another scaling
    activity can start.
    """
    default_cooldown: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The amount of time, in seconds, until a newly launched instance can contribute to the Ama
    zon CloudWatch metrics. This delay lets an instance finish initializing before Amazon EC2 Auto Scali
    ng aggregates instance metrics, resulting in more reliable usage data. Set this value equal to the a
    mount of time that it takes for resource consumption to become stable after an instance reaches the
    InService state. (See [Set the default instance warmup for an Auto Scaling group](https://docs.aws.a
    mazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html))
    """
    default_instance_warmup: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The number of Amazon EC2 instances that
    """
    desired_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) A list of metrics to collect. The allowed values are defined by the [underlying AWS API](
    https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html).
    """
    enabled_metrics: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Allows deleting the Auto Scaling Group without waiting
    """
    force_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    force_delete_warm_pool: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Default: 300) Time (in seconds) after instance comes into service before checking health.
    """
    health_check_grace_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) "EC2" or "ELB". Controls how health checking is done.
    """
    health_check_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The ID of the launch template. Conflicts with `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more
    """
    initial_lifecycle_hook: list[InitialLifecycleHook] | core.ArrayOut[
        InitialLifecycleHook
    ] | None = core.attr(InitialLifecycleHook, default=None, kind=core.Kind.array)

    """
    (Optional) If this block is configured, start an
    """
    instance_refresh: InstanceRefresh | None = core.attr(InstanceRefresh, default=None)

    """
    (Optional) The name of the launch configuration to use.
    """
    launch_configuration: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Nested argument with Launch template specification to use to launch instances. See [Launc
    h Template](#launch_template) below for more details.
    """
    launch_template: LaunchTemplate | None = core.attr(LaunchTemplate, default=None)

    load_balancers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_instance_lifetime: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The maximum size of the Auto Scaling Group.
    """
    max_size: int | core.IntOut = core.attr(int)

    """
    (Optional) The granularity to associate with the metrics to collect. The only valid value is `1Minut
    e`. Default is `1Minute`.
    """
    metrics_granularity: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Setting this causes Terraform to wait for
    """
    min_elb_capacity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The minimum size of the Auto Scaling Group.
    """
    min_size: int | core.IntOut = core.attr(int)

    mixed_instances_policy: MixedInstancesPolicy | None = core.attr(
        MixedInstancesPolicy, default=None
    )

    """
    (Optional) The name of the Auto Scaling Group. By default generated by Terraform. Conflicts with `na
    me_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    placement_group: str | core.StringOut | None = core.attr(str, default=None)

    protect_from_scale_in: bool | core.BoolOut | None = core.attr(bool, default=None)

    service_linked_role_arn: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) A list of processes to suspend for the Auto Scaling Group. The allowed values are `Launch
    , `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledAct
    ions`, `AddToLoadBalancer`, `InstanceRefresh`.
    """
    suspended_processes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag: list[Tag] | core.ArrayOut[Tag] | None = core.attr(Tag, default=None, kind=core.Kind.array)

    tags: list[dict[str, str]] | core.MapArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map_array
    )

    target_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    termination_policies: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_zone_identifier: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    wait_for_capacity_timeout: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Setting this will cause Terraform to wait
    """
    wait_for_elb_capacity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) If this block is configured, add a [Warm Pool](https://docs.aws.amazon.com/autoscaling/ec
    2/userguide/ec2-auto-scaling-warm-pools.html)
    """
    warm_pool: WarmPool | None = core.attr(WarmPool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        max_size: int | core.IntOut,
        min_size: int | core.IntOut,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        capacity_rebalance: bool | core.BoolOut | None = None,
        context: str | core.StringOut | None = None,
        default_cooldown: int | core.IntOut | None = None,
        default_instance_warmup: int | core.IntOut | None = None,
        desired_capacity: int | core.IntOut | None = None,
        enabled_metrics: list[str] | core.ArrayOut[core.StringOut] | None = None,
        force_delete: bool | core.BoolOut | None = None,
        force_delete_warm_pool: bool | core.BoolOut | None = None,
        health_check_grace_period: int | core.IntOut | None = None,
        health_check_type: str | core.StringOut | None = None,
        initial_lifecycle_hook: list[InitialLifecycleHook]
        | core.ArrayOut[InitialLifecycleHook]
        | None = None,
        instance_refresh: InstanceRefresh | None = None,
        launch_configuration: str | core.StringOut | None = None,
        launch_template: LaunchTemplate | None = None,
        load_balancers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        max_instance_lifetime: int | core.IntOut | None = None,
        metrics_granularity: str | core.StringOut | None = None,
        min_elb_capacity: int | core.IntOut | None = None,
        mixed_instances_policy: MixedInstancesPolicy | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        placement_group: str | core.StringOut | None = None,
        protect_from_scale_in: bool | core.BoolOut | None = None,
        service_linked_role_arn: str | core.StringOut | None = None,
        suspended_processes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tag: list[Tag] | core.ArrayOut[Tag] | None = None,
        tags: list[dict[str, str]] | core.MapArrayOut[core.StringOut] | None = None,
        target_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        termination_policies: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpc_zone_identifier: list[str] | core.ArrayOut[core.StringOut] | None = None,
        wait_for_capacity_timeout: str | core.StringOut | None = None,
        wait_for_elb_capacity: int | core.IntOut | None = None,
        warm_pool: WarmPool | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Group.Args(
                max_size=max_size,
                min_size=min_size,
                availability_zones=availability_zones,
                capacity_rebalance=capacity_rebalance,
                context=context,
                default_cooldown=default_cooldown,
                default_instance_warmup=default_instance_warmup,
                desired_capacity=desired_capacity,
                enabled_metrics=enabled_metrics,
                force_delete=force_delete,
                force_delete_warm_pool=force_delete_warm_pool,
                health_check_grace_period=health_check_grace_period,
                health_check_type=health_check_type,
                initial_lifecycle_hook=initial_lifecycle_hook,
                instance_refresh=instance_refresh,
                launch_configuration=launch_configuration,
                launch_template=launch_template,
                load_balancers=load_balancers,
                max_instance_lifetime=max_instance_lifetime,
                metrics_granularity=metrics_granularity,
                min_elb_capacity=min_elb_capacity,
                mixed_instances_policy=mixed_instances_policy,
                name=name,
                name_prefix=name_prefix,
                placement_group=placement_group,
                protect_from_scale_in=protect_from_scale_in,
                service_linked_role_arn=service_linked_role_arn,
                suspended_processes=suspended_processes,
                tag=tag,
                tags=tags,
                target_group_arns=target_group_arns,
                termination_policies=termination_policies,
                vpc_zone_identifier=vpc_zone_identifier,
                wait_for_capacity_timeout=wait_for_capacity_timeout,
                wait_for_elb_capacity=wait_for_elb_capacity,
                warm_pool=warm_pool,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        capacity_rebalance: bool | core.BoolOut | None = core.arg(default=None)

        context: str | core.StringOut | None = core.arg(default=None)

        default_cooldown: int | core.IntOut | None = core.arg(default=None)

        default_instance_warmup: int | core.IntOut | None = core.arg(default=None)

        desired_capacity: int | core.IntOut | None = core.arg(default=None)

        enabled_metrics: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        force_delete: bool | core.BoolOut | None = core.arg(default=None)

        force_delete_warm_pool: bool | core.BoolOut | None = core.arg(default=None)

        health_check_grace_period: int | core.IntOut | None = core.arg(default=None)

        health_check_type: str | core.StringOut | None = core.arg(default=None)

        initial_lifecycle_hook: list[InitialLifecycleHook] | core.ArrayOut[
            InitialLifecycleHook
        ] | None = core.arg(default=None)

        instance_refresh: InstanceRefresh | None = core.arg(default=None)

        launch_configuration: str | core.StringOut | None = core.arg(default=None)

        launch_template: LaunchTemplate | None = core.arg(default=None)

        load_balancers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_instance_lifetime: int | core.IntOut | None = core.arg(default=None)

        max_size: int | core.IntOut = core.arg()

        metrics_granularity: str | core.StringOut | None = core.arg(default=None)

        min_elb_capacity: int | core.IntOut | None = core.arg(default=None)

        min_size: int | core.IntOut = core.arg()

        mixed_instances_policy: MixedInstancesPolicy | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        placement_group: str | core.StringOut | None = core.arg(default=None)

        protect_from_scale_in: bool | core.BoolOut | None = core.arg(default=None)

        service_linked_role_arn: str | core.StringOut | None = core.arg(default=None)

        suspended_processes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tag: list[Tag] | core.ArrayOut[Tag] | None = core.arg(default=None)

        tags: list[dict[str, str]] | core.MapArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        target_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        termination_policies: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpc_zone_identifier: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        wait_for_capacity_timeout: str | core.StringOut | None = core.arg(default=None)

        wait_for_elb_capacity: int | core.IntOut | None = core.arg(default=None)

        warm_pool: WarmPool | None = core.arg(default=None)
