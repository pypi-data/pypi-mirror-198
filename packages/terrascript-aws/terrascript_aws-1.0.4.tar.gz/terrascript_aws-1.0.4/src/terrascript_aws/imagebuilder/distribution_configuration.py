import terrascript.core as core


@core.schema
class LaunchPermission(core.Schema):

    organization_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    organizational_unit_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    user_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        organization_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        organizational_unit_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        user_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        user_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=LaunchPermission.Args(
                organization_arns=organization_arns,
                organizational_unit_arns=organizational_unit_arns,
                user_groups=user_groups,
                user_ids=user_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        organization_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        organizational_unit_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        user_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        user_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AmiDistributionConfiguration(core.Schema):

    ami_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    launch_permission: LaunchPermission | None = core.attr(LaunchPermission, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    target_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ami_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        launch_permission: LaunchPermission | None = None,
        name: str | core.StringOut | None = None,
        target_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AmiDistributionConfiguration.Args(
                ami_tags=ami_tags,
                description=description,
                kms_key_id=kms_key_id,
                launch_permission=launch_permission,
                name=name,
                target_account_ids=target_account_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        launch_permission: LaunchPermission | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        target_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


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


@core.schema
class ContainerDistributionConfiguration(core.Schema):

    container_tags: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    target_repository: TargetRepository = core.attr(TargetRepository)

    def __init__(
        self,
        *,
        target_repository: TargetRepository,
        container_tags: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ContainerDistributionConfiguration.Args(
                target_repository=target_repository,
                container_tags=container_tags,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_tags: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        target_repository: TargetRepository = core.arg()


@core.schema
class LaunchTemplate(core.Schema):

    launch_template_id: str | core.StringOut | None = core.attr(str, default=None)

    launch_template_name: str | core.StringOut | None = core.attr(str, default=None)

    launch_template_version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        launch_template_id: str | core.StringOut | None = None,
        launch_template_name: str | core.StringOut | None = None,
        launch_template_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
                launch_template_version=launch_template_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: str | core.StringOut | None = core.arg(default=None)

        launch_template_name: str | core.StringOut | None = core.arg(default=None)

        launch_template_version: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SnapshotConfiguration(core.Schema):

    target_resource_count: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        target_resource_count: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SnapshotConfiguration.Args(
                target_resource_count=target_resource_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_resource_count: int | core.IntOut | None = core.arg(default=None)


@core.schema
class FastLaunchConfiguration(core.Schema):

    account_id: str | core.StringOut = core.attr(str)

    enabled: bool | core.BoolOut = core.attr(bool)

    launch_template: LaunchTemplate | None = core.attr(LaunchTemplate, default=None)

    max_parallel_launches: int | core.IntOut | None = core.attr(int, default=None)

    snapshot_configuration: SnapshotConfiguration | None = core.attr(
        SnapshotConfiguration, default=None
    )

    def __init__(
        self,
        *,
        account_id: str | core.StringOut,
        enabled: bool | core.BoolOut,
        launch_template: LaunchTemplate | None = None,
        max_parallel_launches: int | core.IntOut | None = None,
        snapshot_configuration: SnapshotConfiguration | None = None,
    ):
        super().__init__(
            args=FastLaunchConfiguration.Args(
                account_id=account_id,
                enabled=enabled,
                launch_template=launch_template,
                max_parallel_launches=max_parallel_launches,
                snapshot_configuration=snapshot_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()

        launch_template: LaunchTemplate | None = core.arg(default=None)

        max_parallel_launches: int | core.IntOut | None = core.arg(default=None)

        snapshot_configuration: SnapshotConfiguration | None = core.arg(default=None)


@core.schema
class LaunchTemplateConfiguration(core.Schema):

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    default: bool | core.BoolOut | None = core.attr(bool, default=None)

    launch_template_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        launch_template_id: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        default: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplateConfiguration.Args(
                launch_template_id=launch_template_id,
                account_id=account_id,
                default=default,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut | None = core.arg(default=None)

        default: bool | core.BoolOut | None = core.arg(default=None)

        launch_template_id: str | core.StringOut = core.arg()


@core.schema
class Distribution(core.Schema):

    ami_distribution_configuration: AmiDistributionConfiguration | None = core.attr(
        AmiDistributionConfiguration, default=None
    )

    container_distribution_configuration: ContainerDistributionConfiguration | None = core.attr(
        ContainerDistributionConfiguration, default=None
    )

    fast_launch_configuration: list[FastLaunchConfiguration] | core.ArrayOut[
        FastLaunchConfiguration
    ] | None = core.attr(FastLaunchConfiguration, default=None, kind=core.Kind.array)

    launch_template_configuration: list[LaunchTemplateConfiguration] | core.ArrayOut[
        LaunchTemplateConfiguration
    ] | None = core.attr(LaunchTemplateConfiguration, default=None, kind=core.Kind.array)

    license_configuration_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    region: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        region: str | core.StringOut,
        ami_distribution_configuration: AmiDistributionConfiguration | None = None,
        container_distribution_configuration: ContainerDistributionConfiguration | None = None,
        fast_launch_configuration: list[FastLaunchConfiguration]
        | core.ArrayOut[FastLaunchConfiguration]
        | None = None,
        launch_template_configuration: list[LaunchTemplateConfiguration]
        | core.ArrayOut[LaunchTemplateConfiguration]
        | None = None,
        license_configuration_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Distribution.Args(
                region=region,
                ami_distribution_configuration=ami_distribution_configuration,
                container_distribution_configuration=container_distribution_configuration,
                fast_launch_configuration=fast_launch_configuration,
                launch_template_configuration=launch_template_configuration,
                license_configuration_arns=license_configuration_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_distribution_configuration: AmiDistributionConfiguration | None = core.arg(default=None)

        container_distribution_configuration: ContainerDistributionConfiguration | None = core.arg(
            default=None
        )

        fast_launch_configuration: list[FastLaunchConfiguration] | core.ArrayOut[
            FastLaunchConfiguration
        ] | None = core.arg(default=None)

        launch_template_configuration: list[LaunchTemplateConfiguration] | core.ArrayOut[
            LaunchTemplateConfiguration
        ] | None = core.arg(default=None)

        license_configuration_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        region: str | core.StringOut = core.arg()


@core.resource(type="aws_imagebuilder_distribution_configuration", namespace="imagebuilder")
class DistributionConfiguration(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the distribution configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the distribution configuration was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the distribution configuration was updated.
    """
    date_updated: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the distribution configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) One or more configuration blocks with distribution settings. Detailed below.
    """
    distribution: list[Distribution] | core.ArrayOut[Distribution] = core.attr(
        Distribution, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the distribution configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags for the distribution configuration. If configured with a p
    rovider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/l
    atest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those d
    efined at the provider-level.
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
        distribution: list[Distribution] | core.ArrayOut[Distribution],
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DistributionConfiguration.Args(
                distribution=distribution,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        distribution: list[Distribution] | core.ArrayOut[Distribution] = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
