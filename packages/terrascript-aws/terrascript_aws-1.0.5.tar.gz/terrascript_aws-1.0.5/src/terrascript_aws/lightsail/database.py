import terrascript.core as core


@core.resource(type="aws_lightsail_database", namespace="lightsail")
class Database(core.Resource):
    """
    When true , applies changes immediately. When false , applies changes during the preferred maintenan
    ce window. Some changes may cause an outage.
    """

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The ARN of the Lightsail instance (matches `id`).
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Availability Zone in which to create your new database. Use the us-east-2a case-sensi
    tive format.
    """
    availability_zone: str | core.StringOut = core.attr(str)

    """
    When true, enables automated backup retention for your database. When false, disables automated back
    up retention for your database. Disabling backup retention deletes all automated database backups. B
    efore disabling this, you may want to create a snapshot of your database.
    """
    backup_retention_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The blueprint ID for your new database. A blueprint describes the major engine version of
    a database. You can get a list of database blueprints IDs by using the AWS CLI command: `aws lights
    ail get-relational-database-blueprints`
    """
    blueprint_id: str | core.StringOut = core.attr(str)

    """
    (Required)  The bundle ID for your new database. A bundle describes the performance specifications f
    or your database (see list below). You can get a list of database bundle IDs by using the AWS CLI co
    mmand: `aws lightsail get-relational-database-bundles`.
    """
    bundle_id: str | core.StringOut = core.attr(str)

    """
    The certificate associated with the database.
    """
    ca_certificate_identifier: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of vCPUs for the database.
    """
    cpu_count: int | core.IntOut = core.attr(int, computed=True)

    """
    The timestamp when the instance was created.
    """
    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    The size of the disk for the database.
    """
    disk_size: float | core.FloatOut = core.attr(float, computed=True)

    """
    The database software (for example, MySQL).
    """
    engine: str | core.StringOut = core.attr(str, computed=True)

    """
    The database engine version (for example, 5.7.23).
    """
    engine_version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required unless `skip_final_snapshot = true`) The name of the database snapshot created if skip fin
    al snapshot is false, which is the default value for that parameter.
    """
    final_snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the Lightsail instance (matches `arn`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the master database created when the Lightsail database resource is created.
    """
    master_database_name: str | core.StringOut = core.attr(str)

    """
    The master endpoint fqdn for the database.
    """
    master_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The master endpoint network port for the database.
    """
    master_endpoint_port: int | core.IntOut = core.attr(int, computed=True)

    """
    (Sensitive) The password for the master user of your new database. The password can include any prin
    table ASCII character except "/", , or "@".
    """
    master_password: str | core.StringOut = core.attr(str)

    """
    The master user name for your new database.
    """
    master_username: str | core.StringOut = core.attr(str)

    """
    The daily time range during which automated backups are created for your new database if automated b
    ackups are enabled. Must be in the hh24:mi-hh24:mi format. Example: `16:00-16:30`. Specified in Coor
    dinated Universal Time (UTC).
    """
    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The weekly time range during which system maintenance can occur on your new database. Must be in the
    ddd:hh24:mi-ddd:hh24:mi format. Specified in Coordinated Universal Time (UTC). Example: `Tue:17:00-
    Tue:17:30`
    """
    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Specifies the accessibility options for your new database. A value of true specifies a database that
    is available to resources outside of your Lightsail account. A value of false specifies a database
    that is available only to your Lightsail resources in the same region as your database.
    """
    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The amount of RAM in GB for the database.
    """
    ram_size: float | core.FloatOut = core.attr(float, computed=True)

    relational_database_name: str | core.StringOut = core.attr(str)

    """
    Describes the secondary Availability Zone of a high availability database. The secondary database is
    used for failover support of a high availability database.
    """
    secondary_availability_zone: str | core.StringOut = core.attr(str, computed=True)

    """
    Determines whether a final database snapshot is created before your database is deleted. If true is
    specified, no database snapshot is created. If false is specified, a database snapshot is created be
    fore your database is deleted. You must specify the final relational database snapshot name paramete
    r if the skip final snapshot parameter is false.
    """
    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The support code for the database. Include this code in your email to support when you have question
    s about a database in Lightsail. This code enables our support team to look up your Lightsail inform
    ation more easily.
    """
    support_code: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. To create a key-only tag, use an empty string as
    the value.
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

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: str | core.StringOut,
        blueprint_id: str | core.StringOut,
        bundle_id: str | core.StringOut,
        master_database_name: str | core.StringOut,
        master_password: str | core.StringOut,
        master_username: str | core.StringOut,
        relational_database_name: str | core.StringOut,
        apply_immediately: bool | core.BoolOut | None = None,
        backup_retention_enabled: bool | core.BoolOut | None = None,
        final_snapshot_name: str | core.StringOut | None = None,
        preferred_backup_window: str | core.StringOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        skip_final_snapshot: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Database.Args(
                availability_zone=availability_zone,
                blueprint_id=blueprint_id,
                bundle_id=bundle_id,
                master_database_name=master_database_name,
                master_password=master_password,
                master_username=master_username,
                relational_database_name=relational_database_name,
                apply_immediately=apply_immediately,
                backup_retention_enabled=backup_retention_enabled,
                final_snapshot_name=final_snapshot_name,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                skip_final_snapshot=skip_final_snapshot,
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

        availability_zone: str | core.StringOut = core.arg()

        backup_retention_enabled: bool | core.BoolOut | None = core.arg(default=None)

        blueprint_id: str | core.StringOut = core.arg()

        bundle_id: str | core.StringOut = core.arg()

        final_snapshot_name: str | core.StringOut | None = core.arg(default=None)

        master_database_name: str | core.StringOut = core.arg()

        master_password: str | core.StringOut = core.arg()

        master_username: str | core.StringOut = core.arg()

        preferred_backup_window: str | core.StringOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        relational_database_name: str | core.StringOut = core.arg()

        skip_final_snapshot: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
