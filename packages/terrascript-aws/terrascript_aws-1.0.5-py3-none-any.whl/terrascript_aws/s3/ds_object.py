import terrascript.core as core


@core.data(type="aws_s3_object", namespace="s3")
class DsObject(core.Data):
    """
    Object data (see **limitations above** to understand cases in which this field is actually available
    )
    """

    body: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the bucket to read the object from. Alternatively, an [S3 access point](https
    ://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest
    /dev/bucket-key.html) for SSE-KMS.
    """
    bucket_key_enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Specifies caching behavior along the request/reply chain.
    """
    cache_control: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies presentational information for the object.
    """
    content_disposition: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies what content encodings have been applied to the object and thus what decoding mechanisms m
    ust be applied to obtain the media-type referenced by the Content-Type header field.
    """
    content_encoding: str | core.StringOut = core.attr(str, computed=True)

    """
    The language the content is in.
    """
    content_language: str | core.StringOut = core.attr(str, computed=True)

    """
    Size of the body in bytes.
    """
    content_length: int | core.IntOut = core.attr(int, computed=True)

    """
    A standard MIME type describing the format of the object data.
    """
    content_type: str | core.StringOut = core.attr(str, computed=True)

    """
    [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) generated for the object (an MD5 sum of the object c
    ontent in case it's not encrypted)
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    If the object expiration is configured (see [object lifecycle management](http://docs.aws.amazon.com
    /AmazonS3/latest/dev/object-lifecycle-mgmt.html)), the field includes this header. It includes the e
    xpiry-date and rule-id key value pairs providing object expiration information. The value of the rul
    e-id is URL encoded.
    """
    expiration: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time at which the object is no longer cacheable.
    """
    expires: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The full path to the object inside the bucket
    """
    key: str | core.StringOut = core.attr(str)

    """
    Last modified date of the object in RFC1123 format (e.g., `Mon, 02 Jan 2006 15:04:05 MST`)
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    """
    A map of metadata stored with the object in S3
    """
    metadata: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    Indicates whether this object has an active [legal hold](https://docs.aws.amazon.com/AmazonS3/latest
    /dev/object-lock-overview.html#object-lock-legal-holds). This field is only returned if you have per
    mission to view an object's legal hold status.
    """
    object_lock_legal_hold_status: str | core.StringOut = core.attr(str, computed=True)

    """
    The object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overvie
    w.html#object-lock-retention-modes) currently in place for this object.
    """
    object_lock_mode: str | core.StringOut = core.attr(str, computed=True)

    """
    The date and time when this object's object lock will expire.
    """
    object_lock_retain_until_date: str | core.StringOut = core.attr(str, computed=True)

    range: str | core.StringOut | None = core.attr(str, default=None)

    """
    If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this
    field includes the chosen encryption and algorithm used.
    """
    server_side_encryption: str | core.StringOut = core.attr(str, computed=True)

    """
    If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used
    for the object.
    """
    sse_kms_key_id: str | core.StringOut = core.attr(str, computed=True)

    """
    [Storage class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) information
    of the object. Available for all objects except for `Standard` storage class objects.
    """
    storage_class: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Specific version ID of the object returned (defaults to latest version)
    """
    version_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    If the bucket is configured as a website, redirects requests for this object to another object in th
    e same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadat
    a.
    """
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
