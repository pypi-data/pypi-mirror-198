import terrascript.core as core


@core.schema
class GlobalClusterMembers(core.Schema):

    db_cluster_arn: str | core.StringOut = core.attr(str, computed=True)

    is_writer: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        db_cluster_arn: str | core.StringOut,
        is_writer: bool | core.BoolOut,
    ):
        super().__init__(
            args=GlobalClusterMembers.Args(
                db_cluster_arn=db_cluster_arn,
                is_writer=is_writer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_cluster_arn: str | core.StringOut = core.arg()

        is_writer: bool | core.BoolOut = core.arg()


@core.resource(type="aws_docdb_global_cluster", namespace="aws_docdb")
class GlobalCluster(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    database_name: str | core.StringOut | None = core.attr(str, default=None)

    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    engine: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    global_cluster_identifier: str | core.StringOut = core.attr(str)

    global_cluster_members: list[GlobalClusterMembers] | core.ArrayOut[
        GlobalClusterMembers
    ] = core.attr(GlobalClusterMembers, computed=True, kind=core.Kind.array)

    global_cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    source_db_cluster_identifier: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        global_cluster_identifier: str | core.StringOut,
        database_name: str | core.StringOut | None = None,
        deletion_protection: bool | core.BoolOut | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        source_db_cluster_identifier: str | core.StringOut | None = None,
        storage_encrypted: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalCluster.Args(
                global_cluster_identifier=global_cluster_identifier,
                database_name=database_name,
                deletion_protection=deletion_protection,
                engine=engine,
                engine_version=engine_version,
                source_db_cluster_identifier=source_db_cluster_identifier,
                storage_encrypted=storage_encrypted,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database_name: str | core.StringOut | None = core.arg(default=None)

        deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        global_cluster_identifier: str | core.StringOut = core.arg()

        source_db_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)
