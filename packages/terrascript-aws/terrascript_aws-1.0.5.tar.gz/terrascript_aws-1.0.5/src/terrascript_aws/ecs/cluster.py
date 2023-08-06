import terrascript.core as core


@core.schema
class LogConfiguration(core.Schema):

    cloud_watch_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    cloud_watch_log_group_name: str | core.StringOut | None = core.attr(str, default=None)

    s3_bucket_encryption_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    s3_bucket_name: str | core.StringOut | None = core.attr(str, default=None)

    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cloud_watch_encryption_enabled: bool | core.BoolOut | None = None,
        cloud_watch_log_group_name: str | core.StringOut | None = None,
        s3_bucket_encryption_enabled: bool | core.BoolOut | None = None,
        s3_bucket_name: str | core.StringOut | None = None,
        s3_key_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LogConfiguration.Args(
                cloud_watch_encryption_enabled=cloud_watch_encryption_enabled,
                cloud_watch_log_group_name=cloud_watch_log_group_name,
                s3_bucket_encryption_enabled=s3_bucket_encryption_enabled,
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        cloud_watch_log_group_name: str | core.StringOut | None = core.arg(default=None)

        s3_bucket_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        s3_bucket_name: str | core.StringOut | None = core.arg(default=None)

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ExecuteCommandConfiguration(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    log_configuration: LogConfiguration | None = core.attr(LogConfiguration, default=None)

    logging: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_id: str | core.StringOut | None = None,
        log_configuration: LogConfiguration | None = None,
        logging: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ExecuteCommandConfiguration.Args(
                kms_key_id=kms_key_id,
                log_configuration=log_configuration,
                logging=logging,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        log_configuration: LogConfiguration | None = core.arg(default=None)

        logging: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    execute_command_configuration: ExecuteCommandConfiguration | None = core.attr(
        ExecuteCommandConfiguration, default=None
    )

    def __init__(
        self,
        *,
        execute_command_configuration: ExecuteCommandConfiguration | None = None,
    ):
        super().__init__(
            args=Configuration.Args(
                execute_command_configuration=execute_command_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execute_command_configuration: ExecuteCommandConfiguration | None = core.arg(default=None)


@core.schema
class DefaultCapacityProviderStrategy(core.Schema):

    base: int | core.IntOut | None = core.attr(int, default=None)

    capacity_provider: str | core.StringOut = core.attr(str)

    weight: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        capacity_provider: str | core.StringOut,
        base: int | core.IntOut | None = None,
        weight: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DefaultCapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                base=base,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: int | core.IntOut | None = core.arg(default=None)

        capacity_provider: str | core.StringOut = core.arg()

        weight: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Setting(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Setting.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_ecs_cluster", namespace="ecs")
class Cluster(core.Resource):
    """
    ARN that identifies the cluster.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, **Deprecated** use the `aws_ecs_cluster_capacity_providers` resource instead) List of sho
    rt names of one or more capacity providers to associate with the cluster. Valid values also include
    FARGATE` and `FARGATE_SPOT`.
    """
    capacity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The execute command configuration for the cluster. Detailed below.
    """
    configuration: Configuration | None = core.attr(Configuration, default=None)

    """
    (Optional, **Deprecated** use the `aws_ecs_cluster_capacity_providers` resource instead) Configurati
    on block for capacity provider strategy to use by default for the cluster. Can be one or more. Detai
    led below.
    """
    default_capacity_provider_strategy: list[DefaultCapacityProviderStrategy] | core.ArrayOut[
        DefaultCapacityProviderStrategy
    ] | None = core.attr(
        DefaultCapacityProviderStrategy, default=None, computed=True, kind=core.Kind.array
    )

    """
    ARN that identifies the cluster.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block(s) with cluster settings. For example, this can be used to enable Clo
    udWatch Container Insights for a cluster. Detailed below.
    """
    setting: list[Setting] | core.ArrayOut[Setting] | None = core.attr(
        Setting, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        capacity_providers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        configuration: Configuration | None = None,
        default_capacity_provider_strategy: list[DefaultCapacityProviderStrategy]
        | core.ArrayOut[DefaultCapacityProviderStrategy]
        | None = None,
        setting: list[Setting] | core.ArrayOut[Setting] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                capacity_providers=capacity_providers,
                configuration=configuration,
                default_capacity_provider_strategy=default_capacity_provider_strategy,
                setting=setting,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        configuration: Configuration | None = core.arg(default=None)

        default_capacity_provider_strategy: list[DefaultCapacityProviderStrategy] | core.ArrayOut[
            DefaultCapacityProviderStrategy
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        setting: list[Setting] | core.ArrayOut[Setting] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
