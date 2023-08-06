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


@core.data(type="aws_memorydb_cluster", namespace="memorydb")
class DsCluster(core.Data):
    """
    The name of the Access Control List associated with the cluster.
    """

    acl_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the cluster.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    True when the cluster allows automatic minor version upgrades.
    """
    auto_minor_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    cluster_endpoint: list[ClusterEndpoint] | core.ArrayOut[ClusterEndpoint] = core.attr(
        ClusterEndpoint, computed=True, kind=core.Kind.array
    )

    """
    Description for the cluster.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    Patch version number of the Redis engine used by the cluster.
    """
    engine_patch_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Version number of the Redis engine used by the cluster.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the final cluster snapshot to be created when this resource is deleted. If omitted, no final
    snapshot will be made.
    """
    final_snapshot_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Same as `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the KMS key used to encrypt the cluster at rest.
    """
    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The weekly time range during which maintenance on the cluster is performed. Specify as a range in th
    e format `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC). Example: `sun:23:00-mon:01:30`.
    """
    maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the cluster.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The compute and memory capacity of the nodes in the cluster.
    """
    node_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of replicas to apply to each shard.
    """
    num_replicas_per_shard: int | core.IntOut = core.attr(int, computed=True)

    """
    The number of shards in the cluster.
    """
    num_shards: int | core.IntOut = core.attr(int, computed=True)

    """
    The name of the parameter group associated with the cluster.
    """
    parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Port number that the cluster configuration endpoint is listening on.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    Set of VPC Security Group ID-s associated with this cluster.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Set of shards in this cluster.
    """
    shards: list[Shards] | core.ArrayOut[Shards] = core.attr(
        Shards, computed=True, kind=core.Kind.array
    )

    """
    The number of days for which MemoryDB retains automatic snapshots before deleting them. When set to
    0`, automatic backups are disabled.
    """
    snapshot_retention_limit: int | core.IntOut = core.attr(int, computed=True)

    """
    The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Ex
    ample: `05:00-09:00`.
    """
    snapshot_window: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the SNS topic to which cluster notifications are sent.
    """
    sns_topic_arn: str | core.StringOut = core.attr(str, computed=True)

    subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the cluster.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    When true, in-transit encryption is enabled for the cluster.
    """
    tls_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
