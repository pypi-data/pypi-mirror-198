import terrascript.core as core


@core.resource(type="aws_docdb_cluster_instance", namespace="docdb")
class ClusterInstance(core.Resource):
    """
    (Optional) Specifies whether any database modifications
    """

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of cluster instance
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates that minor engine upgrades will be applied automatically to the DB instance dur
    ing the maintenance window. Default `true`.
    """
    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Computed) The EC2 Availability Zone that the DB instance is created in. See [docs](https:
    //docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html) about the details.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The identifier of the CA certificate for the DB instance.
    """
    ca_cert_identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The identifier of the [`aws_docdb_cluster`](/docs/providers/aws/r/docdb_cluster.html) in
    which to launch this instance.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    The DB subnet group to associate with this DB instance.
    """
    db_subnet_group_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The region-unique, immutable identifier for the DB instance.
    """
    dbi_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The DNS address for this instance. May not be writable
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the database engine to be used for the DocDB instance. Defaults to `docdb`. V
    alid Values: `docdb`.
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    The database engine version
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The identifier for the DocDB instance, if omitted, Terraform will as
    sign a random, unique identifier.
    """
    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique identifier beginning with the specified prefix. Con
    flicts with `identifier`.
    """
    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The instance class to use. For details on CPU and memory, see [Scaling for DocDB Instance
    s][2]. DocDB currently
    """
    instance_class: str | core.StringOut = core.attr(str)

    """
    The ARN for the KMS encryption key if one is set to the cluster.
    """
    kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The database port
    """
    port: int | core.IntOut = core.attr(int, computed=True)

    """
    The daily time range during which automated backups are created if automated backups are enabled.
    """
    preferred_backup_window: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The window to perform maintenance in.
    """
    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Default 0. Failover Priority setting on instance level. The reader who has lower tier has
    higher priority to get promoter to writer.
    """
    promotion_tier: int | core.IntOut | None = core.attr(int, default=None)

    publicly_accessible: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies whether the DB cluster is encrypted.
    """
    storage_encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) A map of tags to assign to the instance. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    writer: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        instance_class: str | core.StringOut,
        apply_immediately: bool | core.BoolOut | None = None,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        ca_cert_identifier: str | core.StringOut | None = None,
        engine: str | core.StringOut | None = None,
        identifier: str | core.StringOut | None = None,
        identifier_prefix: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        promotion_tier: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterInstance.Args(
                cluster_identifier=cluster_identifier,
                instance_class=instance_class,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                ca_cert_identifier=ca_cert_identifier,
                engine=engine,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                preferred_maintenance_window=preferred_maintenance_window,
                promotion_tier=promotion_tier,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        ca_cert_identifier: str | core.StringOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut = core.arg()

        engine: str | core.StringOut | None = core.arg(default=None)

        identifier: str | core.StringOut | None = core.arg(default=None)

        identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut = core.arg()

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        promotion_tier: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
