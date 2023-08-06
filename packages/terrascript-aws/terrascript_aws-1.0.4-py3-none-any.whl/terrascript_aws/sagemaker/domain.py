import terrascript.core as core


@core.schema
class RetentionPolicy(core.Schema):

    home_efs_file_system: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        home_efs_file_system: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=RetentionPolicy.Args(
                home_efs_file_system=home_efs_file_system,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        home_efs_file_system: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SharingSettings(core.Schema):

    notebook_output_option: str | core.StringOut | None = core.attr(str, default=None)

    s3_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    s3_output_path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        notebook_output_option: str | core.StringOut | None = None,
        s3_kms_key_id: str | core.StringOut | None = None,
        s3_output_path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SharingSettings.Args(
                notebook_output_option=notebook_output_option,
                s3_kms_key_id=s3_kms_key_id,
                s3_output_path=s3_output_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notebook_output_option: str | core.StringOut | None = core.arg(default=None)

        s3_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        s3_output_path: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DefaultResourceSpec(core.Schema):

    instance_type: str | core.StringOut | None = core.attr(str, default=None)

    lifecycle_config_arn: str | core.StringOut | None = core.attr(str, default=None)

    sagemaker_image_arn: str | core.StringOut | None = core.attr(str, default=None)

    sagemaker_image_version_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_type: str | core.StringOut | None = None,
        lifecycle_config_arn: str | core.StringOut | None = None,
        sagemaker_image_arn: str | core.StringOut | None = None,
        sagemaker_image_version_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DefaultResourceSpec.Args(
                instance_type=instance_type,
                lifecycle_config_arn=lifecycle_config_arn,
                sagemaker_image_arn=sagemaker_image_arn,
                sagemaker_image_version_arn=sagemaker_image_version_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: str | core.StringOut | None = core.arg(default=None)

        lifecycle_config_arn: str | core.StringOut | None = core.arg(default=None)

        sagemaker_image_arn: str | core.StringOut | None = core.arg(default=None)

        sagemaker_image_version_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TensorBoardAppSettings(core.Schema):

    default_resource_spec: DefaultResourceSpec | None = core.attr(DefaultResourceSpec, default=None)

    def __init__(
        self,
        *,
        default_resource_spec: DefaultResourceSpec | None = None,
    ):
        super().__init__(
            args=TensorBoardAppSettings.Args(
                default_resource_spec=default_resource_spec,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_resource_spec: DefaultResourceSpec | None = core.arg(default=None)


@core.schema
class JupyterServerAppSettings(core.Schema):

    default_resource_spec: DefaultResourceSpec | None = core.attr(DefaultResourceSpec, default=None)

    lifecycle_config_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        default_resource_spec: DefaultResourceSpec | None = None,
        lifecycle_config_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=JupyterServerAppSettings.Args(
                default_resource_spec=default_resource_spec,
                lifecycle_config_arns=lifecycle_config_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_resource_spec: DefaultResourceSpec | None = core.arg(default=None)

        lifecycle_config_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class CustomImage(core.Schema):

    app_image_config_name: str | core.StringOut = core.attr(str)

    image_name: str | core.StringOut = core.attr(str)

    image_version_number: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        app_image_config_name: str | core.StringOut,
        image_name: str | core.StringOut,
        image_version_number: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CustomImage.Args(
                app_image_config_name=app_image_config_name,
                image_name=image_name,
                image_version_number=image_version_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        app_image_config_name: str | core.StringOut = core.arg()

        image_name: str | core.StringOut = core.arg()

        image_version_number: int | core.IntOut | None = core.arg(default=None)


@core.schema
class KernelGatewayAppSettings(core.Schema):

    custom_image: list[CustomImage] | core.ArrayOut[CustomImage] | None = core.attr(
        CustomImage, default=None, kind=core.Kind.array
    )

    default_resource_spec: DefaultResourceSpec | None = core.attr(DefaultResourceSpec, default=None)

    lifecycle_config_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        custom_image: list[CustomImage] | core.ArrayOut[CustomImage] | None = None,
        default_resource_spec: DefaultResourceSpec | None = None,
        lifecycle_config_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=KernelGatewayAppSettings.Args(
                custom_image=custom_image,
                default_resource_spec=default_resource_spec,
                lifecycle_config_arns=lifecycle_config_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_image: list[CustomImage] | core.ArrayOut[CustomImage] | None = core.arg(default=None)

        default_resource_spec: DefaultResourceSpec | None = core.arg(default=None)

        lifecycle_config_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class DefaultUserSettings(core.Schema):

    execution_role: str | core.StringOut = core.attr(str)

    jupyter_server_app_settings: JupyterServerAppSettings | None = core.attr(
        JupyterServerAppSettings, default=None
    )

    kernel_gateway_app_settings: KernelGatewayAppSettings | None = core.attr(
        KernelGatewayAppSettings, default=None
    )

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    sharing_settings: SharingSettings | None = core.attr(SharingSettings, default=None)

    tensor_board_app_settings: TensorBoardAppSettings | None = core.attr(
        TensorBoardAppSettings, default=None
    )

    def __init__(
        self,
        *,
        execution_role: str | core.StringOut,
        jupyter_server_app_settings: JupyterServerAppSettings | None = None,
        kernel_gateway_app_settings: KernelGatewayAppSettings | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        sharing_settings: SharingSettings | None = None,
        tensor_board_app_settings: TensorBoardAppSettings | None = None,
    ):
        super().__init__(
            args=DefaultUserSettings.Args(
                execution_role=execution_role,
                jupyter_server_app_settings=jupyter_server_app_settings,
                kernel_gateway_app_settings=kernel_gateway_app_settings,
                security_groups=security_groups,
                sharing_settings=sharing_settings,
                tensor_board_app_settings=tensor_board_app_settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execution_role: str | core.StringOut = core.arg()

        jupyter_server_app_settings: JupyterServerAppSettings | None = core.arg(default=None)

        kernel_gateway_app_settings: KernelGatewayAppSettings | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        sharing_settings: SharingSettings | None = core.arg(default=None)

        tensor_board_app_settings: TensorBoardAppSettings | None = core.arg(default=None)


@core.resource(type="aws_sagemaker_domain", namespace="sagemaker")
class Domain(core.Resource):
    """
    (Optional) Specifies the VPC used for non-EFS traffic. The default value is `PublicInternetOnly`. Va
    lid values are `PublicInternetOnly` and `VpcOnly`.
    """

    app_network_access_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) assigned by AWS to this Domain.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The mode of authentication that members use to access the domain. Valid values are `IAM`
    and `SSO`.
    """
    auth_mode: str | core.StringOut = core.attr(str)

    """
    (Required) The default user settings. See [Default User Settings](#default-user-settings) below.
    """
    default_user_settings: DefaultUserSettings = core.attr(DefaultUserSettings)

    """
    (Required) The domain name.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    The ID of the Amazon Elastic File System (EFS) managed by this Domain.
    """
    home_efs_file_system_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the Domain.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The AWS KMS customer managed CMK used to encrypt the EFS volume attached to the domain.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The retention policy for this domain, which specifies whether resources will be retained
    after the Domain is deleted. By default, all resources are retained. See [Retention Policy](#retenti
    on-policy) below.
    """
    retention_policy: RetentionPolicy | None = core.attr(RetentionPolicy, default=None)

    """
    The SSO managed application instance ID.
    """
    single_sign_on_managed_application_instance_id: str | core.StringOut = core.attr(
        str, computed=True
    )

    """
    (Required) The VPC subnets that Studio uses for communication.
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

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

    """
    The domain's URL.
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Amazon Virtual Private Cloud (VPC) that Studio uses for communication.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_mode: str | core.StringOut,
        default_user_settings: DefaultUserSettings,
        domain_name: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        app_network_access_type: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        retention_policy: RetentionPolicy | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                auth_mode=auth_mode,
                default_user_settings=default_user_settings,
                domain_name=domain_name,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                app_network_access_type=app_network_access_type,
                kms_key_id=kms_key_id,
                retention_policy=retention_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_network_access_type: str | core.StringOut | None = core.arg(default=None)

        auth_mode: str | core.StringOut = core.arg()

        default_user_settings: DefaultUserSettings = core.arg()

        domain_name: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        retention_policy: RetentionPolicy | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
