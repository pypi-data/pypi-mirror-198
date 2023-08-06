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


@core.resource(type="aws_memorydb_cluster", namespace="aws_memorydb")
class Cluster(core.Resource):

    acl_name: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    cluster_endpoint: list[ClusterEndpoint] | core.ArrayOut[ClusterEndpoint] = core.attr(
        ClusterEndpoint, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    engine_patch_version: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    final_snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    maintenance_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    node_type: str | core.StringOut = core.attr(str)

    num_replicas_per_shard: int | core.IntOut | None = core.attr(int, default=None)

    num_shards: int | core.IntOut | None = core.attr(int, default=None)

    parameter_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    shards: list[Shards] | core.ArrayOut[Shards] = core.attr(
        Shards, computed=True, kind=core.Kind.array
    )

    snapshot_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_retention_limit: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    snapshot_window: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    sns_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
