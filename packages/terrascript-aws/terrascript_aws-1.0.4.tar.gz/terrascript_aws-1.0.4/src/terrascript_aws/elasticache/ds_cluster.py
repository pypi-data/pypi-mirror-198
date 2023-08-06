import terrascript.core as core


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


@core.schema
class LogDeliveryConfiguration(core.Schema):

    destination: str | core.StringOut = core.attr(str, computed=True)

    destination_type: str | core.StringOut = core.attr(str, computed=True)

    log_format: str | core.StringOut = core.attr(str, computed=True)

    log_type: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_elasticache_cluster", namespace="elasticache")
class DsCluster(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Availability Zone for the cache cluster.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    List of node objects including `id`, `address`, `port` and `availability_zone`.
    """
    cache_nodes: list[CacheNodes] | core.ArrayOut[CacheNodes] = core.attr(
        CacheNodes, computed=True, kind=core.Kind.array
    )

    """
    (Memcached only) The DNS name of the cache cluster without the port appended.
    """
    cluster_address: str | core.StringOut = core.attr(str, computed=True)

    cluster_id: str | core.StringOut = core.attr(str)

    """
    (Memcached only) The configuration endpoint to allow host discovery.
    """
    configuration_endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Redis [SLOWLOG](https://redis.io/commands/slowlog) or Redis [Engine Log](https://docs.aws.amazon.com
    /AmazonElastiCache/latest/red-ug/Log_Delivery.html#Log_contents-engine-log) delivery settings.
    """
    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] = core.attr(LogDeliveryConfiguration, computed=True, kind=core.Kind.array)

    maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    node_type: str | core.StringOut = core.attr(str, computed=True)

    notification_topic_arn: str | core.StringOut = core.attr(str, computed=True)

    num_cache_nodes: int | core.IntOut = core.attr(int, computed=True)

    parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    """
    The replication group to which this cache cluster belongs.
    """
    replication_group_id: str | core.StringOut = core.attr(str, computed=True)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The number of days for which ElastiCache will
    """
    snapshot_retention_limit: int | core.IntOut = core.attr(int, computed=True)

    """
    The daily time range (in UTC) during which ElastiCache will
    """
    snapshot_window: str | core.StringOut = core.attr(str, computed=True)

    subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The tags assigned to the resource
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_id=cluster_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
