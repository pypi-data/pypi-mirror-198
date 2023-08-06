import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class BlockDeviceMappings(core.Schema):

    device_name: str | core.StringOut = core.attr(str, computed=True)

    ebs: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    no_device: str | core.StringOut = core.attr(str, computed=True)

    virtual_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        ebs: dict[str, str] | core.MapOut[core.StringOut],
        no_device: str | core.StringOut,
        virtual_name: str | core.StringOut,
    ):
        super().__init__(
            args=BlockDeviceMappings.Args(
                device_name=device_name,
                ebs=ebs,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        ebs: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        no_device: str | core.StringOut = core.arg()

        virtual_name: str | core.StringOut = core.arg()


@core.schema
class ProductCodes(core.Schema):

    product_code_id: str | core.StringOut = core.attr(str, computed=True)

    product_code_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        product_code_id: str | core.StringOut,
        product_code_type: str | core.StringOut,
    ):
        super().__init__(
            args=ProductCodes.Args(
                product_code_id=product_code_id,
                product_code_type=product_code_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        product_code_id: str | core.StringOut = core.arg()

        product_code_type: str | core.StringOut = core.arg()


@core.data(type="aws_ami", namespace="ec2")
class DsAmi(core.Data):
    """
    The OS architecture of the AMI (ie: `i386` or `x86_64`).
    """

    architecture: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the AMI.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of objects with block device mappings of the AMI.
    """
    block_device_mappings: list[BlockDeviceMappings] | core.ArrayOut[
        BlockDeviceMappings
    ] = core.attr(BlockDeviceMappings, computed=True, kind=core.Kind.array)

    """
    The boot mode of the image.
    """
    boot_mode: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time the image was created.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time when the image will be deprecated.
    """
    deprecation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the AMI that was provided during image
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether enhanced networking with ENA is enabled.
    """
    ena_support: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Limit search to users with *explicit* launch permission on
    """
    executable_users: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) One or more name/value pairs to filter off of. There are
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    The hypervisor type of the image.
    """
    hypervisor: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AMI. Should be the same as the resource `id`.
    """
    image_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The location of the AMI.
    """
    image_location: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account alias (for example, `amazon`, `self`) or
    """
    image_owner_alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of image.
    """
    image_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If true, all deprecated AMIs are included in the response. If false, no deprecated AMIs a
    re included in the response. If no value is specified, the default value is false.
    """
    include_deprecated: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The kernel associated with the image, if any. Only applicable
    """
    kernel_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The name of the AMI that was provided during image creation.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A regex string to apply to the AMI list returned
    """
    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    """
    The AWS account ID of the image owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of AMI owners to limit search. Valid values: an AWS account ID, `self` (the current
    account), or an AWS owner alias (e.g., `amazon`, `aws-marketplace`, `microsoft`).
    """
    owners: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The value is Windows for `Windows` AMIs; otherwise blank.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    The platform details associated with the billing code of the AMI.
    """
    platform_details: str | core.StringOut = core.attr(str, computed=True)

    """
    Any product codes associated with the AMI.
    """
    product_codes: list[ProductCodes] | core.ArrayOut[ProductCodes] = core.attr(
        ProductCodes, computed=True, kind=core.Kind.array
    )

    """
    true` if the image has public launch permissions.
    """
    public: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The RAM disk associated with the image, if any. Only applicable
    """
    ramdisk_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The device name of the root device.
    """
    root_device_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of root device (ie: `ebs` or `instance-store`).
    """
    root_device_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The snapshot id associated with the root device, if any
    """
    root_snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether enhanced networking is enabled.
    """
    sriov_net_support: str | core.StringOut = core.attr(str, computed=True)

    """
    The current state of the AMI. If the state is `available`, the image
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    Describes a state change. Fields are `UNSET` if not available.
    """
    state_reason: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    Any tags assigned to the image.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    If the image is configured for NitroTPM support, the value is `v2.0`.
    """
    tpm_support: str | core.StringOut = core.attr(str, computed=True)

    """
    The operation of the Amazon EC2 instance and the billing code that is associated with the AMI.
    """
    usage_operation: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of virtualization of the AMI (ie: `hvm` or
    """
    virtualization_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        executable_users: list[str] | core.ArrayOut[core.StringOut] | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        include_deprecated: bool | core.BoolOut | None = None,
        most_recent: bool | core.BoolOut | None = None,
        name_regex: str | core.StringOut | None = None,
        owners: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAmi.Args(
                executable_users=executable_users,
                filter=filter,
                include_deprecated=include_deprecated,
                most_recent=most_recent,
                name_regex=name_regex,
                owners=owners,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        executable_users: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        include_deprecated: bool | core.BoolOut | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        name_regex: str | core.StringOut | None = core.arg(default=None)

        owners: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
