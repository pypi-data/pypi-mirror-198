import terrascript.core as core


@core.resource(type="aws_s3_object", namespace="s3")
class Object(core.Resource):
    """
    (Optional) [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl
    ) to apply. Valid values are `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authen
    ticated-read`, `bucket-owner-read`, and `bucket-owner-full-control`. Defaults to `private`.
    """

    acl: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the bucket to put the file in. Alternatively, an [S3 access point](https://docs.a
    ws.amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified.
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest
    /dev/bucket-key.html) for SSE-KMS.
    """
    bucket_key_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org
    /Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
    """
    cache_control: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, conflicts with `source` and `content_base64`) Literal string value to use as the object c
    ontent, which will be uploaded as UTF-8-encoded text.
    """
    content: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, conflicts with `source` and `content`) Base64-encoded data that will be decoded and uploa
    ded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is r
    ecommended only for small content such as the result of the `gzipbase64` function with small text st
    rings. For larger objects, use `source` to stream the content from a disk file.
    """
    content_base64: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Presentational information for the object. Read [w3c content_disposition](http://www.w3.o
    rg/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
    """
    content_disposition: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Content encodings that have been applied to the object and thus what decoding mechanisms
    must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c cont
    ent encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further informati
    on.
    """
    content_encoding: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Language the content is in e.g., en-US or en-GB.
    """
    content_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Standard MIME type describing the format of the object data, e.g., application/octet-stre
    am. All Valid MIME Types are valid for this input.
    """
    content_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Triggers updates when the value changes. The only meaningful value is `filemd5("path/to/f
    ile")` (Terraform 0.11.12 or later) or `${md5(file("path/to/file"))}` (Terraform 0.11.11 or earlier)
    . This attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = "a
    ws:kms"`, also if an object is larger than 16 MB, the AWS Management Console will upload or copy tha
    t object as a Multipart Upload, and therefore the ETag will not be an MD5 digest (see `source_hash`
    instead).
    """
    etag: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether to allow the object to be deleted by removing any legal hold on any object versio
    n. Default is `false`. This value should be set to `true` only if the bucket has S3 object lock enab
    led.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    key` of the resource supplied above
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the object once it is in the bucket.
    """
    key: str | core.StringOut = core.attr(str)

    """
    (Optional) ARN of the KMS Key to use for object encryption. If the S3 Bucket has server-side encrypt
    ion enabled, that value will automatically be used. If referencing the `aws_kms_key` resource, use t
    he `arn` attribute. If referencing the `aws_kms_alias` data source or resource, use the `target_key_
    arn` attribute. Terraform will only perform drift detection if a configuration value is provided.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of keys/values to provision metadata (will be automatically prefixed by `x-amz-meta-`
    , note that only lowercase label are currently supported by the AWS Go API).
    """
    metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) [Legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#ob
    ject-lock-legal-holds) status that you want to apply to the specified object. Valid values are `ON`
    and `OFF`.
    """
    object_lock_legal_hold_status: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-
    overview.html#object-lock-retention-modes) that you want to apply to this object. Valid values are `
    GOVERNANCE` and `COMPLIANCE`.
    """
    object_lock_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Date and time, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8), when
    this object's object lock will [expire](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock
    overview.html#object-lock-retention-periods).
    """
    object_lock_retain_until_date: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Server-side encryption of the object in S3. Valid values are "`AES256`" and "`aws:kms`".
    """
    server_side_encryption: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, conflicts with `content` and `content_base64`) Path to a file that will be read and uploa
    ded as raw bytes for the object content.
    """
    source: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Triggers updates like `etag` but useful to address `etag` encryption limitations. Set usi
    ng `filemd5("path/to/source")` (Terraform 0.11.12 or later). (The value is only stored in state and
    not saved by AWS.)
    """
    source_hash: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) [Storage Class](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html#Amazon
    S3-PutObject-request-header-StorageClass) for the object. Defaults to "`STANDARD`".
    """
    storage_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags to assign to the object. If configured with a provider [`default_tags` config
    uration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-config
    uration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Unique version ID value for the object, if bucket versioning is enabled.
    """
    version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-p
    age-redirect.html).
    """
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
