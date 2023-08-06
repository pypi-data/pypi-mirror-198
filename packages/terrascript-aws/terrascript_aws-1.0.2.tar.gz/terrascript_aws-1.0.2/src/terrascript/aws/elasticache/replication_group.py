import terrascript.core as core


@core.schema
class ClusterMode(core.Schema):

    num_node_groups: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    replicas_per_node_group: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        num_node_groups: int | core.IntOut | None = None,
        replicas_per_node_group: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ClusterMode.Args(
                num_node_groups=num_node_groups,
                replicas_per_node_group=replicas_per_node_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        num_node_groups: int | core.IntOut | None = core.arg(default=None)

        replicas_per_node_group: int | core.IntOut | None = core.arg(default=None)


@core.schema
class LogDeliveryConfiguration(core.Schema):

    destination: str | core.StringOut = core.attr(str)

    destination_type: str | core.StringOut = core.attr(str)

    log_format: str | core.StringOut = core.attr(str)

    log_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination: str | core.StringOut,
        destination_type: str | core.StringOut,
        log_format: str | core.StringOut,
        log_type: str | core.StringOut,
    ):
        super().__init__(
            args=LogDeliveryConfiguration.Args(
                destination=destination,
                destination_type=destination_type,
                log_format=log_format,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut = core.arg()

        destination_type: str | core.StringOut = core.arg()

        log_format: str | core.StringOut = core.arg()

        log_type: str | core.StringOut = core.arg()


@core.resource(type="aws_elasticache_replication_group", namespace="aws_elasticache")
class ReplicationGroup(core.Resource):

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    at_rest_encryption_enabled: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    auth_token: str | core.StringOut | None = core.attr(str, default=None)

    auto_minor_version_upgrade: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    automatic_failover_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cluster_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    cluster_mode: ClusterMode | None = core.attr(ClusterMode, default=None, computed=True)

    configuration_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    data_tiering_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    global_replication_group_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] | None = core.attr(LogDeliveryConfiguration, default=None, kind=core.Kind.array)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    member_clusters: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    multi_az_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    node_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    notification_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    num_cache_clusters: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    num_node_groups: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    number_cache_clusters: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None)

    preferred_cache_cluster_azs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    primary_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    reader_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    replicas_per_node_group: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    replication_group_description: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    replication_group_id: str | core.StringOut = core.attr(str)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_retention_limit: int | core.IntOut | None = core.attr(int, default=None)

    snapshot_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_encryption_enabled: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    user_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        replication_group_id: str | core.StringOut,
        apply_immediately: bool | core.BoolOut | None = None,
        at_rest_encryption_enabled: bool | core.BoolOut | None = None,
        auth_token: str | core.StringOut | None = None,
        auto_minor_version_upgrade: str | core.StringOut | None = None,
        automatic_failover_enabled: bool | core.BoolOut | None = None,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cluster_mode: ClusterMode | None = None,
        data_tiering_enabled: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        global_replication_group_id: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        log_delivery_configuration: list[LogDeliveryConfiguration]
        | core.ArrayOut[LogDeliveryConfiguration]
        | None = None,
        maintenance_window: str | core.StringOut | None = None,
        multi_az_enabled: bool | core.BoolOut | None = None,
        node_type: str | core.StringOut | None = None,
        notification_topic_arn: str | core.StringOut | None = None,
        num_cache_clusters: int | core.IntOut | None = None,
        num_node_groups: int | core.IntOut | None = None,
        number_cache_clusters: int | core.IntOut | None = None,
        parameter_group_name: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_cache_cluster_azs: list[str] | core.ArrayOut[core.StringOut] | None = None,
        replicas_per_node_group: int | core.IntOut | None = None,
        replication_group_description: str | core.StringOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_name: str | core.StringOut | None = None,
        snapshot_retention_limit: int | core.IntOut | None = None,
        snapshot_window: str | core.StringOut | None = None,
        subnet_group_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_encryption_enabled: bool | core.BoolOut | None = None,
        user_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationGroup.Args(
                replication_group_id=replication_group_id,
                apply_immediately=apply_immediately,
                at_rest_encryption_enabled=at_rest_encryption_enabled,
                auth_token=auth_token,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                automatic_failover_enabled=automatic_failover_enabled,
                availability_zones=availability_zones,
                cluster_mode=cluster_mode,
                data_tiering_enabled=data_tiering_enabled,
                description=description,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                global_replication_group_id=global_replication_group_id,
                kms_key_id=kms_key_id,
                log_delivery_configuration=log_delivery_configuration,
                maintenance_window=maintenance_window,
                multi_az_enabled=multi_az_enabled,
                node_type=node_type,
                notification_topic_arn=notification_topic_arn,
                num_cache_clusters=num_cache_clusters,
                num_node_groups=num_node_groups,
                number_cache_clusters=number_cache_clusters,
                parameter_group_name=parameter_group_name,
                port=port,
                preferred_cache_cluster_azs=preferred_cache_cluster_azs,
                replicas_per_node_group=replicas_per_node_group,
                replication_group_description=replication_group_description,
                security_group_ids=security_group_ids,
                security_group_names=security_group_names,
                snapshot_arns=snapshot_arns,
                snapshot_name=snapshot_name,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                transit_encryption_enabled=transit_encryption_enabled,
                user_group_ids=user_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        at_rest_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        auth_token: str | core.StringOut | None = core.arg(default=None)

        auto_minor_version_upgrade: str | core.StringOut | None = core.arg(default=None)

        automatic_failover_enabled: bool | core.BoolOut | None = core.arg(default=None)

        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cluster_mode: ClusterMode | None = core.arg(default=None)

        data_tiering_enabled: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        global_replication_group_id: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
            LogDeliveryConfiguration
        ] | None = core.arg(default=None)

        maintenance_window: str | core.StringOut | None = core.arg(default=None)

        multi_az_enabled: bool | core.BoolOut | None = core.arg(default=None)

        node_type: str | core.StringOut | None = core.arg(default=None)

        notification_topic_arn: str | core.StringOut | None = core.arg(default=None)

        num_cache_clusters: int | core.IntOut | None = core.arg(default=None)

        num_node_groups: int | core.IntOut | None = core.arg(default=None)

        number_cache_clusters: int | core.IntOut | None = core.arg(default=None)

        parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_cache_cluster_azs: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        replicas_per_node_group: int | core.IntOut | None = core.arg(default=None)

        replication_group_description: str | core.StringOut | None = core.arg(default=None)

        replication_group_id: str | core.StringOut = core.arg()

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        snapshot_name: str | core.StringOut | None = core.arg(default=None)

        snapshot_retention_limit: int | core.IntOut | None = core.arg(default=None)

        snapshot_window: str | core.StringOut | None = core.arg(default=None)

        subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_encryption_enabled: bool | core.BoolOut | None = core.arg(default=None)

        user_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
