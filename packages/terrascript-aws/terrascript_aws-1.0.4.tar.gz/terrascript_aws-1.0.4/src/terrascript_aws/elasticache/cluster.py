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


@core.resource(type="aws_elasticache_cluster", namespace="elasticache")
class Cluster(core.Resource):
    """
    (Optional) Whether any database modifications are applied immediately, or during the next maintenanc
    e window. Default is `false`. See [Amazon ElastiCache Documentation for more information.](https://d
    ocs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheCluster.html).
    """

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The ARN of the created ElastiCache Cluster.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether minor version engine upgrades will be applied automatically to the unde
    rlying Cache Cluster instances during the maintenance window.
    """
    auto_minor_version_upgrade: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, u
    se `preferred_availability_zones` instead. Default: System chosen Availability Zone. Changing this v
    alue will re-create the resource.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Memcached only) Whether the nodes in this Memcached node group are created in a single Av
    ailability Zone or created across multiple Availability Zones in the cluster's region. Valid values
    for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cro
    ss-az`, `num_cache_nodes` must be greater than `1`.
    """
    az_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    List of node objects including `id`, `address`, `port` and `availability_zone`.
    """
    cache_nodes: list[CacheNodes] | core.ArrayOut[CacheNodes] = core.attr(
        CacheNodes, computed=True, kind=core.Kind.array
    )

    """
    (Memcached only) DNS name of the cache cluster without the port appended.
    """
    cluster_address: str | core.StringOut = core.attr(str, computed=True)

    cluster_id: str | core.StringOut = core.attr(str)

    """
    (Memcached only) Configuration endpoint to allow host discovery.
    """
    configuration_endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Because ElastiCache pulls the latest minor or patch for a version, this attribute returns the runnin
    g version of the cache engine.
    """
    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Redis only) Name of your final cluster snapshot. If omitted, no final snapshot will be ma
    de.
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Redis only) Specifies the destination and format of Redis [SLOWLOG](https://redis.io/comm
    ands/slowlog) or Redis [Engine Log](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Log_
    Delivery.html#Log_contents-engine-log). See the documentation on [Amazon ElastiCache](https://docs.a
    ws.amazon.com/AmazonElastiCache/latest/red-ug/Log_Delivery.html). See [Log Delivery Configuration](#
    log-delivery-configuration) below for more details.
    """
    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] | None = core.attr(LogDeliveryConfiguration, default=None, kind=core.Kind.array)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    node_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    notification_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    num_cache_nodes: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional, Memcached only) List of the Availability Zones in which cache nodes are created. If you a
    re creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are a
    ssociated with the subnets in the selected subnet group. The number of Availability Zones listed mus
    t equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use
    availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: S
    ystem chosen Availability Zones. Detecting drift of existing node availability zone is not currently
    supported. Updating this argument by itself to migrate existing node availability zones is not curr
    ently supported and will show a perpetual difference.
    """
    preferred_availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional, Required if `engine` is not specified) ID of the replication group to which this cluster
    should belong. If this parameter is specified, the cluster is added to the specified replication gro
    up as a read replica; otherwise, the cluster is a standalone primary that is not part of any replica
    tion group.
    """
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

    """
    (Optional, Redis only) Name of a snapshot from which to restore data into the new node group. Changi
    ng `snapshot_name` forces a new resource.
    """
    snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Redis only) Number of days for which ElastiCache will retain automatic cache cluster snap
    shots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot tha
    t was taken today will be retained for 5 days before being deleted. If the value of SnapshotRetentio
    nLimit is set to zero (0), backups are turned off. Please note that setting a `snapshot_retention_li
    mit` is not supported on cache.t1.micro cache nodes
    """
    snapshot_retention_limit: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Redis only) Daily time range (in UTC) during which ElastiCache will begin taking a daily
    snapshot of your cache cluster. Example: 05:00-09:00
    """
    snapshot_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
