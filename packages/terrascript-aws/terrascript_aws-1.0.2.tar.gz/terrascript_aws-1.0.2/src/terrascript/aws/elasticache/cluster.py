import terrascript.core as core


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


@core.schema
class CacheNodes(core.Schema):

    address: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        availability_zone: str | core.StringOut,
        id: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=CacheNodes.Args(
                address=address,
                availability_zone=availability_zone,
                id=id,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        availability_zone: str | core.StringOut = core.arg()

        id: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.resource(type="aws_elasticache_cluster", namespace="aws_elasticache")
class Cluster(core.Resource):

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_minor_version_upgrade: str | core.StringOut | None = core.attr(str, default=None)

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    az_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cache_nodes: list[CacheNodes] | core.ArrayOut[CacheNodes] = core.attr(
        CacheNodes, computed=True, kind=core.Kind.array
    )

    cluster_address: str | core.StringOut = core.attr(str, computed=True)

    cluster_id: str | core.StringOut = core.attr(str)

    configuration_endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] | None = core.attr(LogDeliveryConfiguration, default=None, kind=core.Kind.array)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    node_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    notification_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    num_cache_nodes: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    preferred_availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    replication_group_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: str | core.StringOut,
        apply_immediately: bool | core.BoolOut | None = None,
        auto_minor_version_upgrade: str | core.StringOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        az_mode: str | core.StringOut | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        log_delivery_configuration: list[LogDeliveryConfiguration]
        | core.ArrayOut[LogDeliveryConfiguration]
        | None = None,
        maintenance_window: str | core.StringOut | None = None,
        node_type: str | core.StringOut | None = None,
        notification_topic_arn: str | core.StringOut | None = None,
        num_cache_nodes: int | core.IntOut | None = None,
        parameter_group_name: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        replication_group_id: str | core.StringOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_name: str | core.StringOut | None = None,
        snapshot_retention_limit: int | core.IntOut | None = None,
        snapshot_window: str | core.StringOut | None = None,
        subnet_group_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                cluster_id=cluster_id,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                az_mode=az_mode,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                log_delivery_configuration=log_delivery_configuration,
                maintenance_window=maintenance_window,
                node_type=node_type,
                notification_topic_arn=notification_topic_arn,
                num_cache_nodes=num_cache_nodes,
                parameter_group_name=parameter_group_name,
                port=port,
                preferred_availability_zones=preferred_availability_zones,
                replication_group_id=replication_group_id,
                security_group_ids=security_group_ids,
                security_group_names=security_group_names,
                snapshot_arns=snapshot_arns,
                snapshot_name=snapshot_name,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        auto_minor_version_upgrade: str | core.StringOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        az_mode: str | core.StringOut | None = core.arg(default=None)

        cluster_id: str | core.StringOut = core.arg()

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
            LogDeliveryConfiguration
        ] | None = core.arg(default=None)

        maintenance_window: str | core.StringOut | None = core.arg(default=None)

        node_type: str | core.StringOut | None = core.arg(default=None)

        notification_topic_arn: str | core.StringOut | None = core.arg(default=None)

        num_cache_nodes: int | core.IntOut | None = core.arg(default=None)

        parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        replication_group_id: str | core.StringOut | None = core.arg(default=None)

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
