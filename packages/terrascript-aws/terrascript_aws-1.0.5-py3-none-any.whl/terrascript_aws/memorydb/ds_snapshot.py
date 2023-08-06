import terrascript.core as core


@core.schema
class ClusterConfiguration(core.Schema):

    description: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    maintenance_window: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    node_type: str | core.StringOut = core.attr(str, computed=True)

    num_shards: int | core.IntOut = core.attr(int, computed=True)

    parameter_group_name: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_retention_limit: int | core.IntOut = core.attr(int, computed=True)

    snapshot_window: str | core.StringOut = core.attr(str, computed=True)

    subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    topic_arn: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        description: str | core.StringOut,
        engine_version: str | core.StringOut,
        maintenance_window: str | core.StringOut,
        name: str | core.StringOut,
        node_type: str | core.StringOut,
        num_shards: int | core.IntOut,
        parameter_group_name: str | core.StringOut,
        port: int | core.IntOut,
        snapshot_retention_limit: int | core.IntOut,
        snapshot_window: str | core.StringOut,
        subnet_group_name: str | core.StringOut,
        topic_arn: str | core.StringOut,
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=ClusterConfiguration.Args(
                description=description,
                engine_version=engine_version,
                maintenance_window=maintenance_window,
                name=name,
                node_type=node_type,
                num_shards=num_shards,
                parameter_group_name=parameter_group_name,
                port=port,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                subnet_group_name=subnet_group_name,
                topic_arn=topic_arn,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut = core.arg()

        engine_version: str | core.StringOut = core.arg()

        maintenance_window: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        node_type: str | core.StringOut = core.arg()

        num_shards: int | core.IntOut = core.arg()

        parameter_group_name: str | core.StringOut = core.arg()

        port: int | core.IntOut = core.arg()

        snapshot_retention_limit: int | core.IntOut = core.arg()

        snapshot_window: str | core.StringOut = core.arg()

        subnet_group_name: str | core.StringOut = core.arg()

        topic_arn: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.data(type="aws_memorydb_snapshot", namespace="memorydb")
class DsSnapshot(core.Data):
    """
    The ARN of the snapshot.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The configuration of the cluster from which the snapshot was taken.
    """
    cluster_configuration: list[ClusterConfiguration] | core.ArrayOut[
        ClusterConfiguration
    ] = core.attr(ClusterConfiguration, computed=True, kind=core.Kind.array)

    """
    Name of the MemoryDB cluster that this snapshot was taken from.
    """
    cluster_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the snapshot.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN of the KMS key used to encrypt the snapshot at rest.
    """
    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the snapshot.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Indicates whether the snapshot is from an automatic backup (`automated`) or was created manually (`m
    anual`).
    """
    source: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of tags assigned to the snapshot.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSnapshot.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
