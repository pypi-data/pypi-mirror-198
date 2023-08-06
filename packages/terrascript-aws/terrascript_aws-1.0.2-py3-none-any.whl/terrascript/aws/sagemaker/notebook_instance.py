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


@core.resource(type="aws_sagemaker_notebook_instance", namespace="aws_sagemaker")
class NotebookInstance(core.Resource):

    accelerator_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    additional_code_repositories: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_code_repository: str | core.StringOut | None = core.attr(str, default=None)

    direct_internet_access: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_metadata_service_configuration: InstanceMetadataServiceConfiguration | None = (
        core.attr(InstanceMetadataServiceConfiguration, default=None)
    )

    instance_type: str | core.StringOut = core.attr(str)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    lifecycle_config_name: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    platform_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    role_arn: str | core.StringOut = core.attr(str)

    root_access: str | core.StringOut | None = core.attr(str, default=None)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: str | core.StringOut = core.attr(str, computed=True)

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
