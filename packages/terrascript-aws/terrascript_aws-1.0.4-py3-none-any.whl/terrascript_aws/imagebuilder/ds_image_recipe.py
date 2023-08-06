import terrascript.core as core


@core.schema
class Ebs(core.Schema):

    delete_on_termination: bool | core.BoolOut = core.attr(bool, computed=True)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    snapshot_id: str | core.StringOut = core.attr(str, computed=True)

    throughput: int | core.IntOut = core.attr(int, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    volume_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: bool | core.BoolOut,
        encrypted: bool | core.BoolOut,
        iops: int | core.IntOut,
        kms_key_id: str | core.StringOut,
        snapshot_id: str | core.StringOut,
        throughput: int | core.IntOut,
        volume_size: int | core.IntOut,
        volume_type: str | core.StringOut,
    ):
        super().__init__(
            args=Ebs.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
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

        kms_key_id: str | core.StringOut = core.arg()

        snapshot_id: str | core.StringOut = core.arg()

        throughput: int | core.IntOut = core.arg()

        volume_size: int | core.IntOut = core.arg()

        volume_type: str | core.StringOut = core.arg()


@core.schema
class BlockDeviceMapping(core.Schema):

    device_name: str | core.StringOut = core.attr(str, computed=True)

    ebs: list[Ebs] | core.ArrayOut[Ebs] = core.attr(Ebs, computed=True, kind=core.Kind.array)

    no_device: str | core.StringOut = core.attr(str, computed=True)

    virtual_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut,
        ebs: list[Ebs] | core.ArrayOut[Ebs],
        no_device: str | core.StringOut,
        virtual_name: str | core.StringOut,
    ):
        super().__init__(
            args=BlockDeviceMapping.Args(
                device_name=device_name,
                ebs=ebs,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: str | core.StringOut = core.arg()

        ebs: list[Ebs] | core.ArrayOut[Ebs] = core.arg()

        no_device: str | core.StringOut = core.arg()

        virtual_name: str | core.StringOut = core.arg()


@core.schema
class Parameter(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Component(core.Schema):

    component_arn: str | core.StringOut = core.attr(str, computed=True)

    parameter: list[Parameter] | core.ArrayOut[Parameter] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        component_arn: str | core.StringOut,
        parameter: list[Parameter] | core.ArrayOut[Parameter],
    ):
        super().__init__(
            args=Component.Args(
                component_arn=component_arn,
                parameter=parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        component_arn: str | core.StringOut = core.arg()

        parameter: list[Parameter] | core.ArrayOut[Parameter] = core.arg()


@core.data(type="aws_imagebuilder_image_recipe", namespace="imagebuilder")
class DsImageRecipe(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the image recipe.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Set of objects with block device mappings for the image recipe.
    """
    block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[BlockDeviceMapping] = core.attr(
        BlockDeviceMapping, computed=True, kind=core.Kind.array
    )

    """
    List of objects with components for the image recipe.
    """
    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    """
    Date the image recipe was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the image recipe.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    name` - Name of the component parameter.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Owner of the image recipe.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    Base image of the image recipe.
    """
    parent_image: str | core.StringOut = core.attr(str, computed=True)

    """
    Platform of the image recipe.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the image recipe.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Base64 encoded contents of user data. Commands or a command script to run when build instance is lau
    nched.
    """
    user_data_base64: str | core.StringOut = core.attr(str, computed=True)

    """
    Version of the image recipe.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    The working directory used during build and test workflows.
    """
    working_directory: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImageRecipe.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
