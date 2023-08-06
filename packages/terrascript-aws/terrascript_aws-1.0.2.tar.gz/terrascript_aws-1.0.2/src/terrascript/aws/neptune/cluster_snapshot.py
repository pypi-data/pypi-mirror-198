import terrascript.core as core


@core.resource(type="aws_neptune_cluster_snapshot", namespace="aws_neptune")
class ClusterSnapshot(core.Resource):

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_cluster_identifier: str | core.StringOut = core.attr(str)

    db_cluster_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    db_cluster_snapshot_identifier: str | core.StringOut = core.attr(str)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    license_model: str | core.StringOut = core.attr(str, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    snapshot_type: str | core.StringOut = core.attr(str, computed=True)

    source_db_cluster_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

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
