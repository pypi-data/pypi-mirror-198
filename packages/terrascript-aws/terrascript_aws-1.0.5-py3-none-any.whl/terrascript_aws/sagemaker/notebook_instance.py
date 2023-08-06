import terrascript.core as core


@core.schema
class InstanceMetadataServiceConfiguration(core.Schema):

    minimum_instance_metadata_service_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        minimum_instance_metadata_service_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InstanceMetadataServiceConfiguration.Args(
                minimum_instance_metadata_service_version=minimum_instance_metadata_service_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minimum_instance_metadata_service_version: str | core.StringOut | None = core.arg(
            default=None
        )


@core.resource(type="aws_sagemaker_notebook_instance", namespace="sagemaker")
class NotebookInstance(core.Resource):
    """
    (Optional) A list of Elastic Inference (EI) instance types to associate with this notebook instance.
    See [Elastic Inference Accelerator](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html) for mo
    re details. Valid values: `ml.eia1.medium`, `ml.eia1.large`, `ml.eia1.xlarge`, `ml.eia2.medium`, `ml
    .eia2.large`, `ml.eia2.xlarge`.
    """

    accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) An array of up to three Git repositories to associate with the notebook instance.
    """
    additional_code_repositories: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Git repository associated with the notebook instance as its default code repository.
    This can be either the name of a Git repository stored as a resource in your account, or the URL of
    a Git repository in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome
    .html) or in any other Git repository.
    """
    default_code_repository: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Set to `Disabled` to disable internet access to notebook. Requires `security_groups` and
    subnet_id` to be set. Supported values: `Enabled` (Default) or `Disabled`. If set to `Disabled`, th
    e notebook instance will be able to access resources only in your VPC, and will not be able to conne
    ct to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VP
    C.
    """
    direct_internet_access: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the notebook instance.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Information on the IMDS configuration of the notebook instance. Conflicts with `instance_
    metadata_service_configuration`. see details below.
    """
    instance_metadata_service_configuration: InstanceMetadataServiceConfiguration | None = (
        core.attr(InstanceMetadataServiceConfiguration, default=None)
    )

    """
    (Required) The name of ML compute instance type.
    """
    instance_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the mo
    del artifacts at rest using Amazon S3 server-side encryption.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of a lifecycle configuration to associate with the notebook instance.
    """
    lifecycle_config_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the notebook instance (must be unique).
    """
    name: str | core.StringOut = core.attr(str)

    """
    The network interface ID that Amazon SageMaker created at the time of creating the instance. Only av
    ailable when setting `subnet_id`.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The platform identifier of the notebook instance runtime environment. This value can be e
    ither `notebook-al1-v1`, `notebook-al2-v1`, or  `notebook-al2-v2`, depending on which version of Ama
    zon Linux you require.
    """
    platform_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The ARN of the IAM role to be used by the notebook instance which allows SageMaker to cal
    l other services on your behalf.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether root access is `Enabled` or `Disabled` for users of the notebook instance. The de
    fault value is `Enabled`.
    """
    root_access: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The associated security groups.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The VPC subnet ID.
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

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
    The URL that you use to connect to the Jupyter notebook that is running in your notebook instance.
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The size, in GB, of the ML storage volume to attach to the notebook instance. The default
    value is 5 GB.
    """
    volume_size: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: str | core.StringOut,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        additional_code_repositories: list[str] | core.ArrayOut[core.StringOut] | None = None,
        default_code_repository: str | core.StringOut | None = None,
        direct_internet_access: str | core.StringOut | None = None,
        instance_metadata_service_configuration: InstanceMetadataServiceConfiguration | None = None,
        kms_key_id: str | core.StringOut | None = None,
        lifecycle_config_name: str | core.StringOut | None = None,
        platform_identifier: str | core.StringOut | None = None,
        root_access: str | core.StringOut | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        volume_size: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NotebookInstance.Args(
                instance_type=instance_type,
                name=name,
                role_arn=role_arn,
                accelerator_types=accelerator_types,
                additional_code_repositories=additional_code_repositories,
                default_code_repository=default_code_repository,
                direct_internet_access=direct_internet_access,
                instance_metadata_service_configuration=instance_metadata_service_configuration,
                kms_key_id=kms_key_id,
                lifecycle_config_name=lifecycle_config_name,
                platform_identifier=platform_identifier,
                root_access=root_access,
                security_groups=security_groups,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                volume_size=volume_size,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        additional_code_repositories: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        default_code_repository: str | core.StringOut | None = core.arg(default=None)

        direct_internet_access: str | core.StringOut | None = core.arg(default=None)

        instance_metadata_service_configuration: InstanceMetadataServiceConfiguration | None = (
            core.arg(default=None)
        )

        instance_type: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        lifecycle_config_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        platform_identifier: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        root_access: str | core.StringOut | None = core.arg(default=None)

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        volume_size: int | core.IntOut | None = core.arg(default=None)
