import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

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

    component_arn: str | core.StringOut = core.attr(str)

    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        component_arn: str | core.StringOut,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
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

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)


@core.schema
class Ebs(core.Schema):

    delete_on_termination: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: str | core.StringOut | None = core.attr(str, default=None)

    iops: int | core.IntOut | None = core.attr(int, default=None)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_id: str | core.StringOut | None = core.attr(str, default=None)

    throughput: int | core.IntOut | None = core.attr(int, default=None)

    volume_size: int | core.IntOut | None = core.attr(int, default=None)

    volume_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delete_on_termination: str | core.StringOut | None = None,
        encrypted: str | core.StringOut | None = None,
        iops: int | core.IntOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        snapshot_id: str | core.StringOut | None = None,
        throughput: int | core.IntOut | None = None,
        volume_size: int | core.IntOut | None = None,
        volume_type: str | core.StringOut | None = None,
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
        delete_on_termination: str | core.StringOut | None = core.arg(default=None)

        encrypted: str | core.StringOut | None = core.arg(default=None)

        iops: int | core.IntOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        snapshot_id: str | core.StringOut | None = core.arg(default=None)

        throughput: int | core.IntOut | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)

        volume_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class BlockDeviceMapping(core.Schema):

    device_name: str | core.StringOut | None = core.attr(str, default=None)

    ebs: Ebs | None = core.attr(Ebs, default=None)

    no_device: bool | core.BoolOut | None = core.attr(bool, default=None)

    virtual_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: str | core.StringOut | None = None,
        ebs: Ebs | None = None,
        no_device: bool | core.BoolOut | None = None,
        virtual_name: str | core.StringOut | None = None,
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
        device_name: str | core.StringOut | None = core.arg(default=None)

        ebs: Ebs | None = core.arg(default=None)

        no_device: bool | core.BoolOut | None = core.arg(default=None)

        virtual_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InstanceConfiguration(core.Schema):

    block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[
        BlockDeviceMapping
    ] | None = core.attr(BlockDeviceMapping, default=None, kind=core.Kind.array)

    image: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        block_device_mapping: list[BlockDeviceMapping]
        | core.ArrayOut[BlockDeviceMapping]
        | None = None,
        image: str | core.StringOut | None = None,
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
        ] | None = core.arg(default=None)

        image: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetRepository(core.Schema):

    repository_name: str | core.StringOut = core.attr(str)

    service: str | core.StringOut = core.attr(str)

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


@core.resource(type="aws_imagebuilder_container_recipe", namespace="imagebuilder")
class ContainerRecipe(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the container recipe.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Ordered configuration block(s) with components for the container recipe. Detailed below.
    """
    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, kind=core.Kind.array
    )

    """
    (Required) The type of the container to create. Valid values: `DOCKER`.
    """
    container_type: str | core.StringOut = core.attr(str)

    """
    Date the container recipe was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the container recipe.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Dockerfile template used to build the image as an inline data blob.
    """
    dockerfile_template_data: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The Amazon S3 URI for the Dockerfile that will be used to build the container image.
    """
    dockerfile_template_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to encrypt the volume. Defaults to unset, which is the value inherited from the p
    arent image.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block used to configure an instance for building and testing container imag
    es. Detailed below.
    """
    instance_configuration: InstanceConfiguration | None = core.attr(
        InstanceConfiguration, default=None
    )

    """
    (Optional) The KMS key used to encrypt the container image.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the container recipe.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Owner of the container recipe.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    parent_image: str | core.StringOut = core.attr(str)

    """
    Platform of the container recipe.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags for the container recipe. If configured with a provider [`
    default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs
    #default_tags-configuration-block) present, tags with matching keys will overwrite those defined at
    the provider-level.
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

    target_repository: TargetRepository = core.attr(TargetRepository)

    version: str | core.StringOut = core.attr(str)

    """
    (Optional) The working directory to be used during build and test workflows.
    """
    working_directory: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        component: list[Component] | core.ArrayOut[Component],
        container_type: str | core.StringOut,
        name: str | core.StringOut,
        parent_image: str | core.StringOut,
        target_repository: TargetRepository,
        version: str | core.StringOut,
        description: str | core.StringOut | None = None,
        dockerfile_template_data: str | core.StringOut | None = None,
        dockerfile_template_uri: str | core.StringOut | None = None,
        instance_configuration: InstanceConfiguration | None = None,
        kms_key_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        working_directory: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContainerRecipe.Args(
                component=component,
                container_type=container_type,
                name=name,
                parent_image=parent_image,
                target_repository=target_repository,
                version=version,
                description=description,
                dockerfile_template_data=dockerfile_template_data,
                dockerfile_template_uri=dockerfile_template_uri,
                instance_configuration=instance_configuration,
                kms_key_id=kms_key_id,
                tags=tags,
                tags_all=tags_all,
                working_directory=working_directory,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        component: list[Component] | core.ArrayOut[Component] = core.arg()

        container_type: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        dockerfile_template_data: str | core.StringOut | None = core.arg(default=None)

        dockerfile_template_uri: str | core.StringOut | None = core.arg(default=None)

        instance_configuration: InstanceConfiguration | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parent_image: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_repository: TargetRepository = core.arg()

        version: str | core.StringOut = core.arg()

        working_directory: str | core.StringOut | None = core.arg(default=None)
