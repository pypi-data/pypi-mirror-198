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


@core.resource(type="aws_s3_object_copy", namespace="s3")
class ObjectCopy(core.Resource):
    """
    (Optional) [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl
    ) to apply. Defaults to `private`. Valid values are `private`, `public-read`, `public-read-write`, `
    authenticated-read`, `aws-exec-read`, `bucket-owner-read`, and `bucket-owner-full-control`. Conflict
    s with `grant`.
    """

    acl: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the bucket to put the file in.
    """
    bucket: str | core.StringOut = core.attr(str)

    bucket_key_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://
    www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.
    """
    cache_control: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies presentational information for the object. Read [w3c content_disposition](http:
    //www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.
    """
    content_disposition: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies what content encodings have been applied to the object and thus what decoding m
    echanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read
    [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further
    information.
    """
    content_encoding: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Language the content is in e.g., en-US or en-GB.
    """
    content_language: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Standard MIME type describing the format of the object data, e.g., `application/octet-str
    eam`. All Valid MIME Types are valid for this input.
    """
    content_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Copies the object if its entity tag (ETag) matches the specified tag.
    """
    copy_if_match: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Copies the object if it has been modified since the specified time, in [RFC3339 format](h
    ttps://tools.ietf.org/html/rfc3339#section-5.8).
    """
    copy_if_modified_since: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Copies the object if its entity tag (ETag) is different than the specified ETag.
    """
    copy_if_none_match: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Copies the object if it hasn't been modified since the specified time, in [RFC3339 format
    ](https://tools.ietf.org/html/rfc3339#section-5.8).
    """
    copy_if_unmodified_since: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the algorithm to use to when encrypting the object (for example, AES256).
    """
    customer_algorithm: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. T
    his value is used to store the object and then it is discarded; Amazon S3 does not store the encrypt
    ion key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side-e
    ncryption-customer-algorithm header.
    """
    customer_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 u
    ses this header for a message integrity check to ensure that the encryption key was transmitted with
    out error.
    """
    customer_key_md5: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The ETag generated for the object (an MD5 sum of the object content). For plaintext objects or objec
    ts encrypted with an AWS-managed key, the hash is an MD5 digest of the object data. For objects encr
    ypted with a KMS key or objects created by either the Multipart Upload or Part Copy operation, the h
    ash is not an MD5 digest, regardless of the method of encryption. More information on possible value
    s can be found on [Common Response Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTComm
    onResponseHeaders.html).
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Account id of the expected destination bucket owner. If the destination bucket is owned b
    y a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Account id of the expected source bucket owner. If the source bucket is owned by a differ
    ent account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    expected_source_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    If the object expiration is configured, this attribute will be set.
    """
    expiration: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Date and time at which the object is no longer cacheable, in [RFC3339 format](https://too
    ls.ietf.org/html/rfc3339#section-5.8).
    """
    expires: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Allow the object to be deleted by removing any legal hold on any object version. Default
    is `false`. This value should be set to `true` only if the bucket has S3 object lock enabled.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configuration block for header grants. Documented below. Conflicts with `acl`.
    """
    grant: list[Grant] | core.ArrayOut[Grant] | None = core.attr(
        Grant, default=None, kind=core.Kind.array
    )

    """
    (Optional) The canonical user ID of the grantee. Used only when `type` is `CanonicalUser`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the object once it is in the bucket.
    """
    key: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the AWS KMS Encryption Context to use for object encryption. The value is a bas
    e64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.
    """
    kms_encryption_context: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Specifies the AWS KMS Key ARN to use for object encryption. This value is a fully qualifi
    ed **ARN** of the KMS Key. If using `aws_kms_key`, use the exported `arn` attribute: `kms_key_id = a
    ws_kms_key.foo.arn`
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Returns the date that the object was last modified, in [RFC3339 format](https://tools.ietf.org/html/
    rfc3339#section-5.8).
    """
    last_modified: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of keys/values to provision metadata (will be automatically prefixed by `x-amz-meta
    , note that only lowercase label are currently supported by the AWS Go API).
    """
    metadata: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Specifies whether the metadata is copied from the source object or replaced with metadata
    provided in the request. Valid values are `COPY` and `REPLACE`.
    """
    metadata_directive: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The [legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.htm
    l#object-lock-legal-holds) status that you want to apply to the specified object. Valid values are `
    ON` and `OFF`.
    """
    object_lock_legal_hold_status: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) The object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-l
    ock-overview.html#object-lock-retention-modes) that you want to apply to this object. Valid values a
    re `GOVERNANCE` and `COMPLIANCE`.
    """
    object_lock_mode: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The date and time, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8),
    when this object's object lock will [expire](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-
    lock-overview.html#object-lock-retention-periods).
    """
    object_lock_retain_until_date: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    If present, indicates that the requester was successfully charged for the request.
    """
    request_charged: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Confirms that the requester knows that they will be charged for the request. Bucket owner
    s need not specify this parameter in their requests. For information about downloading objects from
    requester pays buckets, see Downloading Objects in Requestor Pays Buckets (https://docs.aws.amazon.c
    om/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the Amazon S3 Developer Guide. If incl
    uded, the only valid value is `requester`.
    """
    request_payer: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies server-side encryption of the object in S3. Valid values are `AES256` and `aws:
    kms`.
    """
    server_side_encryption: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) Specifies the source object for the copy operation. You specify the value in one of two f
    ormats. For objects not accessed through an access point, specify the name of the source bucket and
    the key of the source object, separated by a slash (`/`). For example, `testbucket/test1.json`. For
    objects accessed through access points, specify the Amazon Resource Name (ARN) of the object as acce
    ssed through the access point, in the format `arn:aws:s3:<Region>:<account-id>:accesspoint/<access-p
    oint-name>/object/<key>`. For example, `arn:aws:s3:us-west-2:9999912999:accesspoint/my-access-point/
    object/testbucket/test1.json`.
    """
    source: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies the algorithm to use when decrypting the source object (for example, AES256).
    """
    source_customer_algorithm: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source
    object. The encryption key provided in this header must be one that was used when the source object
    was created.
    """
    source_customer_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 u
    ses this header for a message integrity check to ensure that the encryption key was transmitted with
    out error.
    """
    source_customer_key_md5: str | core.StringOut | None = core.attr(str, default=None)

    """
    Version of the copied object in the source bucket.
    """
    source_version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the desired [storage class](https://docs.aws.amazon.com/AmazonS3/latest/API/API
    _CopyObject.html#AmazonS3-CopyObject-request-header-StorageClass) for the object. Defaults to `STAND
    ARD`.
    """
    storage_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether the object tag-set are copied from the source object or replaced with t
    ag-set provided in the request. Valid values are `COPY` and `REPLACE`.
    """
    tagging_directive: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the object. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Version ID of the newly created copy.
    """
    version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/
    dev/how-to-page-redirect.html).
    """
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
