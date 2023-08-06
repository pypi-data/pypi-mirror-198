import terrascript.core as core


@core.schema
class InstanceDisks(core.Schema):

    count: int | core.IntOut = core.attr(int, computed=True)

    size: int | core.IntOut = core.attr(int, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: int | core.IntOut,
        size: int | core.IntOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=InstanceDisks.Args(
                count=count,
                size=size,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut = core.arg()

        size: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class Gpus(core.Schema):

    count: int | core.IntOut = core.attr(int, computed=True)

    manufacturer: str | core.StringOut = core.attr(str, computed=True)

    memory_size: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: int | core.IntOut,
        manufacturer: str | core.StringOut,
        memory_size: int | core.IntOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Gpus.Args(
                count=count,
                manufacturer=manufacturer,
                memory_size=memory_size,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut = core.arg()

        manufacturer: str | core.StringOut = core.arg()

        memory_size: int | core.IntOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Fpgas(core.Schema):

    count: int | core.IntOut = core.attr(int, computed=True)

    manufacturer: str | core.StringOut = core.attr(str, computed=True)

    memory_size: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: int | core.IntOut,
        manufacturer: str | core.StringOut,
        memory_size: int | core.IntOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Fpgas.Args(
                count=count,
                manufacturer=manufacturer,
                memory_size=memory_size,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut = core.arg()

        manufacturer: str | core.StringOut = core.arg()

        memory_size: int | core.IntOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class InferenceAccelerators(core.Schema):

    count: int | core.IntOut = core.attr(int, computed=True)

    manufacturer: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: int | core.IntOut,
        manufacturer: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=InferenceAccelerators.Args(
                count=count,
                manufacturer=manufacturer,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: int | core.IntOut = core.arg()

        manufacturer: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.data(type="aws_ec2_instance_type", namespace="aws_ec2")
class DsInstanceType(core.Data):

    auto_recovery_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    bare_metal: bool | core.BoolOut = core.attr(bool, computed=True)

    burstable_performance_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    current_generation: bool | core.BoolOut = core.attr(bool, computed=True)

    dedicated_hosts_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    default_cores: int | core.IntOut = core.attr(int, computed=True)

    default_threads_per_core: int | core.IntOut = core.attr(int, computed=True)

    default_vcpus: int | core.IntOut = core.attr(int, computed=True)

    ebs_encryption_support: str | core.StringOut = core.attr(str, computed=True)

    ebs_nvme_support: str | core.StringOut = core.attr(str, computed=True)

    ebs_optimized_support: str | core.StringOut = core.attr(str, computed=True)

    ebs_performance_baseline_bandwidth: int | core.IntOut = core.attr(int, computed=True)

    ebs_performance_baseline_iops: int | core.IntOut = core.attr(int, computed=True)

    ebs_performance_baseline_throughput: float | core.FloatOut = core.attr(float, computed=True)

    ebs_performance_maximum_bandwidth: int | core.IntOut = core.attr(int, computed=True)

    ebs_performance_maximum_iops: int | core.IntOut = core.attr(int, computed=True)

    ebs_performance_maximum_throughput: float | core.FloatOut = core.attr(float, computed=True)

    efa_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    ena_support: str | core.StringOut = core.attr(str, computed=True)

    encryption_in_transit_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    fpgas: list[Fpgas] | core.ArrayOut[Fpgas] = core.attr(
        Fpgas, computed=True, kind=core.Kind.array
    )

    free_tier_eligible: bool | core.BoolOut = core.attr(bool, computed=True)

    gpus: list[Gpus] | core.ArrayOut[Gpus] = core.attr(Gpus, computed=True, kind=core.Kind.array)

    hibernation_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    hypervisor: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    inference_accelerators: list[InferenceAccelerators] | core.ArrayOut[
        InferenceAccelerators
    ] = core.attr(InferenceAccelerators, computed=True, kind=core.Kind.array)

    instance_disks: list[InstanceDisks] | core.ArrayOut[InstanceDisks] = core.attr(
        InstanceDisks, computed=True, kind=core.Kind.array
    )

    instance_storage_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    instance_type: str | core.StringOut = core.attr(str)

    ipv6_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    maximum_ipv4_addresses_per_interface: int | core.IntOut = core.attr(int, computed=True)

    maximum_ipv6_addresses_per_interface: int | core.IntOut = core.attr(int, computed=True)

    maximum_network_interfaces: int | core.IntOut = core.attr(int, computed=True)

    memory_size: int | core.IntOut = core.attr(int, computed=True)

    network_performance: str | core.StringOut = core.attr(str, computed=True)

    supported_architectures: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_placement_strategies: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_root_device_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_usages_classes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_virtualization_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    sustained_clock_speed: float | core.FloatOut = core.attr(float, computed=True)

    total_fpga_memory: int | core.IntOut = core.attr(int, computed=True)

    total_gpu_memory: int | core.IntOut = core.attr(int, computed=True)

    total_instance_storage: int | core.IntOut = core.attr(int, computed=True)

    valid_cores: list[int] | core.ArrayOut[core.IntOut] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    valid_threads_per_core: list[int] | core.ArrayOut[core.IntOut] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_type: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceType.Args(
                instance_type=instance_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: str | core.StringOut = core.arg()
