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
class SystemsManagerAgent(core.Schema):

    uninstall_after_build: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        uninstall_after_build: bool | core.BoolOut,
    ):
        super().__init__(
            args=SystemsManagerAgent.Args(
                uninstall_after_build=uninstall_after_build,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        uninstall_after_build: bool | core.BoolOut = core.arg()


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


@core.resource(type="aws_imagebuilder_image_recipe", namespace="imagebuilder")
class ImageRecipe(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the image recipe.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block(s) with block device mappings for the image recipe. Detailed below.
    """
    block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[
        BlockDeviceMapping
    ] | None = core.attr(BlockDeviceMapping, default=None, kind=core.Kind.array)

    """
    (Required) Ordered configuration block(s) with components for the image recipe. Detailed below.
    """
    component: list[Component] | core.ArrayOut[Component] = core.attr(
        Component, kind=core.Kind.array
    )

    """
    Date the image recipe was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the image recipe.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the image recipe.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Owner of the image recipe.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Platform of the image recipe.
    """
    parent_image: str | core.StringOut = core.attr(str)

    """
    Platform of the image recipe.
    """
    platform: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for the Systems Manager Agent installed by default by Image Builder.
    Detailed below.
    """
    systems_manager_agent: SystemsManagerAgent | None = core.attr(
        SystemsManagerAgent, default=None, computed=True
    )

    """
    (Optional) Key-value map of resource tags for the image recipe. If configured with a provider [`defa
    ult_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#def
    ault_tags-configuration-block) present, tags with matching keys will overwrite those defined at the
    provider-level.
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

    user_data_base64: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Version of the image recipe.
    """
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
        name: str | core.StringOut,
        parent_image: str | core.StringOut,
        version: str | core.StringOut,
        block_device_mapping: list[BlockDeviceMapping]
        | core.ArrayOut[BlockDeviceMapping]
        | None = None,
        description: str | core.StringOut | None = None,
        systems_manager_agent: SystemsManagerAgent | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_data_base64: str | core.StringOut | None = None,
        working_directory: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImageRecipe.Args(
                component=component,
                name=name,
                parent_image=parent_image,
                version=version,
                block_device_mapping=block_device_mapping,
                description=description,
                systems_manager_agent=systems_manager_agent,
                tags=tags,
                tags_all=tags_all,
                user_data_base64=user_data_base64,
                working_directory=working_directory,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_device_mapping: list[BlockDeviceMapping] | core.ArrayOut[
            BlockDeviceMapping
        ] | None = core.arg(default=None)

        component: list[Component] | core.ArrayOut[Component] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parent_image: str | core.StringOut = core.arg()

        systems_manager_agent: SystemsManagerAgent | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_data_base64: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()

        working_directory: str | core.StringOut | None = core.arg(default=None)
