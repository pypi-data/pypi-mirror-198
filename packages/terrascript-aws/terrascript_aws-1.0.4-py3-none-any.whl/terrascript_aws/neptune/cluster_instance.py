import terrascript.core as core


@core.resource(type="aws_neptune_cluster_instance", namespace="neptune")
class ClusterInstance(core.Resource):
    """
    The hostname of the instance. See also `endpoint` and `port`.
    """

    address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether any instance modifications
    """
    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of neptune instance
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates that minor engine upgrades will be applied automatically to the instance during
    the maintenance window. Default is `true`.
    """
    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The EC2 Availability Zone that the neptune instance is created in.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The identifier of the [`aws_neptune_cluster`](/docs/providers/aws/r/neptune_cluster.html)
    in which to launch this instance.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    The region-unique, immutable identifier for the neptune instance.
    """
    dbi_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The connection endpoint in `address:port` format.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the database engine to be used for the neptune instance. Defaults to `neptune
    . Valid Values: `neptune`.
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The neptune engine version.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The Instance identifier
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The identifier for the neptune instance, if omitted, Terraform will
    assign a random, unique identifier.
    """
    identifier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique identifier beginning with the specified prefix. Con
    flicts with `identifier`.
    """
    identifier_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The instance class to use.
    """
    instance_class: str | core.StringOut = core.attr(str)

    """
    The ARN for the KMS encryption key if one is set to the neptune cluster.
    """
    kms_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the neptune parameter group to associate with this instance.
    """
    neptune_parameter_group_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required if `publicly_accessible = false`, Optional otherwise) A subnet group to associate with thi
    s neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_
    neptune_cluster`](/docs/providers/aws/r/neptune_cluster.html).
    """
    neptune_subnet_group_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The port on which the DB accepts connections. Defaults to `8182`.
    """
    port: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The daily time range during which automated backups are created if automated backups are
    enabled. Eg: "04:00-09:00"
    """
    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

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

    """
    (Optional) Bool to control if instance is publicly accessible. Default is `false`.
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Specifies whether the neptune cluster is encrypted.
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
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        identifier: str | core.StringOut | None = None,
        identifier_prefix: str | core.StringOut | None = None,
        neptune_parameter_group_name: str | core.StringOut | None = None,
        neptune_subnet_group_name: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        promotion_tier: int | core.IntOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
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
                engine=engine,
                engine_version=engine_version,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                neptune_parameter_group_name=neptune_parameter_group_name,
                neptune_subnet_group_name=neptune_subnet_group_name,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                promotion_tier=promotion_tier,
                publicly_accessible=publicly_accessible,
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

        cluster_identifier: str | core.StringOut = core.arg()

        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        identifier: str | core.StringOut | None = core.arg(default=None)

        identifier_prefix: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut = core.arg()

        neptune_parameter_group_name: str | core.StringOut | None = core.arg(default=None)

        neptune_subnet_group_name: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        promotion_tier: int | core.IntOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
