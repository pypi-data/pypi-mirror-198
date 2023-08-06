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


@core.resource(type="aws_storagegateway_nfs_file_share", namespace="aws_storagegateway")
class NfsFileShare(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    audit_destination_arn: str | core.StringOut | None = core.attr(str, default=None)

    bucket_region: str | core.StringOut | None = core.attr(str, default=None)

    cache_attributes: CacheAttributes | None = core.attr(CacheAttributes, default=None)

    client_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    default_storage_class: str | core.StringOut | None = core.attr(str, default=None)

    file_share_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    fileshare_id: str | core.StringOut = core.attr(str, computed=True)

    gateway_arn: str | core.StringOut = core.attr(str)

    guess_mime_type_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_encrypted: bool | core.BoolOut | None = core.attr(bool, default=None)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    location_arn: str | core.StringOut = core.attr(str)

    nfs_file_share_defaults: NfsFileShareDefaults | None = core.attr(
        NfsFileShareDefaults, default=None
    )

    notification_policy: str | core.StringOut | None = core.attr(str, default=None)

    object_acl: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut = core.attr(str, computed=True)

    read_only: bool | core.BoolOut | None = core.attr(bool, default=None)

    requester_pays: bool | core.BoolOut | None = core.attr(bool, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    squash: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
