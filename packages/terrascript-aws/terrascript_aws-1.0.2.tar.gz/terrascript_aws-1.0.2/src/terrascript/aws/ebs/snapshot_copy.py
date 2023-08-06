import terrascript.core as core


@core.resource(type="aws_ebs_snapshot_copy", namespace="aws_ebs")
class SnapshotCopy(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    data_encryption_key_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_alias: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    permanent_restore: bool | core.BoolOut | None = core.attr(bool, default=None)

    source_region: str | core.StringOut = core.attr(str)

    source_snapshot_id: str | core.StringOut = core.attr(str)

    storage_tier: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    temporary_restore_days: int | core.IntOut | None = core.attr(int, default=None)

    volume_id: str | core.StringOut = core.attr(str, computed=True)

    volume_size: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        source_region: str | core.StringOut,
        source_snapshot_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        permanent_restore: bool | core.BoolOut | None = None,
        storage_tier: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        temporary_restore_days: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotCopy.Args(
                source_region=source_region,
                source_snapshot_id=source_snapshot_id,
                description=description,
                encrypted=encrypted,
                kms_key_id=kms_key_id,
                permanent_restore=permanent_restore,
                storage_tier=storage_tier,
                tags=tags,
                tags_all=tags_all,
                temporary_restore_days=temporary_restore_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        permanent_restore: bool | core.BoolOut | None = core.arg(default=None)

        source_region: str | core.StringOut = core.arg()

        source_snapshot_id: str | core.StringOut = core.arg()

        storage_tier: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        temporary_restore_days: int | core.IntOut | None = core.arg(default=None)
