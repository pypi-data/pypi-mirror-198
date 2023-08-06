import terrascript.core as core


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_name: str | core.StringOut = core.attr(str)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    iops: int | core.IntOut | None = core.attr(int, default=None)

    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        delete_on_termination: bool | core.BoolOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
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
                outpost_arn=outpost_arn,
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

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

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


@core.resource(type="aws_ami", namespace="ec2")
class Ami(core.Resource):
    """
    (Optional) Machine architecture for created instances. Defaults to "x86_64".
    """

    architecture: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the AMI.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The boot mode of the AMI. For more information, see [Boot modes](https://docs.aws.amazon.
    com/AWSEC2/latest/UserGuide/ami-boot.html) in the Amazon Elastic Compute Cloud User Guide.
    """
    boot_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The date and time to deprecate the AMI. If you specified a value for seconds, Amazon EC2
    rounds the seconds to the nearest minute. Valid values: [RFC3339 time string](https://tools.ietf.org
    /html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
    """
    deprecation_time: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A longer, human-readable description for the AMI.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Nested block describing an EBS block device that should be
    """
    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
    """
    ena_support: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Nested block describing an ephemeral block device that
    """
    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    """
    The hypervisor type of the image.
    """
    hypervisor: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the created AMI.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Path to an S3 object containing an image manifest, e.g., created
    """
    image_location: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The AWS account alias (for example, amazon, self) or the AWS account ID of the AMI owner.
    """
    image_owner_alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of image.
    """
    image_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The id of the kernel image (AKI) that will be used as the paravirtual
    """
    kernel_id: str | core.StringOut | None = core.attr(str, default=None)

    manage_ebs_snapshots: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) A region-unique name for the AMI.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The AWS account ID of the image owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    This value is set to windows for Windows AMIs; otherwise, it is blank.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    The platform details associated with the billing code of the AMI.
    """
    platform_details: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether the image has public launch permissions.
    """
    public: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) The id of an initrd image (ARI) that will be used when booting the
    """
    ramdisk_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
    """
    root_device_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Snapshot ID for the root volume (for EBS-backed AMIs)
    """
    root_snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) When set to "simple" (the default), enables enhanced networking
    """
    sriov_net_support: str | core.StringOut | None = core.attr(str, default=None)

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
    (Optional) If the image is configured for NitroTPM support, the value is `v2.0`. For more informatio
    n, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the Amazon E
    lastic Compute Cloud User Guide.
    """
    tpm_support: str | core.StringOut | None = core.attr(str, default=None)

    """
    The operation of the Amazon EC2 instance and the billing code that is associated with the AMI.
    """
    usage_operation: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Keyword to choose what virtualization mode created instances
    """
    virtualization_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        architecture: str | core.StringOut | None = None,
        boot_mode: str | core.StringOut | None = None,
        deprecation_time: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = None,
        ena_support: bool | core.BoolOut | None = None,
        ephemeral_block_device: list[EphemeralBlockDevice]
        | core.ArrayOut[EphemeralBlockDevice]
        | None = None,
        image_location: str | core.StringOut | None = None,
        kernel_id: str | core.StringOut | None = None,
        ramdisk_id: str | core.StringOut | None = None,
        root_device_name: str | core.StringOut | None = None,
        sriov_net_support: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tpm_support: str | core.StringOut | None = None,
        virtualization_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ami.Args(
                name=name,
                architecture=architecture,
                boot_mode=boot_mode,
                deprecation_time=deprecation_time,
                description=description,
                ebs_block_device=ebs_block_device,
                ena_support=ena_support,
                ephemeral_block_device=ephemeral_block_device,
                image_location=image_location,
                kernel_id=kernel_id,
                ramdisk_id=ramdisk_id,
                root_device_name=root_device_name,
                sriov_net_support=sriov_net_support,
                tags=tags,
                tags_all=tags_all,
                tpm_support=tpm_support,
                virtualization_type=virtualization_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        architecture: str | core.StringOut | None = core.arg(default=None)

        boot_mode: str | core.StringOut | None = core.arg(default=None)

        deprecation_time: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.arg(
            default=None
        )

        ena_support: bool | core.BoolOut | None = core.arg(default=None)

        ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
            EphemeralBlockDevice
        ] | None = core.arg(default=None)

        image_location: str | core.StringOut | None = core.arg(default=None)

        kernel_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        ramdisk_id: str | core.StringOut | None = core.arg(default=None)

        root_device_name: str | core.StringOut | None = core.arg(default=None)

        sriov_net_support: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tpm_support: str | core.StringOut | None = core.arg(default=None)

        virtualization_type: str | core.StringOut | None = core.arg(default=None)
