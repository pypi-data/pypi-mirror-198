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


@core.resource(type="aws_rds_global_cluster", namespace="rds")
class GlobalCluster(core.Resource):
    """
    RDS Global Cluster Amazon Resource Name (ARN)
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resources) Name for an automatically created database on cluster creation.
    """
    database_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If the Global Cluster should have deletion protection enabled. The database can't be dele
    ted when this value is set to `true`. The default is `false`.
    """
    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Forces new resources) Name of the database engine to be used for this DB cluster. Terrafo
    rm will only perform drift detection if a configuration value is provided. Valid values: `aurora`, `
    aurora-mysql`, `aurora-postgresql`. Defaults to `aurora`. Conflicts with `source_db_cluster_identifi
    er`.
    """
    engine: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Engine version of the Aurora global database. The `engine`, `engine_version`, and `instan
    ce_class` (on the `aws_rds_cluster_instance`) must together support global databases. See [Using Ama
    zon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-glo
    bal-database.html) for more information. By upgrading the engine version, Terraform will upgrade clu
    ster members. **NOTE:** To avoid an `inconsistent final plan` error while upgrading, use the `lifecy
    cle` `ignore_changes` for `engine_version` meta argument on the associated `aws_rds_cluster` resourc
    e as shown above in [Upgrading Engine Versions](#upgrading-engine-versions) example.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Enable to remove DB Cluster members from Global Cluster on destroy. Required with `source
    _db_cluster_identifier`.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required, Forces new resources) Global cluster identifier.
    """
    global_cluster_identifier: str | core.StringOut = core.attr(str)

    """
    Set of objects containing Global Cluster members.
    """
    global_cluster_members: list[GlobalClusterMembers] | core.ArrayOut[
        GlobalClusterMembers
    ] = core.attr(GlobalClusterMembers, computed=True, kind=core.Kind.array)

    """
    AWS Region-unique, immutable identifier for the global database cluster. This identifier is found in
    AWS CloudTrail log entries whenever the AWS KMS key for the DB cluster is accessed
    """
    global_cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    RDS Global Cluster identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) to use as the primary DB Cluster of the Global Cluster on crea
    tion. Terraform cannot perform drift detection of this value.
    """
    source_db_cluster_identifier: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Forces new resources) Specifies whether the DB cluster is encrypted. The default is `fals
    e` unless `source_db_cluster_identifier` is specified and encrypted. Terraform will only perform dri
    ft detection if a configuration value is provided.
    """
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
        force_destroy: bool | core.BoolOut | None = None,
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
                force_destroy=force_destroy,
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

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        global_cluster_identifier: str | core.StringOut = core.arg()

        source_db_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)
