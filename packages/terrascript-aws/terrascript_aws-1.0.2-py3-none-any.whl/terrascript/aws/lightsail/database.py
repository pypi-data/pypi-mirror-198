import terrascript.core as core


@core.resource(type="aws_lightsail_database", namespace="aws_lightsail")
class Database(core.Resource):

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str)

    backup_retention_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    blueprint_id: str | core.StringOut = core.attr(str)

    bundle_id: str | core.StringOut = core.attr(str)

    ca_certificate_identifier: str | core.StringOut = core.attr(str, computed=True)

    cpu_count: int | core.IntOut = core.attr(int, computed=True)

    created_at: str | core.StringOut = core.attr(str, computed=True)

    disk_size: float | core.FloatOut = core.attr(float, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    final_snapshot_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    master_database_name: str | core.StringOut = core.attr(str)

    master_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    master_endpoint_port: int | core.IntOut = core.attr(int, computed=True)

    master_password: str | core.StringOut = core.attr(str)

    master_username: str | core.StringOut = core.attr(str)

    preferred_backup_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    ram_size: float | core.FloatOut = core.attr(float, computed=True)

    relational_database_name: str | core.StringOut = core.attr(str)

    secondary_availability_zone: str | core.StringOut = core.attr(str, computed=True)

    skip_final_snapshot: bool | core.BoolOut | None = core.attr(bool, default=None)

    support_code: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
