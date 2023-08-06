import terrascript.core as core


@core.schema
class ClientData(core.Schema):

    comment: str | core.StringOut | None = core.attr(str, default=None)

    upload_end: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    upload_size: float | core.FloatOut | None = core.attr(float, default=None, computed=True)

    upload_start: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        comment: str | core.StringOut | None = None,
        upload_end: str | core.StringOut | None = None,
        upload_size: float | core.FloatOut | None = None,
        upload_start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ClientData.Args(
                comment=comment,
                upload_end=upload_end,
                upload_size=upload_size,
                upload_start=upload_start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comment: str | core.StringOut | None = core.arg(default=None)

        upload_end: str | core.StringOut | None = core.arg(default=None)

        upload_size: float | core.FloatOut | None = core.arg(default=None)

        upload_start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UserBucket(core.Schema):

    s3_bucket: str | core.StringOut = core.attr(str)

    s3_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_bucket: str | core.StringOut,
        s3_key: str | core.StringOut,
    ):
        super().__init__(
            args=UserBucket.Args(
                s3_bucket=s3_bucket,
                s3_key=s3_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket: str | core.StringOut = core.arg()

        s3_key: str | core.StringOut = core.arg()


@core.schema
class DiskContainer(core.Schema):

    description: str | core.StringOut | None = core.attr(str, default=None)

    format: str | core.StringOut = core.attr(str)

    url: str | core.StringOut | None = core.attr(str, default=None)

    user_bucket: UserBucket | None = core.attr(UserBucket, default=None)

    def __init__(
        self,
        *,
        format: str | core.StringOut,
        description: str | core.StringOut | None = None,
        url: str | core.StringOut | None = None,
        user_bucket: UserBucket | None = None,
    ):
        super().__init__(
            args=DiskContainer.Args(
                format=format,
                description=description,
                url=url,
                user_bucket=user_bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: str | core.StringOut | None = core.arg(default=None)

        format: str | core.StringOut = core.arg()

        url: str | core.StringOut | None = core.arg(default=None)

        user_bucket: UserBucket | None = core.arg(default=None)


@core.resource(type="aws_ebs_snapshot_import", namespace="aws_ebs")
class SnapshotImport(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    client_data: ClientData | None = core.attr(ClientData, default=None)

    data_encryption_key_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    disk_container: DiskContainer = core.attr(DiskContainer)

    encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    outpost_arn: str | core.StringOut = core.attr(str, computed=True)

    owner_alias: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    permanent_restore: bool | core.BoolOut | None = core.attr(bool, default=None)

    role_name: str | core.StringOut | None = core.attr(str, default=None)

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
        disk_container: DiskContainer,
        client_data: ClientData | None = None,
        description: str | core.StringOut | None = None,
        encrypted: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        permanent_restore: bool | core.BoolOut | None = None,
        role_name: str | core.StringOut | None = None,
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
            args=SnapshotImport.Args(
                disk_container=disk_container,
                client_data=client_data,
                description=description,
                encrypted=encrypted,
                kms_key_id=kms_key_id,
                permanent_restore=permanent_restore,
                role_name=role_name,
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
        client_data: ClientData | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disk_container: DiskContainer = core.arg()

        encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        permanent_restore: bool | core.BoolOut | None = core.arg(default=None)

        role_name: str | core.StringOut | None = core.arg(default=None)

        storage_tier: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        temporary_restore_days: int | core.IntOut | None = core.arg(default=None)
