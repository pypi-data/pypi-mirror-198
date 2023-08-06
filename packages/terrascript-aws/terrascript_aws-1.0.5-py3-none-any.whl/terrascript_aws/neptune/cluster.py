import terrascript.core as core


@core.resource(type="aws_neptune_cluster", namespace="neptune")
class Cluster(core.Resource):
    """
    (Optional) Specifies whether upgrades between different major versions are allowed. You must set it
    to `true` when providing an `engine_version` parameter that uses a different major version than the
    DB cluster's current version. Default is `false`.
    """

    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Specifies whether any cluster modifications are applied immediately, or during the next m
    aintenance window. Default is `false`.
    """
    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The Neptune Cluster Amazon Resource Name (ARN)
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of EC2 Availability Zones that instances in the Neptune cluster can be created in.
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

    cluster_members: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The Neptune Cluster Resource ID
    """
    cluster_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If set to true, tags are copied to any snapshot of the DB cluster that is created.
    """
    copy_tags_to_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A value that indicates whether the DB cluster has deletion protection enabled.The databas
    e can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
    """
    deletion_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A list of the log types this DB cluster is configured to export to Cloudwatch Logs. Curre
    ntly only supports `audit`.
    """
    enable_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The DNS address of the Neptune instance
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the database engine to be used for this Neptune cluster. Defaults to `neptune
    .
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The database engine version.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The name of your final Neptune snapshot when this Neptune cluster is deleted. If omitted,
    no final snapshot will be made.
    """
    final_snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Route53 Hosted Zone ID of the endpoint
    """
    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether or not mappings of AWS Identity and Access Management (IAM) accounts to
    database accounts is enabled.
    """
    iam_database_authentication_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A List of ARNs for the IAM roles to associate to the Neptune Cluster.
    """
    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The Neptune Cluster Identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN for the KMS encryption key. When specifying `kms_key_arn`, `storage_encrypted` ne
    eds to be set to true.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A cluster parameter group to associate with the cluster.
    """
    neptune_cluster_parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A Neptune subnet group to associate with this Neptune instance.
    """
    neptune_subnet_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The port on which the Neptune accepts connections. Default is `8182`.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The daily time range during which automated backups are created if automated backups are
    enabled using the BackupRetentionPeriod parameter. Time in UTC. Default: A 30-minute window selected
    at random from an 8-hour block of time per regionE.g., 04:00-09:00
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
    A read-only endpoint for the Neptune cluster, automatically load-balanced across replicas
    """
    reader_endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN of a source Neptune cluster or Neptune instance if this Neptune cluster is to be crea
    ted as a Read Replica.
    """
    replication_source_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Determines whether a final Neptune snapshot is created before the Neptune cluster is dele
    ted. If true is specified, no Neptune snapshot is created. If false is specified, a Neptune snapshot
    is created before the Neptune cluster is deleted, using the value from `final_snapshot_identifier`.
    Default is `false`.
    """
    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies whether or not to create this cluster from a snapshot. You can use either the n
    ame or ARN when specifying a Neptune cluster snapshot, or the ARN when specifying a Neptune snapshot
    .
    """
    snapshot_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies whether the Neptune cluster is encrypted. The default is `false` if not specifi
    ed.
    """
    storage_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of tags to assign to the Neptune cluster. If configured with a provider [`default_t
    ags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_
    tags-configuration-block) present, tags with matching keys will overwrite those defined at the provi
    der-level.
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
    (Optional) List of VPC security groups to associate with the Cluster
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allow_major_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = None,
        backup_retention_period: int | core.IntOut | None = None,
        cluster_identifier: str | core.StringOut | None = None,
        cluster_identifier_prefix: str | core.StringOut | None = None,
        copy_tags_to_snapshot: bool | core.BoolOut | None = None,
        deletion_protection: bool | core.BoolOut | None = None,
        enable_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        final_snapshot_identifier: str | core.StringOut | None = None,
        iam_database_authentication_enabled: bool | core.BoolOut | None = None,
        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        neptune_cluster_parameter_group_name: str | core.StringOut | None = None,
        neptune_subnet_group_name: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        replication_source_identifier: str | core.StringOut | None = None,
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
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                availability_zones=availability_zones,
                backup_retention_period=backup_retention_period,
                cluster_identifier=cluster_identifier,
                cluster_identifier_prefix=cluster_identifier_prefix,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                deletion_protection=deletion_protection,
                enable_cloudwatch_logs_exports=enable_cloudwatch_logs_exports,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                iam_roles=iam_roles,
                kms_key_arn=kms_key_arn,
                neptune_cluster_parameter_group_name=neptune_cluster_parameter_group_name,
                neptune_subnet_group_name=neptune_subnet_group_name,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                replication_source_identifier=replication_source_identifier,
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
        allow_major_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        availability_zones: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        backup_retention_period: int | core.IntOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        copy_tags_to_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        deletion_protection: bool | core.BoolOut | None = core.arg(default=None)

        enable_cloudwatch_logs_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        final_snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        iam_database_authentication_enabled: bool | core.BoolOut | None = core.arg(default=None)

        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        neptune_cluster_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        neptune_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        replication_source_identifier: str | core.StringOut | None = core.arg(default=None)

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        snapshot_identifier: str | core.StringOut | None = core.arg(default=None)

        storage_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
