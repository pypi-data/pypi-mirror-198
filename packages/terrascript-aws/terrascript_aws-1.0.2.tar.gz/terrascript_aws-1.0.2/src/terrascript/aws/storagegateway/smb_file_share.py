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


@core.resource(type="aws_storagegateway_smb_file_share", namespace="aws_storagegateway")
class SmbFileShare(core.Resource):

    access_based_enumeration: bool | core.BoolOut | None = core.attr(bool, default=None)

    admin_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    audit_destination_arn: str | core.StringOut | None = core.attr(str, default=None)

    authentication: str | core.StringOut | None = core.attr(str, default=None)

    bucket_region: str | core.StringOut | None = core.attr(str, default=None)

    cache_attributes: CacheAttributes | None = core.attr(CacheAttributes, default=None)

    case_sensitivity: str | core.StringOut | None = core.attr(str, default=None)

    default_storage_class: str | core.StringOut | None = core.attr(str, default=None)

    file_share_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    fileshare_id: str | core.StringOut = core.attr(str, computed=True)

    gateway_arn: str | core.StringOut = core.attr(str)

    guess_mime_type_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    invalid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    location_arn: str | core.StringOut = core.attr(str)

    notification_policy: str | core.StringOut | None = core.attr(str, default=None)

    object_acl: str | core.StringOut | None = core.attr(str, default=None)

    oplocks_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    path: str | core.StringOut = core.attr(str, computed=True)

    read_only: bool | core.BoolOut | None = core.attr(bool, default=None)

    requester_pays: bool | core.BoolOut | None = core.attr(bool, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    smb_acl_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    valid_user_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
