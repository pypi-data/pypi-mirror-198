import terrascript.core as core


@core.data(type="aws_db_snapshot", namespace="rds")
class DsDbSnapshot(core.Data):
    """
    Specifies the allocated storage size in gigabytes (GB).
    """

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    """
    Specifies the name of the Availability Zone the DB instance was located in at the time of the DB sna
    pshot.
    """
    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns the list of snapshots created by the specific db_instance
    """
    db_instance_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) for the DB snapshot.
    """
    db_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Returns information on a specific snapshot_id.
    """
    db_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    Specifies whether the DB snapshot is encrypted.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies the name of the database engine.
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the version of the database engine.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    The snapshot ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set this value to true to include manual DB snapshots that are public and can be
    """
    include_public: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Set this value to true to include shared manual DB snapshots from other
    """
    include_shared: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of t
    he snapshot.
    """
    iops: int | core.IntOut = core.attr(int, computed=True)

    """
    The ARN for the KMS encryption key.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    License model information for the restored DB instance.
    """
    license_model: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Provides the option group name for the DB snapshot.
    """
    option_group_name: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    """
    Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
    """
    snapshot_create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The type of snapshots to be returned. If you don't specify a SnapshotType
    """
    snapshot_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross custome
    r or cross region copy.
    """
    source_db_snapshot_identifier: str | core.StringOut = core.attr(str, computed=True)

    """
    The region that the DB snapshot was created in or copied from.
    """
    source_region: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the status of this DB snapshot.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the storage type associated with DB snapshot.
    """
    storage_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the ID of the VPC associated with the DB snapshot.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        db_instance_identifier: str | core.StringOut | None = None,
        db_snapshot_identifier: str | core.StringOut | None = None,
        include_public: bool | core.BoolOut | None = None,
        include_shared: bool | core.BoolOut | None = None,
        most_recent: bool | core.BoolOut | None = None,
        snapshot_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbSnapshot.Args(
                db_instance_identifier=db_instance_identifier,
                db_snapshot_identifier=db_snapshot_identifier,
                include_public=include_public,
                include_shared=include_shared,
                most_recent=most_recent,
                snapshot_type=snapshot_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_instance_identifier: str | core.StringOut | None = core.arg(default=None)

        db_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        include_public: bool | core.BoolOut | None = core.arg(default=None)

        include_shared: bool | core.BoolOut | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_type: str | core.StringOut | None = core.arg(default=None)
