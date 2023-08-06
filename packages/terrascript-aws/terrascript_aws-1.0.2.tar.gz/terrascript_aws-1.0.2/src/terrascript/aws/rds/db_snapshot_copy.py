import terrascript.core as core


@core.resource(type="aws_db_snapshot_copy", namespace="aws_rds")
class DbSnapshotCopy(core.Resource):

    allocated_storage: int | core.IntOut = core.attr(int, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    copy_tags: bool | core.BoolOut | None = core.attr(bool, default=None)

    db_snapshot_arn: str | core.StringOut = core.attr(str, computed=True)

    destination_region: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    engine: str | core.StringOut = core.attr(str, computed=True)

    engine_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    iops: int | core.IntOut = core.attr(int, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    license_model: str | core.StringOut = core.attr(str, computed=True)

    option_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    port: int | core.IntOut = core.attr(int, computed=True)

    presigned_url: str | core.StringOut | None = core.attr(str, default=None)

    snapshot_type: str | core.StringOut = core.attr(str, computed=True)

    source_db_snapshot_identifier: str | core.StringOut = core.attr(str)

    source_region: str | core.StringOut = core.attr(str, computed=True)

    storage_type: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_custom_availability_zone: str | core.StringOut | None = core.attr(str, default=None)

    target_db_snapshot_identifier: str | core.StringOut = core.attr(str)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        source_db_snapshot_identifier: str | core.StringOut,
        target_db_snapshot_identifier: str | core.StringOut,
        copy_tags: bool | core.BoolOut | None = None,
        destination_region: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        option_group_name: str | core.StringOut | None = None,
        presigned_url: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_custom_availability_zone: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSnapshotCopy.Args(
                source_db_snapshot_identifier=source_db_snapshot_identifier,
                target_db_snapshot_identifier=target_db_snapshot_identifier,
                copy_tags=copy_tags,
                destination_region=destination_region,
                kms_key_id=kms_key_id,
                option_group_name=option_group_name,
                presigned_url=presigned_url,
                tags=tags,
                tags_all=tags_all,
                target_custom_availability_zone=target_custom_availability_zone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        copy_tags: bool | core.BoolOut | None = core.arg(default=None)

        destination_region: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        option_group_name: str | core.StringOut | None = core.arg(default=None)

        presigned_url: str | core.StringOut | None = core.arg(default=None)

        source_db_snapshot_identifier: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_custom_availability_zone: str | core.StringOut | None = core.arg(default=None)

        target_db_snapshot_identifier: str | core.StringOut = core.arg()
