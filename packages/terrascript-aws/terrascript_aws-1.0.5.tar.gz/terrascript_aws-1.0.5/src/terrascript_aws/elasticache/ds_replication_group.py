import terrascript.core as core


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


@core.data(type="aws_elasticache_replication_group", namespace="elasticache")
class DsReplicationGroup(core.Data):
    """
    The Amazon Resource Name (ARN) of the created ElastiCache Replication Group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether an AuthToken (password) is enabled.
    """
    auth_token_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    A flag whether a read-only replica will be automatically promoted to read/write primary if the exist
    ing primary fails.
    """
    automatic_failover_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The configuration endpoint address to allow host discovery.
    """
    configuration_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The description of the replication group.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Redis [SLOWLOG](https://redis.io/commands/slowlog) or Redis [Engine Log](https://docs.aws.amazon.com
    /AmazonElastiCache/latest/red-ug/Log_Delivery.html#Log_contents-engine-log) delivery settings.
    """
    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] = core.attr(LogDeliveryConfiguration, computed=True, kind=core.Kind.array)

    """
    The identifiers of all the nodes that are part of this replication group.
    """
    member_clusters: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Specifies whether Multi-AZ Support is enabled for the replication group.
    """
    multi_az_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    node_type: str | core.StringOut = core.attr(str, computed=True)

    num_cache_clusters: int | core.IntOut = core.attr(int, computed=True)

    """
    Number of node groups (shards) for the replication group.
    """
    num_node_groups: int | core.IntOut = core.attr(int, computed=True)

    number_cache_clusters: int | core.IntOut = core.attr(int, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    """
    The endpoint of the primary node in this node group (shard).
    """
    primary_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The endpoint of the reader node in this node group (shard).
    """
    reader_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    Number of replica nodes in each node group.
    """
    replicas_per_node_group: int | core.IntOut = core.attr(int, computed=True)

    """
    (**Deprecated** use `description` instead) The description of the replication group.
    """
    replication_group_description: str | core.StringOut = core.attr(str, computed=True)

    replication_group_id: str | core.StringOut = core.attr(str)

    """
    The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting t
    hem.
    """
    snapshot_retention_limit: int | core.IntOut = core.attr(int, computed=True)

    """
    The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node g
    roup (shard).
    """
    snapshot_window: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        replication_group_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsReplicationGroup.Args(
                replication_group_id=replication_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replication_group_id: str | core.StringOut = core.arg()
