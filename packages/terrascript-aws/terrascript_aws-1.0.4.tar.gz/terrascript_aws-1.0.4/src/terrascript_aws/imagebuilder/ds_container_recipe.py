import terrascript.core as core


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
class InstanceConfiguration(core.Schema):

    block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[BlockDeviceMapping] = core.attr(
        BlockDeviceMapping, computed=True, kind=core.Kind.array
    )

    image: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[BlockDeviceMapping],
        image: str | core.StringOut,
    ):
        super().__init__(
            args=InstanceConfiguration.Args(
                block_device_mapping=block_device_mapping,
                image=image,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[
            BlockDeviceMapping
        ] = core.arg()

        image: str | core.StringOut = core.arg()


@core.schema
class TargetRepository(core.Schema):

    repository_name: str | core.StringOut = core.attr(str, computed=True)

    service: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        repository_name: str | core.StringOut,
        service: str | core.StringOut,
    ):
        super().__init__(
            args=TargetRepository.Args(
                repository_name=repository_name,
                service=service,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: str | core.StringOut = core.arg()

        service: str | core.StringOut = core.arg()


@core.data(type="aws_imagebuilder_container_recipe", namespace="imagebuilder")
class DsContainerRecipe(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the container recipe.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    List of objects with components for the container recipe.
    """
    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    """
    Type of the container.
    """
    container_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the container recipe was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the container recipe.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Dockerfile template used to build the image.
    """
    dockerfile_template_data: str | core.StringOut = core.attr(str, computed=True)

    """
    Flag that indicates if the target container is encrypted.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    List of objects with instance configurations for building and testing container images.
    """
    instance_configuration: list[InstanceConfiguration] | core.ArrayOut[
        InstanceConfiguration
    ] = core.attr(InstanceConfiguration, computed=True, kind=core.Kind.array)

    """
    s_key_id` - Amazon Resource Name (ARN) of the Key Management Service (KMS) Key for encryption.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    name` - Name of the component parameter.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Owner of the container recipe.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    Base image for the container recipe.
    """
    parent_image: str | core.StringOut = core.attr(str, computed=True)

    """
    Platform of the container recipe.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the container recipe.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Destination repository for the container image.
    """
    target_repository: list[TargetRepository] | core.ArrayOut[TargetRepository] = core.attr(
        TargetRepository, computed=True, kind=core.Kind.array
    )

    """
    Version of the container recipe.
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
            args=DsContainerRecipe.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
