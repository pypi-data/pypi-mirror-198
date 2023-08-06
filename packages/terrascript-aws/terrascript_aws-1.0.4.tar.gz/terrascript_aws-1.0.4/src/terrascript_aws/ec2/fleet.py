import terrascript.core as core


@core.schema
class TargetCapacitySpecification(core.Schema):

    default_target_capacity_type: str | core.StringOut = core.attr(str)

    on_demand_target_capacity: int | core.IntOut | None = core.attr(int, default=None)

    spot_target_capacity: int | core.IntOut | None = core.attr(int, default=None)

    total_target_capacity: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        default_target_capacity_type: str | core.StringOut,
        total_target_capacity: int | core.IntOut,
        on_demand_target_capacity: int | core.IntOut | None = None,
        spot_target_capacity: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=TargetCapacitySpecification.Args(
                default_target_capacity_type=default_target_capacity_type,
                total_target_capacity=total_target_capacity,
                on_demand_target_capacity=on_demand_target_capacity,
                spot_target_capacity=spot_target_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_target_capacity_type: str | core.StringOut = core.arg()

        on_demand_target_capacity: int | core.IntOut | None = core.arg(default=None)

        spot_target_capacity: int | core.IntOut | None = core.arg(default=None)

        total_target_capacity: int | core.IntOut = core.arg()


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
class Override(core.Schema):

    availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    instance_requirements: InstanceRequirements | None = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    max_price: str | core.StringOut | None = core.attr(str, default=None)

    priority: float | core.FloatOut | None = core.attr(float, default=None)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    weighted_capacity: float | core.FloatOut | None = core.attr(float, default=None)

    def __init__(
        self,
        *,
        availability_zone: str | core.StringOut | None = None,
        instance_requirements: InstanceRequirements | None = None,
        instance_type: str | core.StringOut | None = None,
        max_price: str | core.StringOut | None = None,
        priority: float | core.FloatOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        weighted_capacity: float | core.FloatOut | None = None,
    ):
        super().__init__(
            args=Override.Args(
                availability_zone=availability_zone,
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                max_price=max_price,
                priority=priority,
                subnet_id=subnet_id,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut | None = core.arg(default=None)

        instance_requirements: InstanceRequirements | None = core.arg(default=None)

        instance_type: str | core.StringOut | None = core.arg(default=None)

        max_price: str | core.StringOut | None = core.arg(default=None)

        priority: float | core.FloatOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        weighted_capacity: float | core.FloatOut | None = core.arg(default=None)


@core.schema
class LaunchTemplateSpecification(core.Schema):

    launch_template_id: str | core.StringOut | None = core.attr(str, default=None)

    launch_template_name: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        version: str | core.StringOut,
        launch_template_id: str | core.StringOut | None = None,
        launch_template_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplateSpecification.Args(
                version=version,
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: str | core.StringOut | None = core.arg(default=None)

        launch_template_name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()


@core.schema
class LaunchTemplateConfig(core.Schema):

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
            args=LaunchTemplateConfig.Args(
                launch_template_specification=launch_template_specification,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_specification: LaunchTemplateSpecification = core.arg()

        override: list[Override] | core.ArrayOut[Override] | None = core.arg(default=None)


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
class MaintenanceStrategies(core.Schema):

    capacity_rebalance: CapacityRebalance | None = core.attr(CapacityRebalance, default=None)

    def __init__(
        self,
        *,
        capacity_rebalance: CapacityRebalance | None = None,
    ):
        super().__init__(
            args=MaintenanceStrategies.Args(
                capacity_rebalance=capacity_rebalance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_rebalance: CapacityRebalance | None = core.arg(default=None)


@core.schema
class SpotOptions(core.Schema):

    allocation_strategy: str | core.StringOut | None = core.attr(str, default=None)

    instance_interruption_behavior: str | core.StringOut | None = core.attr(str, default=None)

    instance_pools_to_use_count: int | core.IntOut | None = core.attr(int, default=None)

    maintenance_strategies: MaintenanceStrategies | None = core.attr(
        MaintenanceStrategies, default=None
    )

    def __init__(
        self,
        *,
        allocation_strategy: str | core.StringOut | None = None,
        instance_interruption_behavior: str | core.StringOut | None = None,
        instance_pools_to_use_count: int | core.IntOut | None = None,
        maintenance_strategies: MaintenanceStrategies | None = None,
    ):
        super().__init__(
            args=SpotOptions.Args(
                allocation_strategy=allocation_strategy,
                instance_interruption_behavior=instance_interruption_behavior,
                instance_pools_to_use_count=instance_pools_to_use_count,
                maintenance_strategies=maintenance_strategies,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut | None = core.arg(default=None)

        instance_interruption_behavior: str | core.StringOut | None = core.arg(default=None)

        instance_pools_to_use_count: int | core.IntOut | None = core.arg(default=None)

        maintenance_strategies: MaintenanceStrategies | None = core.arg(default=None)


@core.schema
class OnDemandOptions(core.Schema):

    allocation_strategy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        allocation_strategy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OnDemandOptions.Args(
                allocation_strategy=allocation_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ec2_fleet", namespace="ec2")
class Fleet(core.Resource):
    """
    The ARN of the fleet
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Reserved.
    """
    context: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether running instances should be terminated if the total target capacity of the EC2 Fl
    eet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. D
    efaults to `termination`.
    """
    excess_capacity_termination_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    Fleet identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Nested argument containing EC2 Launch Template configurations. Defined below.
    """
    launch_template_config: LaunchTemplateConfig = core.attr(LaunchTemplateConfig)

    """
    (Optional) Nested argument containing On-Demand configurations. Defined below.
    """
    on_demand_options: OnDemandOptions | None = core.attr(OnDemandOptions, default=None)

    """
    (Optional) Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
    """
    replace_unhealthy_instances: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Nested argument containing Spot configurations. Defined below.
    """
    spot_options: SpotOptions | None = core.attr(SpotOptions, default=None)

    """
    (Optional) Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template. I
    f configured with a provider [`default_tags` configuration block](https://registry.terraform.io/prov
    iders/hashicorp/aws/latest/docs#default_tags-configuration-block) present, tags with matching keys w
    ill overwrite those defined at the provider-level.
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
    (Required) Nested argument containing target capacity configurations. Defined below.
    """
    target_capacity_specification: TargetCapacitySpecification = core.attr(
        TargetCapacitySpecification
    )

    """
    (Optional) Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults t
    o `false`.
    """
    terminate_instances: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `f
    alse`.
    """
    terminate_instances_with_expiration: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The type of request. Indicates whether the EC2 Fleet only requests the target capacity, o
    r also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        launch_template_config: LaunchTemplateConfig,
        target_capacity_specification: TargetCapacitySpecification,
        context: str | core.StringOut | None = None,
        excess_capacity_termination_policy: str | core.StringOut | None = None,
        on_demand_options: OnDemandOptions | None = None,
        replace_unhealthy_instances: bool | core.BoolOut | None = None,
        spot_options: SpotOptions | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        terminate_instances: bool | core.BoolOut | None = None,
        terminate_instances_with_expiration: bool | core.BoolOut | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                launch_template_config=launch_template_config,
                target_capacity_specification=target_capacity_specification,
                context=context,
                excess_capacity_termination_policy=excess_capacity_termination_policy,
                on_demand_options=on_demand_options,
                replace_unhealthy_instances=replace_unhealthy_instances,
                spot_options=spot_options,
                tags=tags,
                tags_all=tags_all,
                terminate_instances=terminate_instances,
                terminate_instances_with_expiration=terminate_instances_with_expiration,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        context: str | core.StringOut | None = core.arg(default=None)

        excess_capacity_termination_policy: str | core.StringOut | None = core.arg(default=None)

        launch_template_config: LaunchTemplateConfig = core.arg()

        on_demand_options: OnDemandOptions | None = core.arg(default=None)

        replace_unhealthy_instances: bool | core.BoolOut | None = core.arg(default=None)

        spot_options: SpotOptions | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_capacity_specification: TargetCapacitySpecification = core.arg()

        terminate_instances: bool | core.BoolOut | None = core.arg(default=None)

        terminate_instances_with_expiration: bool | core.BoolOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
