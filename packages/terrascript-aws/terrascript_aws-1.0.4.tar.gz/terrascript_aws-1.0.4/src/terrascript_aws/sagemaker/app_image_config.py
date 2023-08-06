import terrascript.core as core


@core.schema
class FileSystemConfig(core.Schema):

    default_gid: int | core.IntOut | None = core.attr(int, default=None)

    default_uid: int | core.IntOut | None = core.attr(int, default=None)

    mount_path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_gid: int | core.IntOut | None = None,
        default_uid: int | core.IntOut | None = None,
        mount_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FileSystemConfig.Args(
                default_gid=default_gid,
                default_uid=default_uid,
                mount_path=mount_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_gid: int | core.IntOut | None = core.arg(default=None)

        default_uid: int | core.IntOut | None = core.arg(default=None)

        mount_path: str | core.StringOut | None = core.arg(default=None)


@core.schema
class KernelSpec(core.Schema):

    display_name: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        display_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=KernelSpec.Args(
                name=name,
                display_name=display_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        display_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.schema
class KernelGatewayImageConfig(core.Schema):

    file_system_config: FileSystemConfig | None = core.attr(FileSystemConfig, default=None)

    kernel_spec: KernelSpec = core.attr(KernelSpec)

    def __init__(
        self,
        *,
        kernel_spec: KernelSpec,
        file_system_config: FileSystemConfig | None = None,
    ):
        super().__init__(
            args=KernelGatewayImageConfig.Args(
                kernel_spec=kernel_spec,
                file_system_config=file_system_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_system_config: FileSystemConfig | None = core.arg(default=None)

        kernel_spec: KernelSpec = core.arg()


@core.resource(type="aws_sagemaker_app_image_config", namespace="sagemaker")
class AppImageConfig(core.Resource):
    """
    (Required) The name of the App Image Config.
    """

    app_image_config_name: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) assigned by AWS to this App Image Config.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the App Image Config.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The configuration for the file system and kernels in a SageMaker image running as a Kerne
    lGateway app. See [Kernel Gateway Image Config](#kernel-gateway-image-config) details below.
    """
    kernel_gateway_image_config: KernelGatewayImageConfig | None = core.attr(
        KernelGatewayImageConfig, default=None
    )

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

    def __init__(
        self,
        resource_name: str,
        *,
        app_image_config_name: str | core.StringOut,
        kernel_gateway_image_config: KernelGatewayImageConfig | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppImageConfig.Args(
                app_image_config_name=app_image_config_name,
                kernel_gateway_image_config=kernel_gateway_image_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_image_config_name: str | core.StringOut = core.arg()

        kernel_gateway_image_config: KernelGatewayImageConfig | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
