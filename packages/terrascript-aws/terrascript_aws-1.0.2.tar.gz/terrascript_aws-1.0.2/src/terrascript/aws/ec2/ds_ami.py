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


@core.data(type="aws_ami", namespace="aws_ec2")
class DsAmi(core.Data):

    architecture: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    block_device_mappings: list[BlockDeviceMappings] | core.ArrayOut[
        BlockDeviceMappings
    ] = core.attr(BlockDeviceMappings, computed=True, kind=core.Kind.array)

    boot_mode: str | core.StringOut = core.attr(str, computed=True)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    deprecation_time: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    ena_support: bool | core.BoolOut = core.attr(bool, computed=True)

    executable_users: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    hypervisor: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    image_id: str | core.StringOut = core.attr(str, computed=True)

    image_location: str | core.StringOut = core.attr(str, computed=True)

    image_owner_alias: str | core.StringOut = core.attr(str, computed=True)

    image_type: str | core.StringOut = core.attr(str, computed=True)

    include_deprecated: bool | core.BoolOut | None = core.attr(bool, default=None)

    kernel_id: str | core.StringOut = core.attr(str, computed=True)

    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str, computed=True)

    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    owners: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    platform: str | core.StringOut = core.attr(str, computed=True)

    platform_details: str | core.StringOut = core.attr(str, computed=True)

    product_codes: list[ProductCodes] | core.ArrayOut[ProductCodes] = core.attr(
        ProductCodes, computed=True, kind=core.Kind.array
    )

    public: bool | core.BoolOut = core.attr(bool, computed=True)

    ramdisk_id: str | core.StringOut = core.attr(str, computed=True)

    root_device_name: str | core.StringOut = core.attr(str, computed=True)

    root_device_type: str | core.StringOut = core.attr(str, computed=True)

    root_snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    sriov_net_support: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    state_reason: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tpm_support: str | core.StringOut = core.attr(str, computed=True)

    usage_operation: str | core.StringOut = core.attr(str, computed=True)

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
