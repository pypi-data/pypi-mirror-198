import terrascript.core as core


@core.resource(type="aws_s3_object", namespace="aws_s3")
class Object(core.Resource):

    acl: str | core.StringOut | None = core.attr(str, default=None)

    bucket: str | core.StringOut = core.attr(str)

    bucket_key_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    cache_control: str | core.StringOut | None = core.attr(str, default=None)

    content: str | core.StringOut | None = core.attr(str, default=None)

    content_base64: str | core.StringOut | None = core.attr(str, default=None)

    content_disposition: str | core.StringOut | None = core.attr(str, default=None)

    content_encoding: str | core.StringOut | None = core.attr(str, default=None)

    content_language: str | core.StringOut | None = core.attr(str, default=None)

    content_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    etag: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    object_lock_legal_hold_status: str | core.StringOut | None = core.attr(str, default=None)

    object_lock_mode: str | core.StringOut | None = core.attr(str, default=None)

    object_lock_retain_until_date: str | core.StringOut | None = core.attr(str, default=None)

    server_side_encryption: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    source: str | core.StringOut | None = core.attr(str, default=None)

    source_hash: str | core.StringOut | None = core.attr(str, default=None)

    storage_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: str | core.StringOut = core.attr(str, computed=True)

    website_redirect: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
        acl: str | core.StringOut | None = None,
        bucket_key_enabled: bool | core.BoolOut | None = None,
        cache_control: str | core.StringOut | None = None,
        content: str | core.StringOut | None = None,
        content_base64: str | core.StringOut | None = None,
        content_disposition: str | core.StringOut | None = None,
        content_encoding: str | core.StringOut | None = None,
        content_language: str | core.StringOut | None = None,
        content_type: str | core.StringOut | None = None,
        etag: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        metadata: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        object_lock_legal_hold_status: str | core.StringOut | None = None,
        object_lock_mode: str | core.StringOut | None = None,
        object_lock_retain_until_date: str | core.StringOut | None = None,
        server_side_encryption: str | core.StringOut | None = None,
        source: str | core.StringOut | None = None,
        source_hash: str | core.StringOut | None = None,
        storage_class: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        website_redirect: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Object.Args(
                bucket=bucket,
                key=key,
                acl=acl,
                bucket_key_enabled=bucket_key_enabled,
                cache_control=cache_control,
                content=content,
                content_base64=content_base64,
                content_disposition=content_disposition,
                content_encoding=content_encoding,
                content_language=content_language,
                content_type=content_type,
                etag=etag,
                force_destroy=force_destroy,
                kms_key_id=kms_key_id,
                metadata=metadata,
                object_lock_legal_hold_status=object_lock_legal_hold_status,
                object_lock_mode=object_lock_mode,
                object_lock_retain_until_date=object_lock_retain_until_date,
                server_side_encryption=server_side_encryption,
                source=source,
                source_hash=source_hash,
                storage_class=storage_class,
                tags=tags,
                tags_all=tags_all,
                website_redirect=website_redirect,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acl: str | core.StringOut | None = core.arg(default=None)

        bucket: str | core.StringOut = core.arg()

        bucket_key_enabled: bool | core.BoolOut | None = core.arg(default=None)

        cache_control: str | core.StringOut | None = core.arg(default=None)

        content: str | core.StringOut | None = core.arg(default=None)

        content_base64: str | core.StringOut | None = core.arg(default=None)

        content_disposition: str | core.StringOut | None = core.arg(default=None)

        content_encoding: str | core.StringOut | None = core.arg(default=None)

        content_language: str | core.StringOut | None = core.arg(default=None)

        content_type: str | core.StringOut | None = core.arg(default=None)

        etag: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        object_lock_legal_hold_status: str | core.StringOut | None = core.arg(default=None)

        object_lock_mode: str | core.StringOut | None = core.arg(default=None)

        object_lock_retain_until_date: str | core.StringOut | None = core.arg(default=None)

        server_side_encryption: str | core.StringOut | None = core.arg(default=None)

        source: str | core.StringOut | None = core.arg(default=None)

        source_hash: str | core.StringOut | None = core.arg(default=None)

        storage_class: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        website_redirect: str | core.StringOut | None = core.arg(default=None)
