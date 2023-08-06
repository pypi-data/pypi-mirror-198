import terrascript.core as core


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


@core.data(type="aws_memorydb_cluster", namespace="aws_memorydb")
class DsCluster(core.Data):

    acl_name: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_minor_version_upgrade: bool | core.BoolOut = core.attr(bool, computed=True)

    cluster_endpoint: list[ClusterEndpoint] | core.ArrayOut[ClusterEndpoint] = core.attr(
        ClusterEndpoint, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    engine_patch_version: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    node_type: str | core.StringOut = core.attr(str, computed=True)

    num_replicas_per_shard: int | core.IntOut = core.attr(int, computed=True)

    num_shards: int | core.IntOut = core.attr(int, computed=True)

    parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    shards: list[Shards] | core.ArrayOut[Shards] = core.attr(
        Shards, computed=True, kind=core.Kind.array
    )

    snapshot_retention_limit: int | core.IntOut = core.attr(int, computed=True)

    snapshot_window: str | core.StringOut = core.attr(str, computed=True)

    sns_topic_arn: str | core.StringOut = core.attr(str, computed=True)

    subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
