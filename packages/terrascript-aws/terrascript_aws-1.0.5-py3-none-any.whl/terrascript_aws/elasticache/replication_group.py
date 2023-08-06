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


@core.resource(type="aws_elasticache_replication_group", namespace="elasticache")
class ReplicationGroup(core.Resource):
    """
    (Optional) Specifies whether any modifications are applied immediately, or during the next maintenan
    ce window. Default is `false`.
    """

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    ARN of the created ElastiCache Replication Group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether to enable encryption at rest.
    """
    at_rest_encryption_enabled: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Password used to access a password protected server. Can be specified only if `transit_en
    cryption_enabled = true`.
    """
    auth_token: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether minor version engine upgrades will be applied automatically to the unde
    rlying Cache Cluster instances during the maintenance window.
    """
    auto_minor_version_upgrade: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Specifies whether a read-only replica will be automatically promoted to read/write primar
    y if the existing primary fails. If enabled, `num_cache_clusters` must be greater than 1. Must be en
    abled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
    """
    automatic_failover_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, **Deprecated** use `preferred_cache_cluster_azs` instead) List of EC2 availability zones
    in which the replication group's cache clusters will be created. The order of the availability zones
    in the list is not considered.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Indicates if cluster mode is enabled.
    """
    cluster_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional, **Deprecated** use root-level `num_node_groups` and `replicas_per_node_group` instead) Cr
    eate a native Redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode document
    ed below. Only 1 `cluster_mode` block is allowed. Note that configuring this block does not enable c
    luster mode, i.e., data sharding, this requires using a parameter group that has the parameter `clus
    ter-enabled` set to true.
    """
    cluster_mode: ClusterMode | None = core.attr(ClusterMode, default=None, computed=True)

    """
    Address of the replication group configuration endpoint when cluster mode is enabled.
    """
    configuration_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Enables data tiering. Data tiering is only supported for replication groups using the r6g
    d node type. This parameter must be set to `true` when using r6gd nodes.
    """
    data_tiering_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the cache engine to be used for the clusters in this replication group. The only
    valid value is `redis`.
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Version number of the cache engine to be used for the cache clusters in this replication
    group.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Because ElastiCache pulls the latest minor or patch for a version, this attribute returns the runnin
    g version of the cache engine.
    """
    engine_version_actual: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of your final node group (shard) snapshot. ElastiCache creates the snapshot from
    the primary node in the cluster. If omitted, no final snapshot will be made.
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of the global replication group to which this replication group should belong. If
    this parameter is specified, the replication group is added to the specified global replication grou
    p as a secondary replication group; otherwise, the replication group is not part of any global repli
    cation group. If `global_replication_group_id` is set, the `num_node_groups` parameter (or the `num_
    node_groups` parameter of the deprecated `cluster_mode` block) cannot be set.
    """
    global_replication_group_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    ID of the ElastiCache Replication Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses serv
    ice managed encryption. Can be specified only if `at_rest_encryption_enabled = true`.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Redis only) Specifies the destination and format of Redis [SLOWLOG](https://redis.io/comm
    ands/slowlog) or Redis [Engine Log](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Log_
    Delivery.html#Log_contents-engine-log). See the documentation on [Amazon ElastiCache](https://docs.a
    ws.amazon.com/AmazonElastiCache/latest/red-ug/Log_Delivery.html#Log_contents-engine-log). See [Log D
    elivery Configuration](#log-delivery-configuration) below for more details.
    """
    log_delivery_configuration: list[LogDeliveryConfiguration] | core.ArrayOut[
        LogDeliveryConfiguration
    ] | None = core.attr(LogDeliveryConfiguration, default=None, kind=core.Kind.array)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Identifiers of all the nodes that are part of this replication group.
    """
    member_clusters: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Specifies whether to enable Multi-AZ Support for the replication group. If `true`, `autom
    atic_failover_enabled` must also be enabled. Defaults to `false`.
    """
    multi_az_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Instance class to be used. See AWS documentation for information on [supported node types
    ](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html) and [g
    uidance on selecting node types](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/nodes-s
    elect-size.html). Required unless `global_replication_group_id` is set. Cannot be set if `global_rep
    lication_group_id` is set.
    """
    node_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    notification_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Number of cache clusters (primary and replicas) this replication group will have. If Mult
    i-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other mod
    ifications. Conflicts with `num_node_groups`, the deprecated`number_cache_clusters`, or the deprecat
    ed `cluster_mode`. Defaults to `1`.
    """
    num_cache_clusters: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional, **Deprecated** use root-level `num_node_groups` instead) Number of node groups (shards) f
    or this Redis replication group. Changing this number will trigger an online resizing operation befo
    re other settings modifications. Required unless `global_replication_group_id` is set.
    """
    num_node_groups: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional, **Deprecated** use `num_cache_clusters` instead) Number of cache clusters (primary and re
    plicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must b
    e at least 2. Updates will occur before other modifications. Conflicts with `num_cache_clusters`, `n
    um_node_groups`, or the deprecated `cluster_mode`. Defaults to `1`.
    """
    number_cache_clusters: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Name of the parameter group to associate with this replication group. If this argument is
    omitted, the default cache parameter group for the specified engine is used. To enable "cluster mod
    e", i.e., data sharding, use a parameter group that has the parameter `cluster-enabled` set to true.
    """
    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) List of EC2 availability zones in which the replication group's cache clusters will be cr
    eated. The order of the availability zones in the list is considered. The first item in the list wil
    l be the primary node. Ignored when updating.
    """
    preferred_cache_cluster_azs: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Redis only) Address of the endpoint for the primary node in the replication group, if the cluster m
    ode is disabled.
    """
    primary_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Redis only) Address of the endpoint for the reader node in the replication group, if the cluster mo
    de is disabled.
    """
    reader_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Required with `cluster_mode` `num_node_groups`, **Deprecated** use root-level `replicas_p
    er_node_group` instead) Number of replica nodes in each node group. Valid values are 0 to 5. Changin
    g this number will trigger an online resizing operation before other settings modifications.
    """
    replicas_per_node_group: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    replication_group_description: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    replication_group_id: str | core.StringOut = core.attr(str)

    """
    (Optional) One or more Amazon VPC security groups associated with this replication group. Use this p
    arameter only when you are creating a replication group in an Amazon Virtual Private Cloud
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) List of cache security group names to associate with this replication group.
    """
    security_group_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Name of a snapshot from which to restore data into the new node group. Changing the `snap
    shot_name` forces a new resource.
    """
    snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Redis only) Number of days for which ElastiCache will retain automatic cache cluster snap
    shots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot tha
    t was taken today will be retained for 5 days before being deleted. If the value of `snapshot_retent
    ion_limit` is set to zero (0), backups are turned off. Please note that setting a `snapshot_retentio
    n_limit` is not supported on cache.t1.micro cache nodes
    """
    snapshot_retention_limit: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Redis only) Daily time range (in UTC) during which ElastiCache will begin taking a daily
    snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-0
    9:00`
    """
    snapshot_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the cache subnet group to be used for the replication group.
    """
    subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags to assign to the resource. Adding tags to this resource will add or overwrite
    any existing tags on the clusters in the replication group and not to the group itself. If configur
    ed with a provider [`default_tags` configuration block](https://registry.terraform.io/providers/hash
    icorp/aws/latest/docs#default_tags-configuration-block) present, tags with matching keys will overwr
    ite those defined at the provider-level.
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

    """
    (Optional) Whether to enable encryption in transit.
    """
    transit_encryption_enabled: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) User Group ID to associate with the replication group. Only a maximum of one (1) user gro
    up ID is valid. **NOTE:** This argument _is_ a set because the AWS specification allows for multiple
    IDs. However, in practice, AWS only allows a maximum size of one.
    """
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
