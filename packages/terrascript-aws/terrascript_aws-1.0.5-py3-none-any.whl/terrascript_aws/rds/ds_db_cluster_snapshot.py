import terrascript.core as core


@core.data(type="aws_db_cluster_snapshot", namespace="rds")
class DsDbClusterSnapshot(core.Data):
    """
    Specifies the allocated storage size in gigabytes (GB).
    """

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    """
    List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Returns the list of snapshots created by the specific db_cluster
    """
    db_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
    """
    db_cluster_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific snapshot_id.
    """
    db_cluster_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    Specifies the name of the database engine.
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    Version of the database engine for this DB cluster snapshot.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The snapshot ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set this value to true to include manual DB Cluster Snapshots that are public and can be
    """
    include_public: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Set this value to true to include shared manual DB Cluster Snapshots from other
    """
    include_shared: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    License model information for the restored DB cluster.
    """
    license_model: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most recent Snapshot.
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Port that the DB cluster was listening on at the time of the snapshot.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    Time when the snapshot was taken, in Universal Coordinated Time (UTC).
    """
    snapshot_create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The type of snapshots to be returned. If you don't specify a SnapshotType
    """
    snapshot_type: str | core.StringOut | None = core.attr(str, default=None)

    source_db_cluster_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of this DB Cluster Snapshot.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether the DB cluster snapshot is encrypted.
    """
    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    A map of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The VPC ID associated with the DB cluster snapshot.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        db_cluster_identifier: str | core.StringOut | None = None,
        db_cluster_snapshot_identifier: str | core.StringOut | None = None,
        include_public: bool | core.BoolOut | None = None,
        include_shared: bool | core.BoolOut | None = None,
        most_recent: bool | core.BoolOut | None = None,
        snapshot_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbClusterSnapshot.Args(
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_snapshot_identifier=db_cluster_snapshot_identifier,
                include_public=include_public,
                include_shared=include_shared,
                most_recent=most_recent,
                snapshot_type=snapshot_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        db_cluster_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        include_public: bool | core.BoolOut | None = core.arg(default=None)

        include_shared: bool | core.BoolOut | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
