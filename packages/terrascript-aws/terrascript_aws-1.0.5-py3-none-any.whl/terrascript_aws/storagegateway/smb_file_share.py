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


@core.resource(type="aws_storagegateway_smb_file_share", namespace="storagegateway")
class SmbFileShare(core.Resource):
    """
    (Optional) The files and folders on this share will only be visible to users with read access. Defau
    lt value is `false`.
    """

    access_based_enumeration: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A list of users in the Active Directory that have admin access to the file share. Only va
    lid if `authentication` is set to `ActiveDirectory`.
    """
    admin_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Amazon Resource Name (ARN) of the SMB File Share.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the CloudWatch Log Group used for the audit logs.
    """
    audit_destination_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The authentication method that users use to access the file share. Defaults to `ActiveDir
    ectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
    """
    authentication: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The region of the S3 buck used by the file share. Required when specifying a `vpc_endpoin
    t_dns_name`.
    """
    bucket_region: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Refresh cache information. see [Cache Attributes](#cache_attributes) for more details.
    """
    cache_attributes: CacheAttributes | None = core.attr(CacheAttributes, default=None)

    """
    (Optional) The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client dete
    rmines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The d
    efault value is `ClientSpecified`.
    """
    case_sensitivity: str | core.StringOut | None = core.attr(str, default=None)

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
    ID of the SMB File Share.
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
    Amazon Resource Name (ARN) of the SMB File Share.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of users in the Active Directory that are not allowed to access the file share. On
    ly valid if `authentication` is set to `ActiveDirectory`.
    """
    invalid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
    (Optional) Boolean to indicate Opportunistic lock (oplock) status. Defaults to `true`.
    """
    oplocks_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

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
    (Optional) Set this value to `true` to enable ACL (access control list) on the SMB fileshare. Set it
    to `false` to map file and directory permissions to the POSIX permissions. This setting applies onl
    y to `ActiveDirectory` authentication type.
    """
    smb_acl_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

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
    (Optional) A list of users in the Active Directory that are allowed to access the file share. If you
    need to specify an Active directory group, add '@' before the name of the group. It will be set on
    Allowed group in AWS console. Only valid if `authentication` is set to `ActiveDirectory`.
    """
    valid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The DNS name of the VPC endpoint for S3 private link.
    """
    vpc_endpoint_dns_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: str | core.StringOut,
        location_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
        access_based_enumeration: bool | core.BoolOut | None = None,
        admin_user_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        audit_destination_arn: str | core.StringOut | None = None,
        authentication: str | core.StringOut | None = None,
        bucket_region: str | core.StringOut | None = None,
        cache_attributes: CacheAttributes | None = None,
        case_sensitivity: str | core.StringOut | None = None,
        default_storage_class: str | core.StringOut | None = None,
        file_share_name: str | core.StringOut | None = None,
        guess_mime_type_enabled: bool | core.BoolOut | None = None,
        invalid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        kms_encrypted: bool | core.BoolOut | None = None,
        kms_key_arn: str | core.StringOut | None = None,
        notification_policy: str | core.StringOut | None = None,
        object_acl: str | core.StringOut | None = None,
        oplocks_enabled: bool | core.BoolOut | None = None,
        read_only: bool | core.BoolOut | None = None,
        requester_pays: bool | core.BoolOut | None = None,
        smb_acl_enabled: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        valid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpc_endpoint_dns_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SmbFileShare.Args(
                gateway_arn=gateway_arn,
                location_arn=location_arn,
                role_arn=role_arn,
                access_based_enumeration=access_based_enumeration,
                admin_user_list=admin_user_list,
                audit_destination_arn=audit_destination_arn,
                authentication=authentication,
                bucket_region=bucket_region,
                cache_attributes=cache_attributes,
                case_sensitivity=case_sensitivity,
                default_storage_class=default_storage_class,
                file_share_name=file_share_name,
                guess_mime_type_enabled=guess_mime_type_enabled,
                invalid_user_list=invalid_user_list,
                kms_encrypted=kms_encrypted,
                kms_key_arn=kms_key_arn,
                notification_policy=notification_policy,
                object_acl=object_acl,
                oplocks_enabled=oplocks_enabled,
                read_only=read_only,
                requester_pays=requester_pays,
                smb_acl_enabled=smb_acl_enabled,
                tags=tags,
                tags_all=tags_all,
                valid_user_list=valid_user_list,
                vpc_endpoint_dns_name=vpc_endpoint_dns_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_based_enumeration: bool | core.BoolOut | None = core.arg(default=None)

        admin_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        audit_destination_arn: str | core.StringOut | None = core.arg(default=None)

        authentication: str | core.StringOut | None = core.arg(default=None)

        bucket_region: str | core.StringOut | None = core.arg(default=None)

        cache_attributes: CacheAttributes | None = core.arg(default=None)

        case_sensitivity: str | core.StringOut | None = core.arg(default=None)

        default_storage_class: str | core.StringOut | None = core.arg(default=None)

        file_share_name: str | core.StringOut | None = core.arg(default=None)

        gateway_arn: str | core.StringOut = core.arg()

        guess_mime_type_enabled: bool | core.BoolOut | None = core.arg(default=None)

        invalid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        kms_encrypted: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        location_arn: str | core.StringOut = core.arg()

        notification_policy: str | core.StringOut | None = core.arg(default=None)

        object_acl: str | core.StringOut | None = core.arg(default=None)

        oplocks_enabled: bool | core.BoolOut | None = core.arg(default=None)

        read_only: bool | core.BoolOut | None = core.arg(default=None)

        requester_pays: bool | core.BoolOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        smb_acl_enabled: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        valid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_dns_name: str | core.StringOut | None = core.arg(default=None)
