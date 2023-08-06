import terrascript.core as core


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: str | core.StringOut = core.attr(str)

    no_device: bool | core.BoolOut | None = core.attr(bool, default=None)

    virtual_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        no_device: bool | core.BoolOut | None = None,
        virtual_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        no_device: bool | core.BoolOut | None = core.arg(default=None)

        virtual_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    throughput: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    volume_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        iops: int | core.IntOut | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
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
        delete_on_termination: bool | core.BoolOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: bool | core.BoolOut | None = core.attr(bool, default=None)

    device_name: str | core.StringOut = core.attr(str)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    iops: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    no_device: bool | core.BoolOut | None = core.attr(bool, default=None)

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
        no_device: bool | core.BoolOut | None = None,
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
                no_device=no_device,
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

        no_device: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    http_put_response_hop_limit: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    http_tokens: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: str | core.StringOut | None = None,
        http_put_response_hop_limit: int | core.IntOut | None = None,
        http_tokens: str | core.StringOut | None = None,
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
        http_endpoint: str | core.StringOut | None = core.arg(default=None)

        http_put_response_hop_limit: int | core.IntOut | None = core.arg(default=None)

        http_tokens: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_launch_configuration", namespace="aws_auto_scaling")
class LaunchConfiguration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    associate_public_ip_address: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.attr(
        EbsBlockDevice, default=None, computed=True, kind=core.Kind.array
    )

    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    enable_monitoring: bool | core.BoolOut | None = core.attr(bool, default=None)

    ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
        EphemeralBlockDevice
    ] | None = core.attr(EphemeralBlockDevice, default=None, kind=core.Kind.array)

    iam_instance_profile: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_id: str | core.StringOut = core.attr(str)

    instance_type: str | core.StringOut = core.attr(str)

    key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    metadata_options: MetadataOptions | None = core.attr(
        MetadataOptions, default=None, computed=True
    )

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    placement_tenancy: str | core.StringOut | None = core.attr(str, default=None)

    root_block_device: RootBlockDevice | None = core.attr(
        RootBlockDevice, default=None, computed=True
    )

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    spot_price: str | core.StringOut | None = core.attr(str, default=None)

    user_data: str | core.StringOut | None = core.attr(str, default=None)

    user_data_base64: str | core.StringOut | None = core.attr(str, default=None)

    vpc_classic_link_id: str | core.StringOut | None = core.attr(str, default=None)

    vpc_classic_link_security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        image_id: str | core.StringOut,
        instance_type: str | core.StringOut,
        associate_public_ip_address: bool | core.BoolOut | None = None,
        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = None,
        ebs_optimized: bool | core.BoolOut | None = None,
        enable_monitoring: bool | core.BoolOut | None = None,
        ephemeral_block_device: list[EphemeralBlockDevice]
        | core.ArrayOut[EphemeralBlockDevice]
        | None = None,
        iam_instance_profile: str | core.StringOut | None = None,
        key_name: str | core.StringOut | None = None,
        metadata_options: MetadataOptions | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        placement_tenancy: str | core.StringOut | None = None,
        root_block_device: RootBlockDevice | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        spot_price: str | core.StringOut | None = None,
        user_data: str | core.StringOut | None = None,
        user_data_base64: str | core.StringOut | None = None,
        vpc_classic_link_id: str | core.StringOut | None = None,
        vpc_classic_link_security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LaunchConfiguration.Args(
                image_id=image_id,
                instance_type=instance_type,
                associate_public_ip_address=associate_public_ip_address,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                enable_monitoring=enable_monitoring,
                ephemeral_block_device=ephemeral_block_device,
                iam_instance_profile=iam_instance_profile,
                key_name=key_name,
                metadata_options=metadata_options,
                name=name,
                name_prefix=name_prefix,
                placement_tenancy=placement_tenancy,
                root_block_device=root_block_device,
                security_groups=security_groups,
                spot_price=spot_price,
                user_data=user_data,
                user_data_base64=user_data_base64,
                vpc_classic_link_id=vpc_classic_link_id,
                vpc_classic_link_security_groups=vpc_classic_link_security_groups,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        associate_public_ip_address: bool | core.BoolOut | None = core.arg(default=None)

        ebs_block_device: list[EbsBlockDevice] | core.ArrayOut[EbsBlockDevice] | None = core.arg(
            default=None
        )

        ebs_optimized: bool | core.BoolOut | None = core.arg(default=None)

        enable_monitoring: bool | core.BoolOut | None = core.arg(default=None)

        ephemeral_block_device: list[EphemeralBlockDevice] | core.ArrayOut[
            EphemeralBlockDevice
        ] | None = core.arg(default=None)

        iam_instance_profile: str | core.StringOut | None = core.arg(default=None)

        image_id: str | core.StringOut = core.arg()

        instance_type: str | core.StringOut = core.arg()

        key_name: str | core.StringOut | None = core.arg(default=None)

        metadata_options: MetadataOptions | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        placement_tenancy: str | core.StringOut | None = core.arg(default=None)

        root_block_device: RootBlockDevice | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        spot_price: str | core.StringOut | None = core.arg(default=None)

        user_data: str | core.StringOut | None = core.arg(default=None)

        user_data_base64: str | core.StringOut | None = core.arg(default=None)

        vpc_classic_link_id: str | core.StringOut | None = core.arg(default=None)

        vpc_classic_link_security_groups: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)
