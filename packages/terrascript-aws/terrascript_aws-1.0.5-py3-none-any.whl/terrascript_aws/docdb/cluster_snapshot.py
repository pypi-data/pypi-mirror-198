import terrascript.core as core


@core.resource(type="aws_docdb_cluster_snapshot", namespace="docdb")
class ClusterSnapshot(core.Resource):
    """
    List of EC2 Availability Zones that instances in the DocDB cluster snapshot can be restored in.
    """

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) The DocDB Cluster Identifier from which to take the snapshot.
    """
    db_cluster_identifier: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the DocDB Cluster Snapshot.
    """
    db_cluster_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Identifier for the snapshot.
    """
    db_cluster_snapshot_identifier: str | core.StringOut = core.attr(str)

    """
    Specifies the name of the database engine.
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    Version of the database engine for this DocDB cluster snapshot.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    If storage_encrypted is true, the AWS KMS key identifier for the encrypted DocDB cluster snapshot.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Port that the DocDB cluster was listening on at the time of the snapshot.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_type: str | core.StringOut = core.attr(str, computed=True)

    source_db_cluster_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The status of this DocDB Cluster Snapshot.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies whether the DocDB cluster snapshot is encrypted.
    """
    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The VPC ID associated with the DocDB cluster snapshot.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_cluster_identifier: str | core.StringOut,
        db_cluster_snapshot_identifier: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterSnapshot.Args(
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_snapshot_identifier=db_cluster_snapshot_identifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_cluster_identifier: str | core.StringOut = core.arg()

        db_cluster_snapshot_identifier: str | core.StringOut = core.arg()
