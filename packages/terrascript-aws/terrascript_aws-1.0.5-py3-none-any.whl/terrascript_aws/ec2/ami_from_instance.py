import terrascript.core as core


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: str | core.StringOut = core.attr(str, computed=True)

    virtual_name: str | core.StringOut = core.attr(str, computed=True)

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
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        device_name: str | core.StringOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        outpost_arn: str | core.StringOut,
        snapshot_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                outpost_arn=outpost_arn,
                snapshot_id=snapshot_id,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut = core.arg()

        device_name: str | core.StringOut = core.arg()

        encrypted: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        outpost_arn: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()

        throughput: int | core.IntOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.resource(type="aws_ami_from_instance", namespace="ec2")
class AmiFromInstance(core.Resource):

    architecture: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the AMI.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    boot_mode: str | core.StringOut = core.attr(str, computed=True)

    deprecation_time: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    ena_support: bool | core.BoolOut = core.attr(bool, computed=True)

    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    hypervisor: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the created AMI.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    image_location: str | core.StringOut = core.attr(str, computed=True)

    image_owner_alias: str | core.StringOut = core.attr(str, computed=True)

    image_type: str | core.StringOut = core.attr(str, computed=True)

    kernel_id: str | core.StringOut = core.attr(str, computed=True)

    manage_ebs_snapshots: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) A region-unique name for the AMI.
    """
    name: str | core.StringOut = core.attr(str)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    platform: str | core.StringOut = core.attr(str, computed=True)

    platform_details: str | core.StringOut = core.attr(str, computed=True)

    public: bool | core.BoolOut = core.attr(bool, computed=True)

    ramdisk_id: str | core.StringOut = core.attr(str, computed=True)

    root_device_name: str | core.StringOut = core.attr(str, computed=True)

    root_snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Boolean that overrides the behavior of stopping
    """
    snapshot_without_reboot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The id of the instance to use as the basis of the AMI.
    """
    source_instance_id: str | core.StringOut = core.attr(str)

    sriov_net_support: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tpm_support: str | core.StringOut = core.attr(str, computed=True)

    usage_operation: str | core.StringOut = core.attr(str, computed=True)

    virtualization_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        source_instance_id: str | core.StringOut,
        deprecation_time: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = None,
        ephemeral_block_device: list[EphemeralBlockDevice]
        | core.ArrayOut[EphemeralBlockDevice]
        | None = None,
        snapshot_without_reboot: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AmiFromInstance.Args(
                name=name,
                source_instance_id=source_instance_id,
                deprecation_time=deprecation_time,
                description=description,
                ebs_block_device=ebs_block_device,
                ephemeral_block_device=ephemeral_block_device,
                snapshot_without_reboot=snapshot_without_reboot,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deprecation_time: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.arg(
            default=None
        )

        ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
            EphemeralBlockDevice
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        snapshot_without_reboot: bool | core.BoolOut | None = core.arg(default=None)

        source_instance_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
