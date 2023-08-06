import terrascript.core as core


@core.resource(type="aws_dms_replication_instance", namespace="aws_dms")
class ReplicationInstance(core.Resource):

    allocated_storage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    allow_major_version_upgrade: bool | core.BoolOut | None = core.attr(bool, default=None)

    apply_immediately: bool | core.BoolOut | None = core.attr(bool, default=None)

    auto_minor_version_upgrade: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    multi_az: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    preferred_maintenance_window: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    replication_instance_arn: str | core.StringOut = core.attr(str, computed=True)

    replication_instance_class: str | core.StringOut = core.attr(str)

    replication_instance_id: str | core.StringOut = core.attr(str)

    replication_instance_private_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    replication_instance_public_ips: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    replication_subnet_group_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        replication_instance_class: str | core.StringOut,
        replication_instance_id: str | core.StringOut,
        allocated_storage: int | core.IntOut | None = None,
        allow_major_version_upgrade: bool | core.BoolOut | None = None,
        apply_immediately: bool | core.BoolOut | None = None,
        auto_minor_version_upgrade: bool | core.BoolOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        multi_az: bool | core.BoolOut | None = None,
        preferred_maintenance_window: str | core.StringOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        replication_subnet_group_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationInstance.Args(
                replication_instance_class=replication_instance_class,
                replication_instance_id=replication_instance_id,
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                engine_version=engine_version,
                kms_key_arn=kms_key_arn,
                multi_az=multi_az,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                replication_subnet_group_id=replication_subnet_group_id,
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
        allocated_storage: int | core.IntOut | None = core.arg(default=None)

        allow_major_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        apply_immediately: bool | core.BoolOut | None = core.arg(default=None)

        auto_minor_version_upgrade: bool | core.BoolOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        multi_az: bool | core.BoolOut | None = core.arg(default=None)

        preferred_maintenance_window: str | core.StringOut | None = core.arg(default=None)

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        replication_instance_class: str | core.StringOut = core.arg()

        replication_instance_id: str | core.StringOut = core.arg()

        replication_subnet_group_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )
