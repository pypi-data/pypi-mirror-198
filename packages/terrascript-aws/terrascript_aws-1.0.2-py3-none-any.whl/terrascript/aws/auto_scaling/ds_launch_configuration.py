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


@core.data(type="aws_launch_configuration", namespace="aws_auto_scaling")
class DsLaunchConfiguration(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    associate_public_ip_address: bool | core.BoolOut = core.attr(bool, computed=True)

    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] = core.attr(
        EbsBlockDevice, computed=True, kind=core.Kind.array
    )

    ebs_optimized: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_monitoring: bool | core.BoolOut = core.attr(bool, computed=True)

    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] = core.attr(EphemeralBlockDevice, computed=True, kind=core.Kind.array)

    iam_instance_profile: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_id: str | core.StringOut = core.attr(str, computed=True)

    instance_type: str | core.StringOut = core.attr(str, computed=True)

    key_name: str | core.StringOut = core.attr(str, computed=True)

    metadata_options: list[MetadataOptions] | core.ArrayOut[MetadataOptions] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    placement_tenancy: str | core.StringOut = core.attr(str, computed=True)

    root_block_device: list[RootBlockDevice] | core.ArrayOut[RootBlockDevice] = core.attr(
        RootBlockDevice, computed=True, kind=core.Kind.array
    )

    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    spot_price: str | core.StringOut = core.attr(str, computed=True)

    user_data: str | core.StringOut = core.attr(str, computed=True)

    vpc_classic_link_id: str | core.StringOut = core.attr(str, computed=True)

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
