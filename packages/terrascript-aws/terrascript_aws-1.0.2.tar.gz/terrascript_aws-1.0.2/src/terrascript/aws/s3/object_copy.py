import terrascript.core as core


@core.schema
class Grant(core.Schema):

    email: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None)

    permissions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    type: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut],
        type: str | core.StringOut,
        email: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
        uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Grant.Args(
                permissions=permissions,
                type=type,
                email=email,
                id=id,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        permissions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        type: str | core.StringOut = core.arg()

        uri: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_s3_object_copy", namespace="aws_s3")
class ObjectCopy(core.Resource):

    acl: str | core.StringOut | None = core.attr(str, default=None)

    bucket: str | core.StringOut = core.attr(str)

    bucket_key_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    cache_control: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    content_disposition: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    content_encoding: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    content_language: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    content_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    copy_if_match: str | core.StringOut | None = core.attr(str, default=None)

    copy_if_modified_since: str | core.StringOut | None = core.attr(str, default=None)

    copy_if_none_match: str | core.StringOut | None = core.attr(str, default=None)

    copy_if_unmodified_since: str | core.StringOut | None = core.attr(str, default=None)

    customer_algorithm: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    customer_key: str | core.StringOut | None = core.attr(str, default=None)

    customer_key_md5: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    etag: str | core.StringOut = core.attr(str, computed=True)

    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    expected_source_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    expiration: str | core.StringOut = core.attr(str, computed=True)

    expires: str | core.StringOut | None = core.attr(str, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    grant: list[Grant] | core.ArrayOut[Grant] | None = core.attr(
        Grant, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str)

    kms_encryption_context: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    last_modified: str | core.StringOut = core.attr(str, computed=True)

    metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    metadata_directive: str | core.StringOut | None = core.attr(str, default=None)

    object_lock_legal_hold_status: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    object_lock_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    object_lock_retain_until_date: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    request_charged: bool | core.BoolOut = core.attr(bool, computed=True)

    request_payer: str | core.StringOut | None = core.attr(str, default=None)

    server_side_encryption: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    source: str | core.StringOut = core.attr(str)

    source_customer_algorithm: str | core.StringOut | None = core.attr(str, default=None)

    source_customer_key: str | core.StringOut | None = core.attr(str, default=None)

    source_customer_key_md5: str | core.StringOut | None = core.attr(str, default=None)

    source_version_id: str | core.StringOut = core.attr(str, computed=True)

    storage_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tagging_directive: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: str | core.StringOut = core.attr(str, computed=True)

    website_redirect: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
        source: str | core.StringOut,
        acl: str | core.StringOut | None = None,
        bucket_key_enabled: bool | core.BoolOut | None = None,
        cache_control: str | core.StringOut | None = None,
        content_disposition: str | core.StringOut | None = None,
        content_encoding: str | core.StringOut | None = None,
        content_language: str | core.StringOut | None = None,
        content_type: str | core.StringOut | None = None,
        copy_if_match: str | core.StringOut | None = None,
        copy_if_modified_since: str | core.StringOut | None = None,
        copy_if_none_match: str | core.StringOut | None = None,
        copy_if_unmodified_since: str | core.StringOut | None = None,
        customer_algorithm: str | core.StringOut | None = None,
        customer_key: str | core.StringOut | None = None,
        customer_key_md5: str | core.StringOut | None = None,
        expected_bucket_owner: str | core.StringOut | None = None,
        expected_source_bucket_owner: str | core.StringOut | None = None,
        expires: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        grant: list[Grant] | core.ArrayOut[Grant] | None = None,
        kms_encryption_context: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        metadata: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        metadata_directive: str | core.StringOut | None = None,
        object_lock_legal_hold_status: str | core.StringOut | None = None,
        object_lock_mode: str | core.StringOut | None = None,
        object_lock_retain_until_date: str | core.StringOut | None = None,
        request_payer: str | core.StringOut | None = None,
        server_side_encryption: str | core.StringOut | None = None,
        source_customer_algorithm: str | core.StringOut | None = None,
        source_customer_key: str | core.StringOut | None = None,
        source_customer_key_md5: str | core.StringOut | None = None,
        storage_class: str | core.StringOut | None = None,
        tagging_directive: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        website_redirect: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ObjectCopy.Args(
                bucket=bucket,
                key=key,
                source=source,
                acl=acl,
                bucket_key_enabled=bucket_key_enabled,
                cache_control=cache_control,
                content_disposition=content_disposition,
                content_encoding=content_encoding,
                content_language=content_language,
                content_type=content_type,
                copy_if_match=copy_if_match,
                copy_if_modified_since=copy_if_modified_since,
                copy_if_none_match=copy_if_none_match,
                copy_if_unmodified_since=copy_if_unmodified_since,
                customer_algorithm=customer_algorithm,
                customer_key=customer_key,
                customer_key_md5=customer_key_md5,
                expected_bucket_owner=expected_bucket_owner,
                expected_source_bucket_owner=expected_source_bucket_owner,
                expires=expires,
                force_destroy=force_destroy,
                grant=grant,
                kms_encryption_context=kms_encryption_context,
                kms_key_id=kms_key_id,
                metadata=metadata,
                metadata_directive=metadata_directive,
                object_lock_legal_hold_status=object_lock_legal_hold_status,
                object_lock_mode=object_lock_mode,
                object_lock_retain_until_date=object_lock_retain_until_date,
                request_payer=request_payer,
                server_side_encryption=server_side_encryption,
                source_customer_algorithm=source_customer_algorithm,
                source_customer_key=source_customer_key,
                source_customer_key_md5=source_customer_key_md5,
                storage_class=storage_class,
                tagging_directive=tagging_directive,
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

        content_disposition: str | core.StringOut | None = core.arg(default=None)

        content_encoding: str | core.StringOut | None = core.arg(default=None)

        content_language: str | core.StringOut | None = core.arg(default=None)

        content_type: str | core.StringOut | None = core.arg(default=None)

        copy_if_match: str | core.StringOut | None = core.arg(default=None)

        copy_if_modified_since: str | core.StringOut | None = core.arg(default=None)

        copy_if_none_match: str | core.StringOut | None = core.arg(default=None)

        copy_if_unmodified_since: str | core.StringOut | None = core.arg(default=None)

        customer_algorithm: str | core.StringOut | None = core.arg(default=None)

        customer_key: str | core.StringOut | None = core.arg(default=None)

        customer_key_md5: str | core.StringOut | None = core.arg(default=None)

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        expected_source_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        expires: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        grant: list[Grant] | core.ArrayOut[Grant] | None = core.arg(default=None)

        key: str | core.StringOut = core.arg()

        kms_encryption_context: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        metadata_directive: str | core.StringOut | None = core.arg(default=None)

        object_lock_legal_hold_status: str | core.StringOut | None = core.arg(default=None)

        object_lock_mode: str | core.StringOut | None = core.arg(default=None)

        object_lock_retain_until_date: str | core.StringOut | None = core.arg(default=None)

        request_payer: str | core.StringOut | None = core.arg(default=None)

        server_side_encryption: str | core.StringOut | None = core.arg(default=None)

        source: str | core.StringOut = core.arg()

        source_customer_algorithm: str | core.StringOut | None = core.arg(default=None)

        source_customer_key: str | core.StringOut | None = core.arg(default=None)

        source_customer_key_md5: str | core.StringOut | None = core.arg(default=None)

        storage_class: str | core.StringOut | None = core.arg(default=None)

        tagging_directive: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        website_redirect: str | core.StringOut | None = core.arg(default=None)
