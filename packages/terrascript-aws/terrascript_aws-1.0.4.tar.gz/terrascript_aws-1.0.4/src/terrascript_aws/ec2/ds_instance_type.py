import terrascript.core as core


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


@core.data(type="aws_ec2_instance_type", namespace="ec2")
class DsInstanceType(core.Data):
    """
    true` if auto recovery is supported.
    """

    auto_recovery_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    true` if it is a bare metal instance type.
    """
    bare_metal: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    true` if the instance type is a burstable performance instance type.
    """
    burstable_performance_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    true`  if the instance type is a current generation.
    """
    current_generation: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    true` if Dedicated Hosts are supported on the instance type.
    """
    dedicated_hosts_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The default number of cores for the instance type.
    """
    default_cores: int | core.IntOut = core.attr(int, computed=True)

    """
    The  default  number of threads per core for the instance type.
    """
    default_threads_per_core: int | core.IntOut = core.attr(int, computed=True)

    """
    The default number of vCPUs for the instance type.
    """
    default_vcpus: int | core.IntOut = core.attr(int, computed=True)

    """
    Indicates whether Amazon EBS encryption is supported.
    """
    ebs_encryption_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether non-volatile memory express (NVMe) is supported.
    """
    ebs_nvme_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates that the instance type is Amazon EBS-optimized.
    """
    ebs_optimized_support: str | core.StringOut = core.attr(str, computed=True)

    """
    The baseline bandwidth performance for an EBS-optimized instance type, in Mbps.
    """
    ebs_performance_baseline_bandwidth: int | core.IntOut = core.attr(int, computed=True)

    """
    The baseline input/output storage operations per seconds for an EBS-optimized instance type.
    """
    ebs_performance_baseline_iops: int | core.IntOut = core.attr(int, computed=True)

    """
    The baseline throughput performance for an EBS-optimized instance type, in MBps.
    """
    ebs_performance_baseline_throughput: float | core.FloatOut = core.attr(float, computed=True)

    """
    The maximum bandwidth performance for an EBS-optimized instance type, in Mbps.
    """
    ebs_performance_maximum_bandwidth: int | core.IntOut = core.attr(int, computed=True)

    """
    The maximum input/output storage operations per second for an EBS-optimized instance type.
    """
    ebs_performance_maximum_iops: int | core.IntOut = core.attr(int, computed=True)

    """
    The maximum throughput performance for an EBS-optimized instance type, in MBps.
    """
    ebs_performance_maximum_throughput: float | core.FloatOut = core.attr(float, computed=True)

    """
    Indicates whether Elastic Fabric Adapter (EFA) is supported.
    """
    efa_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Indicates whether Elastic Network Adapter (ENA) is supported.
    """
    ena_support: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether encryption in-transit between instances is supported.
    """
    encryption_in_transit_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Describes the FPGA accelerator settings for the instance type.
    """
    fpgas: list[Fpgas] | core.ArrayOut[Fpgas] = core.attr(
        Fpgas, computed=True, kind=core.Kind.array
    )

    """
    true` if the instance type is eligible for the free tier.
    """
    free_tier_eligible: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Describes the GPU accelerators for the instance type.
    """
    gpus: list[Gpus] | core.ArrayOut[Gpus] = core.attr(Gpus, computed=True, kind=core.Kind.array)

    """
    true` if On-Demand hibernation is supported.
    """
    hibernation_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Indicates the hypervisor used for the instance type.
    """
    hypervisor: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    inference_accelerators: list[InferenceAccelerators] | core.ArrayOut[
        InferenceAccelerators
    ] = core.attr(InferenceAccelerators, computed=True, kind=core.Kind.array)

    """
    Describes the disks for the instance type.
    """
    instance_disks: list[InstanceDisks] | core.ArrayOut[InstanceDisks] = core.attr(
        InstanceDisks, computed=True, kind=core.Kind.array
    )

    """
    true` if instance storage is supported.
    """
    instance_storage_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) Instance
    """
    instance_type: str | core.StringOut = core.attr(str)

    """
    true` if IPv6 is supported.
    """
    ipv6_supported: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The maximum number of IPv4 addresses per network interface.
    """
    maximum_ipv4_addresses_per_interface: int | core.IntOut = core.attr(int, computed=True)

    """
    The maximum number of IPv6 addresses per network interface.
    """
    maximum_ipv6_addresses_per_interface: int | core.IntOut = core.attr(int, computed=True)

    """
    The maximum number of network interfaces for the instance type.
    """
    maximum_network_interfaces: int | core.IntOut = core.attr(int, computed=True)

    """
    Size of the instance memory, in MiB.
    """
    memory_size: int | core.IntOut = core.attr(int, computed=True)

    """
    Describes the network performance.
    """
    network_performance: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of architectures supported by the instance type.
    """
    supported_architectures: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    A list of supported placement groups types.
    """
    supported_placement_strategies: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Indicates the supported root device types.
    """
    supported_root_device_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Indicates whether the instance type is offered for spot or On-Demand.
    """
    supported_usages_classes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The supported virtualization types.
    """
    supported_virtualization_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The speed of the processor, in GHz.
    """
    sustained_clock_speed: float | core.FloatOut = core.attr(float, computed=True)

    """
    The total memory of all FPGA accelerators for the instance type (in MiB).
    """
    total_fpga_memory: int | core.IntOut = core.attr(int, computed=True)

    """
    The total size of the memory for the GPU accelerators for the instance type (in MiB).
    """
    total_gpu_memory: int | core.IntOut = core.attr(int, computed=True)

    """
    The total size of the instance disks, in GB.
    """
    total_instance_storage: int | core.IntOut = core.attr(int, computed=True)

    """
    List of the valid number of cores that can be configured for the instance type.
    """
    valid_cores: list[int] | core.ArrayOut[core.IntOut] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    """
    List of the valid number of threads per core that can be configured for the instance type.
    """
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
