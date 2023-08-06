import terrascript.core as core


@core.resource(type="aws_docdb_cluster", namespace="docdb")
class Cluster(core.Resource):
    """
    (Optional) Specifies whether any cluster modifications
    """

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of cluster
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of EC2 Availability Zones that
    """
    availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The days to retain backups for. Default `1`
    """
    backup_retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Forces new resources) The cluster identifier. If omitted, Terraform will assign a random,
    unique identifier.
    """
    cluster_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique cluster identifier beginning with the specified pre
    fix. Conflicts with `cluster_identifier`.
    """
    cluster_identifier_prefix: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The DocDB Cluster Resource ID
    """
    cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A cluster parameter group to associate with the cluster.
    """
    db_cluster_parameter_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) A DB subnet group to associate with this DB instance.
    """
    db_subnet_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A value that indicates whether the DB cluster has deletion protection enabled. The databa
    se can't be deleted when deletion protection is enabled. By default, deletion protection is disabled
    .
    """
    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) List of log types to export to cloudwatch. If omitted, no logs will be exported.
    """
    enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The DNS address of the DocDB instance
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the database engine to be used for this DB cluster. Defaults to `docdb`. Vali
    d Values: `docdb`
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The database engine version. Updating this argument results in an outage.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The name of your final DB snapshot
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The global cluster identifier specified on [`aws_docdb_global_cluster`](/docs/providers/a
    ws/r/docdb_global_cluster.html).
    """
    global_cluster_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Route53 Hosted Zone ID of the endpoint
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The DocDB Cluster Identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` nee
    ds to be set to true.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required unless a `snapshot_identifier` or unless a `global_cluster_identifier` is provided when th
    e cluster is the "secondary" cluster of a global database) Password for the master DB user. Note tha
    t this may
    """
    master_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required unless a `snapshot_identifier` or unless a `global_cluster_identifier` is provided when th
    e cluster is the "secondary" cluster of a global database) Username for the master DB user.
    """
    master_username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The port on which the DB accepts connections
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The daily time range during which automated backups are created if automated backups are
    enabled using the BackupRetentionPeriod parameter.Time in UTC
    """
    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The weekly time range during which system maintenance can occur, in (UTC) e.g., wed:04:00
    wed:04:30
    """
    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    A read-only endpoint for the DocDB cluster, automatically load-balanced across replicas
    """
    reader_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Determines whether a final DB snapshot is created before the DB cluster is deleted. If tr
    ue is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before t
    he DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
    """
    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether or not to create this cluster from a snapshot. You can use either the n
    ame or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
    """
    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether the DB cluster is encrypted. The default is `false`.
    """
    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

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
    (Optional) List of VPC security groups to associate
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        apply_immediately: bool | core.BoolOut | None = None,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        backup_retention_period: int | core.IntOut | None = None,
        cluster_identifier: str | core.StringOut | None = None,
        cluster_identifier_prefix: str | core.StringOut | None = None,
        cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = None,
        db_cluster_parameter_group_name: str | core.StringOut | None = None,
        db_subnet_group_name: str | core.StringOut | None = None,
        deletion_protection: bool | core.BoolOut | None = None,
        enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        global_cluster_identifier: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        master_password: str | core.StringOut | None = None,
        master_username: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        skip_final_snapshot: bool | core.BoolOut | None = None,
        snapshot_identifier: str | core.StringOut | None = None,
        storage_encrypted: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                apply_immediately=apply_immediately,
                availability_zones=availability_zones,
                backup_retention_period=backup_retention_period,
                cluster_identifier=cluster_identifier,
                cluster_identifier_prefix=cluster_identifier_prefix,
                cluster_members=cluster_members,
                db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                db_subnet_group_name=db_subnet_group_name,
                deletion_protection=deletion_protection,
                enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                global_cluster_identifier=global_cluster_identifier,
                kms_key_id=kms_key_id,
                master_password=master_password,
                master_username=master_username,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                storage_encrypted=storage_encrypted,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        backup_retention_period: int | core.IntOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        cluster_members: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        db_cluster_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        db_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        enabled_cloudwatch_logs_exports: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        global_cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        master_password: str | core.StringOut | None = core.arg(default=None)

        master_username: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
