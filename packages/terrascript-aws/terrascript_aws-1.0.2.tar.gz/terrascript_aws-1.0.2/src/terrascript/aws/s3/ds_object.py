import terrascript.core as core


@core.data(type="aws_s3_object", namespace="aws_s3")
class DsObject(core.Data):

    body: str | core.StringOut = core.attr(str, computed=True)

    bucket: str | core.StringOut = core.attr(str)

    bucket_key_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    cache_control: str | core.StringOut = core.attr(str, computed=True)

    content_disposition: str | core.StringOut = core.attr(str, computed=True)

    content_encoding: str | core.StringOut = core.attr(str, computed=True)

    content_language: str | core.StringOut = core.attr(str, computed=True)

    content_length: int | core.IntOut = core.attr(int, computed=True)

    content_type: str | core.StringOut = core.attr(str, computed=True)

    etag: str | core.StringOut = core.attr(str, computed=True)

    expiration: str | core.StringOut = core.attr(str, computed=True)

    expires: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    metadata: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    object_lock_legal_hold_status: str | core.StringOut = core.attr(str, computed=True)

    object_lock_mode: str | core.StringOut = core.attr(str, computed=True)

    object_lock_retain_until_date: str | core.StringOut = core.attr(str, computed=True)

    range: str | core.StringOut | None = core.attr(str, default=None)

    server_side_encryption: str | core.StringOut = core.attr(str, computed=True)

    sse_kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    storage_class: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    website_redirect_location: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
        range: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsObject.Args(
                bucket=bucket,
                key=key,
                range=range,
                tags=tags,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        range: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        version_id: str | core.StringOut | None = core.arg(default=None)
