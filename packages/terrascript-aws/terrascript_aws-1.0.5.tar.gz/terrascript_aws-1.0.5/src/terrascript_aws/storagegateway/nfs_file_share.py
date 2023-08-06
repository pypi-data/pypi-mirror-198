import terrascript.core as core


@core.schema
class CacheAttributes(core.Schema):

    cache_stale_timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CacheAttributes.Args(
                cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cache_stale_timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)


@core.schema
class NfsFileShareDefaults(core.Schema):

    directory_mode: str | core.StringOut | None = core.attr(str, default=None)

    file_mode: str | core.StringOut | None = core.attr(str, default=None)

    group_id: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        directory_mode: str | core.StringOut | None = None,
        file_mode: str | core.StringOut | None = None,
        group_id: str | core.StringOut | None = None,
        owner_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NfsFileShareDefaults.Args(
                directory_mode=directory_mode,
                file_mode=file_mode,
                group_id=group_id,
                owner_id=owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_mode: str | core.StringOut | None = core.arg(default=None)

        file_mode: str | core.StringOut | None = core.arg(default=None)

        group_id: str | core.StringOut | None = core.arg(default=None)

        owner_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_storagegateway_nfs_file_share", namespace="storagegateway")
class NfsFileShare(core.Resource):
    """
    Amazon Resource Name (ARN) of the NFS File Share.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the storage used for audit logs.
    """
    audit_destination_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The region of the S3 bucket used by the file share. Required when specifying `vpc_endpoin
    t_dns_name`.
    """
    bucket_region: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Refresh cache information. see [Cache Attributes](#cache_attributes) for more details.
    """
    cache_attributes: CacheAttributes | None = core.attr(CacheAttributes, default=None)

    """
    (Required) The list of clients that are allowed to access the file gateway. The list must contain ei
    ther valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1
    item. Maximum 100 items.
    """
    client_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) The default [storage class](https://docs.aws.amazon.com/storagegateway/latest/APIReferenc
    e/API_CreateNFSFileShare.html#StorageGateway-CreateNFSFileShare-request-DefaultStorageClass) for obj
    ects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`.
    """
    default_storage_class: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the file share. Must be set if an S3 prefix name is set in `location_arn`.
    """
    file_share_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    ID of the NFS File Share.
    """
    fileshare_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the file gateway.
    """
    gateway_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Boolean value that enables guessing of the MIME type for uploaded objects based on file e
    xtensions. Defaults to `true`.
    """
    guess_mime_type_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Amazon Resource Name (ARN) of the NFS File Share.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key
    , or `false` to use a key managed by Amazon S3. Defaults to `false`.
    """
    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This va
    lue can only be set when `kms_encrypted` is true.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ARN of the backed storage used for storing file data.
    """
    location_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Nested argument with file share default values. More information below. see [NFS File Sha
    re Defaults](#nfs_file_share_defaults) for more details.
    """
    nfs_file_share_defaults: NfsFileShareDefaults | None = core.attr(
        NfsFileShareDefaults, default=None
    )

    """
    (Optional) The notification policy of the file share. For more information see the [AWS Documentatio
    n](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateNFSFileShare.html#Storag
    eGateway-CreateNFSFileShare-request-NotificationPolicy). Default value is `{}`.
    """
    notification_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Access Control List permission for S3 objects. Defaults to `private`.
    """
    object_acl: str | core.StringOut | None = core.attr(str, default=None)

    """
    File share path used by the NFS client to identify the mount point.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Boolean to indicate write status of file share. File share does not accept writes if `tru
    e`. Defaults to `false`.
    """
    read_only: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Boolean who pays the cost of the request and the data download from the Amazon S3 bucket.
    Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to
    false`.
    """
    requester_pays: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes
    when it accesses the underlying storage.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only
    root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (ev
    eryone is mapped to anonymous user)
    """
    squash: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) The DNS name of the VPC endpoint for S3 PrivateLink.
    """
    vpc_endpoint_dns_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        client_list: list[str] | core.ArrayOut[core.StringOut],
        gateway_arn: str | core.StringOut,
        location_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
        audit_destination_arn: str | core.StringOut | None = None,
        bucket_region: str | core.StringOut | None = None,
        cache_attributes: CacheAttributes | None = None,
        default_storage_class: str | core.StringOut | None = None,
        file_share_name: str | core.StringOut | None = None,
        guess_mime_type_enabled: bool | core.BoolOut | None = None,
        kms_encrypted: bool | core.BoolOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        nfs_file_share_defaults: NfsFileShareDefaults | None = None,
        notification_policy: str | core.StringOut | None = None,
        object_acl: str | core.StringOut | None = None,
        read_only: bool | core.BoolOut | None = None,
        requester_pays: bool | core.BoolOut | None = None,
        squash: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_endpoint_dns_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NfsFileShare.Args(
                client_list=client_list,
                gateway_arn=gateway_arn,
                location_arn=location_arn,
                role_arn=role_arn,
                audit_destination_arn=audit_destination_arn,
                bucket_region=bucket_region,
                cache_attributes=cache_attributes,
                default_storage_class=default_storage_class,
                file_share_name=file_share_name,
                guess_mime_type_enabled=guess_mime_type_enabled,
                kms_encrypted=kms_encrypted,
                kms_key_arn=kms_key_arn,
                nfs_file_share_defaults=nfs_file_share_defaults,
                notification_policy=notification_policy,
                object_acl=object_acl,
                read_only=read_only,
                requester_pays=requester_pays,
                squash=squash,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_dns_name=vpc_endpoint_dns_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audit_destination_arn: str | core.StringOut | None = core.arg(default=None)

        bucket_region: str | core.StringOut | None = core.arg(default=None)

        cache_attributes: CacheAttributes | None = core.arg(default=None)

        client_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        default_storage_class: str | core.StringOut | None = core.arg(default=None)

        file_share_name: str | core.StringOut | None = core.arg(default=None)

        gateway_arn: str | core.StringOut = core.arg()

        guess_mime_type_enabled: bool | core.BoolOut | None = core.arg(default=None)

        kms_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        location_arn: str | core.StringOut = core.arg()

        nfs_file_share_defaults: NfsFileShareDefaults | None = core.arg(default=None)

        notification_policy: str | core.StringOut | None = core.arg(default=None)

        object_acl: str | core.StringOut | None = core.arg(default=None)

        read_only: bool | core.BoolOut | None = core.arg(default=None)

        requester_pays: bool | core.BoolOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        squash: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_dns_name: str | core.StringOut | None = core.arg(default=None)
