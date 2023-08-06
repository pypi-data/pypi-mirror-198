import terrascript.core as core


@core.resource(type="aws_db_cluster_snapshot", namespace="rds")
class DbClusterSnapshot(core.Resource):
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
    (Required) The DB Cluster Identifier from which to take the snapshot.
    """
    db_cluster_identifier: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
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
    Version of the database engine for this DB cluster snapshot.
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    License model information for the restored DB cluster.
    """
    license_model: str | core.StringOut = core.attr(str, computed=True)

    """
    Port that the DB cluster was listening on at the time of the snapshot.
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_type: str | core.StringOut = core.attr(str, computed=True)

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
    (Optional) A map of tags to assign to the DB cluster. If configured with a provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block) present, tags with matching keys will overwrite those defined at the provider-l
    evel.
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
    The VPC ID associated with the DB cluster snapshot.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_cluster_identifier: str | core.StringOut,
        db_cluster_snapshot_identifier: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbClusterSnapshot.Args(
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_snapshot_identifier=db_cluster_snapshot_identifier,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_cluster_identifier: str | core.StringOut = core.arg()

        db_cluster_snapshot_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
