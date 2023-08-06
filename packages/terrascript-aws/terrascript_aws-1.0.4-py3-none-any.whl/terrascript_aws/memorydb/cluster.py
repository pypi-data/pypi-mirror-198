import terrascript.core as core


@core.schema
class Endpoint(core.Schema):

    address: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=Endpoint.Args(
                address=address,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.schema
class Nodes(core.Schema):

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    create_time: str | core.StringOut = core.attr(str, computed=True)

    endpoint: list[Endpoint] | core.ArrayOut[Endpoint] = core.attr(
        Endpoint, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zone: str | core.StringOut,
        create_time: str | core.StringOut,
        endpoint: list[Endpoint] | core.ArrayOut[Endpoint],
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Nodes.Args(
                availability_zone=availability_zone,
                create_time=create_time,
                endpoint=endpoint,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: str | core.StringOut = core.arg()

        create_time: str | core.StringOut = core.arg()

        endpoint: list[Endpoint] | core.ArrayOut[Endpoint] = core.arg()

        name: str | core.StringOut = core.arg()


@core.schema
class Shards(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    nodes: list[Nodes] | core.ArrayOut[Nodes] = core.attr(
        Nodes, computed=True, kind=core.Kind.array
    )

    num_nodes: int | core.IntOut = core.attr(int, computed=True)

    slots: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        nodes: list[Nodes] | core.ArrayOut[Nodes],
        num_nodes: int | core.IntOut,
        slots: str | core.StringOut,
    ):
        super().__init__(
            args=Shards.Args(
                name=name,
                nodes=nodes,
                num_nodes=num_nodes,
                slots=slots,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        nodes: list[Nodes] | core.ArrayOut[Nodes] = core.arg()

        num_nodes: int | core.IntOut = core.arg()

        slots: str | core.StringOut = core.arg()


@core.schema
class ClusterEndpoint(core.Schema):

    address: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        port: int | core.IntOut,
    ):
        super().__init__(
            args=ClusterEndpoint.Args(
                address=address,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()


@core.resource(type="aws_memorydb_cluster", namespace="memorydb")
class Cluster(core.Resource):
    """
    (Required) The name of the Access Control List to associate with the cluster.
    """

    acl_name: str | core.StringOut = core.attr(str)

    """
    The ARN of the cluster.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) When set to `true`, the cluster will automatically receive minor eng
    ine version upgrades after launch. Defaults to `true`.
    """
    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    cluster_endpoint: list[ClusterEndpoint] | core.ArrayOut[ClusterEndpoint] = core.attr(
        ClusterEndpoint, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Description for the cluster. Defaults to `"Managed by Terraform"`.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Patch version number of the Redis engine used by the cluster.
    """
    engine_patch_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Version number of the Redis engine to be used for the cluster. Downgrades are not support
    ed.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the final cluster snapshot to be created when this resource is deleted. If omitte
    d, no final snapshot will be made.
    """
    final_snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    Same as `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) ARN of the KMS key used to encrypt the cluster at rest.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the weekly time range during which maintenance on the cluster is performed. Spe
    cify as a range in the format `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC). The minimum maintenance win
    dow is a 60 minute period. Example: `sun:23:00-mon:01:30`.
    """
    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Name of the cluster. If omitted, Terraform will assign a random, uni
    que name. Conflicts with `name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The compute and memory capacity of the nodes in the cluster. See AWS documentation on [su
    pported node types](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.supportedtypes.html)
    as well as [vertical scaling](https://docs.aws.amazon.com/memorydb/latest/devguide/cluster-vertical-
    scaling.html).
    """
    node_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of replicas to apply to each shard, up to a maximum of 5. Defaults to `1` (i.e
    . 2 nodes per shard).
    """
    num_replicas_per_shard: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The number of shards in the cluster. Defaults to `1`.
    """
    num_shards: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The name of the parameter group associated with the cluster.
    """
    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) The port number on which each of the nodes accepts connections. Defa
    ults to `6379`.
    """
    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Set of VPC Security Group ID-s to associate with this cluster.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Set of shards in this cluster.
    """
    shards: list[Shards] | core.ArrayOut[Shards] = core.attr(
        Shards, computed=True, kind=core.Kind.array
    )

    """
    (Optional, Forces new resource) List of ARN-s that uniquely identify RDB snapshot files stored in S3
    . The snapshot files will be used to populate the new cluster. Object names in the ARN-s cannot cont
    ain any commas.
    """
    snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional, Forces new resource) The name of a snapshot from which to restore data into the new clust
    er.
    """
    snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The number of days for which MemoryDB retains automatic snapshots before deleting them. W
    hen set to `0`, automatic backups are disabled. Defaults to `0`.
    """
    snapshot_retention_limit: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of you
    r shard. Example: `05:00-09:00`.
    """
    snapshot_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) ARN of the SNS topic to which cluster notifications are sent.
    """
    sns_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Forces new resource) The name of the subnet group to be used for the cluster. Defaults to
    a subnet group consisting of default VPC subnets.
    """
    subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    """
    (Optional, Forces new resource) A flag to enable in-transit encryption on the cluster. When set to `
    false`, the `acl_name` must be `open-access`. Defaults to `true`.
    """
    tls_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        acl_name: str | core.StringOut,
        node_type: str | core.StringOut,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_name: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        maintenance_window: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        num_replicas_per_shard: int | core.IntOut | None = None,
        num_shards: int | core.IntOut | None = None,
        parameter_group_name: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        snapshot_name: str | core.StringOut | None = None,
        snapshot_retention_limit: int | core.IntOut | None = None,
        snapshot_window: str | core.StringOut | None = None,
        sns_topic_arn: str | core.StringOut | None = None,
        subnet_group_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tls_enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                acl_name=acl_name,
                node_type=node_type,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                description=description,
                engine_version=engine_version,
                final_snapshot_name=final_snapshot_name,
                kms_key_arn=kms_key_arn,
                maintenance_window=maintenance_window,
                name=name,
                name_prefix=name_prefix,
                num_replicas_per_shard=num_replicas_per_shard,
                num_shards=num_shards,
                parameter_group_name=parameter_group_name,
                port=port,
                security_group_ids=security_group_ids,
                snapshot_arns=snapshot_arns,
                snapshot_name=snapshot_name,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                sns_topic_arn=sns_topic_arn,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                tls_enabled=tls_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acl_name: str | core.StringOut = core.arg()

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_name: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        maintenance_window: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        node_type: str | core.StringOut = core.arg()

        num_replicas_per_shard: int | core.IntOut | None = core.arg(default=None)

        num_shards: int | core.IntOut | None = core.arg(default=None)

        parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        snapshot_name: str | core.StringOut | None = core.arg(default=None)

        snapshot_retention_limit: int | core.IntOut | None = core.arg(default=None)

        snapshot_window: str | core.StringOut | None = core.arg(default=None)

        sns_topic_arn: str | core.StringOut | None = core.arg(default=None)

        subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tls_enabled: bool | core.BoolOut | None = core.arg(default=None)
