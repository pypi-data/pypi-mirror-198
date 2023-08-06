import terrascript.core as core


@core.schema
class LaunchPermission(core.Schema):

    organization_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    organizational_unit_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    user_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    user_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        organization_arns: list[str] | core.ArrayOut[core.StringOut],
        organizational_unit_arns: list[str] | core.ArrayOut[core.StringOut],
        user_groups: list[str] | core.ArrayOut[core.StringOut],
        user_ids: list[str] | core.ArrayOut[core.StringOut],
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
        organization_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        organizational_unit_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        user_groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        user_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class AmiDistributionConfiguration(core.Schema):

    ami_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    launch_permission: list[LaunchPermission] | core.ArrayOut[LaunchPermission] = core.attr(
        LaunchPermission, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    target_account_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        description: str | core.StringOut,
        kms_key_id: str | core.StringOut,
        launch_permission: list[LaunchPermission] | core.ArrayOut[LaunchPermission],
        name: str | core.StringOut,
        target_account_ids: list[str] | core.ArrayOut[core.StringOut],
        ami_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AmiDistributionConfiguration.Args(
                description=description,
                kms_key_id=kms_key_id,
                launch_permission=launch_permission,
                name=name,
                target_account_ids=target_account_ids,
                ami_tags=ami_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut = core.arg()

        launch_permission: list[LaunchPermission] | core.ArrayOut[LaunchPermission] = core.arg()

        name: str | core.StringOut = core.arg()

        target_account_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


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


@core.schema
class ContainerDistributionConfiguration(core.Schema):

    container_tags: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    target_repository: list[TargetRepository] | core.ArrayOut[TargetRepository] = core.attr(
        TargetRepository, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        container_tags: list[str] | core.ArrayOut[core.StringOut],
        description: str | core.StringOut,
        target_repository: list[TargetRepository] | core.ArrayOut[TargetRepository],
    ):
        super().__init__(
            args=ContainerDistributionConfiguration.Args(
                container_tags=container_tags,
                description=description,
                target_repository=target_repository,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_tags: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        description: str | core.StringOut = core.arg()

        target_repository: list[TargetRepository] | core.ArrayOut[TargetRepository] = core.arg()


@core.schema
class LaunchTemplate(core.Schema):

    launch_template_id: str | core.StringOut = core.attr(str, computed=True)

    launch_template_name: str | core.StringOut = core.attr(str, computed=True)

    launch_template_version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        launch_template_id: str | core.StringOut,
        launch_template_name: str | core.StringOut,
        launch_template_version: str | core.StringOut,
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
        launch_template_id: str | core.StringOut = core.arg()

        launch_template_name: str | core.StringOut = core.arg()

        launch_template_version: str | core.StringOut = core.arg()


@core.schema
class SnapshotConfiguration(core.Schema):

    target_resource_count: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        target_resource_count: int | core.IntOut,
    ):
        super().__init__(
            args=SnapshotConfiguration.Args(
                target_resource_count=target_resource_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_resource_count: int | core.IntOut = core.arg()


@core.schema
class FastLaunchConfiguration(core.Schema):

    account_id: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    launch_template: list[LaunchTemplate] | core.ArrayOut[LaunchTemplate] = core.attr(
        LaunchTemplate, computed=True, kind=core.Kind.array
    )

    max_parallel_launches: int | core.IntOut = core.attr(int, computed=True)

    snapshot_configuration: list[SnapshotConfiguration] | core.ArrayOut[
        SnapshotConfiguration
    ] = core.attr(SnapshotConfiguration, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        account_id: str | core.StringOut,
        enabled: bool | core.BoolOut,
        launch_template: list[LaunchTemplate] | core.ArrayOut[LaunchTemplate],
        max_parallel_launches: int | core.IntOut,
        snapshot_configuration: list[SnapshotConfiguration] | core.ArrayOut[SnapshotConfiguration],
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

        launch_template: list[LaunchTemplate] | core.ArrayOut[LaunchTemplate] = core.arg()

        max_parallel_launches: int | core.IntOut = core.arg()

        snapshot_configuration: list[SnapshotConfiguration] | core.ArrayOut[
            SnapshotConfiguration
        ] = core.arg()


@core.schema
class LaunchTemplateConfiguration(core.Schema):

    account_id: str | core.StringOut = core.attr(str, computed=True)

    default: bool | core.BoolOut = core.attr(bool, computed=True)

    launch_template_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        account_id: str | core.StringOut,
        default: bool | core.BoolOut,
        launch_template_id: str | core.StringOut,
    ):
        super().__init__(
            args=LaunchTemplateConfiguration.Args(
                account_id=account_id,
                default=default,
                launch_template_id=launch_template_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut = core.arg()

        default: bool | core.BoolOut = core.arg()

        launch_template_id: str | core.StringOut = core.arg()


@core.schema
class Distribution(core.Schema):

    ami_distribution_configuration: list[AmiDistributionConfiguration] | core.ArrayOut[
        AmiDistributionConfiguration
    ] = core.attr(AmiDistributionConfiguration, computed=True, kind=core.Kind.array)

    container_distribution_configuration: list[ContainerDistributionConfiguration] | core.ArrayOut[
        ContainerDistributionConfiguration
    ] = core.attr(ContainerDistributionConfiguration, computed=True, kind=core.Kind.array)

    fast_launch_configuration: list[FastLaunchConfiguration] | core.ArrayOut[
        FastLaunchConfiguration
    ] = core.attr(FastLaunchConfiguration, computed=True, kind=core.Kind.array)

    launch_template_configuration: list[LaunchTemplateConfiguration] | core.ArrayOut[
        LaunchTemplateConfiguration
    ] = core.attr(LaunchTemplateConfiguration, computed=True, kind=core.Kind.array)

    license_configuration_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    region: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ami_distribution_configuration: list[AmiDistributionConfiguration]
        | core.ArrayOut[AmiDistributionConfiguration],
        container_distribution_configuration: list[ContainerDistributionConfiguration]
        | core.ArrayOut[ContainerDistributionConfiguration],
        fast_launch_configuration: list[FastLaunchConfiguration]
        | core.ArrayOut[FastLaunchConfiguration],
        launch_template_configuration: list[LaunchTemplateConfiguration]
        | core.ArrayOut[LaunchTemplateConfiguration],
        license_configuration_arns: list[str] | core.ArrayOut[core.StringOut],
        region: str | core.StringOut,
    ):
        super().__init__(
            args=Distribution.Args(
                ami_distribution_configuration=ami_distribution_configuration,
                container_distribution_configuration=container_distribution_configuration,
                fast_launch_configuration=fast_launch_configuration,
                launch_template_configuration=launch_template_configuration,
                license_configuration_arns=license_configuration_arns,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami_distribution_configuration: list[AmiDistributionConfiguration] | core.ArrayOut[
            AmiDistributionConfiguration
        ] = core.arg()

        container_distribution_configuration: list[
            ContainerDistributionConfiguration
        ] | core.ArrayOut[ContainerDistributionConfiguration] = core.arg()

        fast_launch_configuration: list[FastLaunchConfiguration] | core.ArrayOut[
            FastLaunchConfiguration
        ] = core.arg()

        launch_template_configuration: list[LaunchTemplateConfiguration] | core.ArrayOut[
            LaunchTemplateConfiguration
        ] = core.arg()

        license_configuration_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        region: str | core.StringOut = core.arg()


@core.data(type="aws_imagebuilder_distribution_configuration", namespace="imagebuilder")
class DsDistributionConfiguration(core.Data):
    """
    (Required) Amazon Resource Name (ARN) of the distribution configuration.
    """

    arn: str | core.StringOut = core.attr(str)

    """
    Date the distribution configuration was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    Date the distribution configuration was updated.
    """
    date_updated: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the distribution configuration.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of distributions.
    """
    distribution: list[Distribution] | core.ArrayOut[Distribution] = core.attr(
        Distribution, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the distribution configuration.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the distribution configuration.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDistributionConfiguration.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
