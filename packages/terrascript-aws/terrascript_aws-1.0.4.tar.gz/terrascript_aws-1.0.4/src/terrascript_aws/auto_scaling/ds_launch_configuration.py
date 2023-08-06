import terrascript.core as core


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut = core.attr(str, computed=True)

    http_put_response_hop_limit: int | core.IntOut = core.attr(int, computed=True)

    http_tokens: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut,
        http_put_response_hop_limit: int | core.IntOut,
        http_tokens: str | core.StringOut,
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: str | core.StringOut = core.arg()

        http_put_response_hop_limit: int | core.IntOut = core.arg()

        http_tokens: str | core.StringOut = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        throughput: int | core.IntOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: bool | core.BoolOut = core.arg()

        encrypted: bool | core.BoolOut = core.arg()

        iops: int | core.IntOut = core.arg()

        throughput: int | core.IntOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    device_name: str | core.StringOut = core.attr(str, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    no_device: bool | core.BoolOut = core.attr(bool, computed=True)

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
        no_device: bool | core.BoolOut,
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
                no_device=no_device,
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

        no_device: bool | core.BoolOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()

        throughput: int | core.IntOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


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


@core.data(type="aws_launch_configuration", namespace="auto_scaling")
class DsLaunchConfiguration(core.Data):
    """
    The Amazon Resource Name of the launch configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether a Public IP address is associated with the instance.
    """
    associate_public_ip_address: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The EBS Block Devices attached to the instance.
    """
    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] = core.attr(
        EbsBlockDevice, computed=True, kind=core.Kind.array
    )

    """
    Whether the launched EC2 instance will be EBS-optimized.
    """
    ebs_optimized: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether Detailed Monitoring is Enabled.
    """
    enable_monitoring: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The Ephemeral volumes on the instance.
    """
    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] = core.attr(EphemeralBlockDevice, computed=True, kind=core.Kind.array)

    """
    The IAM Instance Profile to associate with launched instances.
    """
    iam_instance_profile: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the launch configuration.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The EC2 Image ID of the instance.
    """
    image_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Instance Type of the instance to launch.
    """
    instance_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The Key Name that should be used for the instance.
    """
    key_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The metadata options for the instance.
    """
    metadata_options: list[MetadataOptions] | core.ArrayOut[MetadataOptions] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    """
    (Required) The name of the launch configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The Tenancy of the instance.
    """
    placement_tenancy: str | core.StringOut = core.attr(str, computed=True)

    """
    The Root Block Device of the instance.
    """
    root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] = core.attr(
        RootBlockDevice, computed=True, kind=core.Kind.array
    )

    """
    A list of associated Security Group IDS.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The Price to use for reserving Spot instances.
    """
    spot_price: str | core.StringOut = core.attr(str, computed=True)

    """
    The User Data of the instance.
    """
    user_data: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of a ClassicLink-enabled VPC.
    """
    vpc_classic_link_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
    """
    vpc_classic_link_security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsLaunchConfiguration.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
