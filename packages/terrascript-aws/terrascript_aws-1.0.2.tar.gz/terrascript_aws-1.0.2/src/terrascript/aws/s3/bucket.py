import terrascript.core as core


@core.schema
class Logging(core.Schema):

    target_bucket: str | core.StringOut = core.attr(str)

    target_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        target_bucket: str | core.StringOut,
        target_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Logging.Args(
                target_bucket=target_bucket,
                target_prefix=target_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_bucket: str | core.StringOut = core.arg()

        target_prefix: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Grant(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None)

    permissions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    type: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        permissions: list[str] | core.ArrayOut[core.StringOut],
        type: str | core.StringOut,
        id: str | core.StringOut | None = None,
        uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Grant.Args(
                permissions=permissions,
                type=type,
                id=id,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        permissions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        type: str | core.StringOut = core.arg()

        uri: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ApplyServerSideEncryptionByDefault(core.Schema):

    kms_master_key_id: str | core.StringOut | None = core.attr(str, default=None)

    sse_algorithm: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        sse_algorithm: str | core.StringOut,
        kms_master_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ApplyServerSideEncryptionByDefault.Args(
                sse_algorithm=sse_algorithm,
                kms_master_key_id=kms_master_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_master_key_id: str | core.StringOut | None = core.arg(default=None)

        sse_algorithm: str | core.StringOut = core.arg()


@core.schema
class ServerSideEncryptionConfigurationRule(core.Schema):

    apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault = core.attr(
        ApplyServerSideEncryptionByDefault
    )

    bucket_key_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault,
        bucket_key_enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ServerSideEncryptionConfigurationRule.Args(
                apply_server_side_encryption_by_default=apply_server_side_encryption_by_default,
                bucket_key_enabled=bucket_key_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault = core.arg()

        bucket_key_enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class ServerSideEncryptionConfiguration(core.Schema):

    rule: ServerSideEncryptionConfigurationRule = core.attr(ServerSideEncryptionConfigurationRule)

    def __init__(
        self,
        *,
        rule: ServerSideEncryptionConfigurationRule,
    ):
        super().__init__(
            args=ServerSideEncryptionConfiguration.Args(
                rule=rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule: ServerSideEncryptionConfigurationRule = core.arg()


@core.schema
class NoncurrentVersionTransition(core.Schema):

    days: int | core.IntOut | None = core.attr(int, default=None)

    storage_class: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: str | core.StringOut,
        days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NoncurrentVersionTransition.Args(
                storage_class=storage_class,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: int | core.IntOut | None = core.arg(default=None)

        storage_class: str | core.StringOut = core.arg()


@core.schema
class NoncurrentVersionExpiration(core.Schema):

    days: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=NoncurrentVersionExpiration.Args(
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Expiration(core.Schema):

    date: str | core.StringOut | None = core.attr(str, default=None)

    days: int | core.IntOut | None = core.attr(int, default=None)

    expired_object_delete_marker: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        date: str | core.StringOut | None = None,
        days: int | core.IntOut | None = None,
        expired_object_delete_marker: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Expiration.Args(
                date=date,
                days=days,
                expired_object_delete_marker=expired_object_delete_marker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date: str | core.StringOut | None = core.arg(default=None)

        days: int | core.IntOut | None = core.arg(default=None)

        expired_object_delete_marker: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Transition(core.Schema):

    date: str | core.StringOut | None = core.attr(str, default=None)

    days: int | core.IntOut | None = core.attr(int, default=None)

    storage_class: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: str | core.StringOut,
        date: str | core.StringOut | None = None,
        days: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Transition.Args(
                storage_class=storage_class,
                date=date,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date: str | core.StringOut | None = core.arg(default=None)

        days: int | core.IntOut | None = core.arg(default=None)

        storage_class: str | core.StringOut = core.arg()


@core.schema
class LifecycleRule(core.Schema):

    abort_incomplete_multipart_upload_days: int | core.IntOut | None = core.attr(int, default=None)

    enabled: bool | core.BoolOut = core.attr(bool)

    expiration: Expiration | None = core.attr(Expiration, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    noncurrent_version_expiration: NoncurrentVersionExpiration | None = core.attr(
        NoncurrentVersionExpiration, default=None
    )

    noncurrent_version_transition: list[NoncurrentVersionTransition] | core.ArrayOut[
        NoncurrentVersionTransition
    ] | None = core.attr(NoncurrentVersionTransition, default=None, kind=core.Kind.array)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    transition: list[Transition] | core.ArrayOut[Transition] | None = core.attr(
        Transition, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        abort_incomplete_multipart_upload_days: int | core.IntOut | None = None,
        expiration: Expiration | None = None,
        id: str | core.StringOut | None = None,
        noncurrent_version_expiration: NoncurrentVersionExpiration | None = None,
        noncurrent_version_transition: list[NoncurrentVersionTransition]
        | core.ArrayOut[NoncurrentVersionTransition]
        | None = None,
        prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transition: list[Transition] | core.ArrayOut[Transition] | None = None,
    ):
        super().__init__(
            args=LifecycleRule.Args(
                enabled=enabled,
                abort_incomplete_multipart_upload_days=abort_incomplete_multipart_upload_days,
                expiration=expiration,
                id=id,
                noncurrent_version_expiration=noncurrent_version_expiration,
                noncurrent_version_transition=noncurrent_version_transition,
                prefix=prefix,
                tags=tags,
                transition=transition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        abort_incomplete_multipart_upload_days: int | core.IntOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut = core.arg()

        expiration: Expiration | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        noncurrent_version_expiration: NoncurrentVersionExpiration | None = core.arg(default=None)

        noncurrent_version_transition: list[NoncurrentVersionTransition] | core.ArrayOut[
            NoncurrentVersionTransition
        ] | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transition: list[Transition] | core.ArrayOut[Transition] | None = core.arg(default=None)


@core.schema
class Website(core.Schema):

    error_document: str | core.StringOut | None = core.attr(str, default=None)

    index_document: str | core.StringOut | None = core.attr(str, default=None)

    redirect_all_requests_to: str | core.StringOut | None = core.attr(str, default=None)

    routing_rules: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        error_document: str | core.StringOut | None = None,
        index_document: str | core.StringOut | None = None,
        redirect_all_requests_to: str | core.StringOut | None = None,
        routing_rules: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Website.Args(
                error_document=error_document,
                index_document=index_document,
                redirect_all_requests_to=redirect_all_requests_to,
                routing_rules=routing_rules,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_document: str | core.StringOut | None = core.arg(default=None)

        index_document: str | core.StringOut | None = core.arg(default=None)

        redirect_all_requests_to: str | core.StringOut | None = core.arg(default=None)

        routing_rules: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CorsRule(core.Schema):

    allowed_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    allowed_origins: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_age_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allowed_methods: list[str] | core.ArrayOut[core.StringOut],
        allowed_origins: list[str] | core.ArrayOut[core.StringOut],
        allowed_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        max_age_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CorsRule.Args(
                allowed_methods=allowed_methods,
                allowed_origins=allowed_origins,
                allowed_headers=allowed_headers,
                expose_headers=expose_headers,
                max_age_seconds=max_age_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allowed_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        allowed_origins: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_age_seconds: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Versioning(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    mfa_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        mfa_delete: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Versioning.Args(
                enabled=enabled,
                mfa_delete=mfa_delete,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        mfa_delete: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class ReplicationTime(core.Schema):

    minutes: int | core.IntOut | None = core.attr(int, default=None)

    status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        minutes: int | core.IntOut | None = None,
        status: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ReplicationTime.Args(
                minutes=minutes,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: int | core.IntOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Metrics(core.Schema):

    minutes: int | core.IntOut | None = core.attr(int, default=None)

    status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        minutes: int | core.IntOut | None = None,
        status: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Metrics.Args(
                minutes=minutes,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: int | core.IntOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AccessControlTranslation(core.Schema):

    owner: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        owner: str | core.StringOut,
    ):
        super().__init__(
            args=AccessControlTranslation.Args(
                owner=owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        owner: str | core.StringOut = core.arg()


@core.schema
class Destination(core.Schema):

    access_control_translation: AccessControlTranslation | None = core.attr(
        AccessControlTranslation, default=None
    )

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    bucket: str | core.StringOut = core.attr(str)

    metrics: Metrics | None = core.attr(Metrics, default=None)

    replica_kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    replication_time: ReplicationTime | None = core.attr(ReplicationTime, default=None)

    storage_class: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        access_control_translation: AccessControlTranslation | None = None,
        account_id: str | core.StringOut | None = None,
        metrics: Metrics | None = None,
        replica_kms_key_id: str | core.StringOut | None = None,
        replication_time: ReplicationTime | None = None,
        storage_class: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Destination.Args(
                bucket=bucket,
                access_control_translation=access_control_translation,
                account_id=account_id,
                metrics=metrics,
                replica_kms_key_id=replica_kms_key_id,
                replication_time=replication_time,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_translation: AccessControlTranslation | None = core.arg(default=None)

        account_id: str | core.StringOut | None = core.arg(default=None)

        bucket: str | core.StringOut = core.arg()

        metrics: Metrics | None = core.arg(default=None)

        replica_kms_key_id: str | core.StringOut | None = core.arg(default=None)

        replication_time: ReplicationTime | None = core.arg(default=None)

        storage_class: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SseKmsEncryptedObjects(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=SseKmsEncryptedObjects.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class SourceSelectionCriteria(core.Schema):

    sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = core.attr(
        SseKmsEncryptedObjects, default=None
    )

    def __init__(
        self,
        *,
        sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = None,
    ):
        super().__init__(
            args=SourceSelectionCriteria.Args(
                sse_kms_encrypted_objects=sse_kms_encrypted_objects,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = core.arg(default=None)


@core.schema
class Rules(core.Schema):

    delete_marker_replication_status: str | core.StringOut | None = core.attr(str, default=None)

    destination: Destination = core.attr(Destination)

    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    priority: int | core.IntOut | None = core.attr(int, default=None)

    source_selection_criteria: SourceSelectionCriteria | None = core.attr(
        SourceSelectionCriteria, default=None
    )

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        destination: Destination,
        status: str | core.StringOut,
        delete_marker_replication_status: str | core.StringOut | None = None,
        filter: Filter | None = None,
        id: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        priority: int | core.IntOut | None = None,
        source_selection_criteria: SourceSelectionCriteria | None = None,
    ):
        super().__init__(
            args=Rules.Args(
                destination=destination,
                status=status,
                delete_marker_replication_status=delete_marker_replication_status,
                filter=filter,
                id=id,
                prefix=prefix,
                priority=priority,
                source_selection_criteria=source_selection_criteria,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_marker_replication_status: str | core.StringOut | None = core.arg(default=None)

        destination: Destination = core.arg()

        filter: Filter | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        priority: int | core.IntOut | None = core.arg(default=None)

        source_selection_criteria: SourceSelectionCriteria | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()


@core.schema
class ReplicationConfiguration(core.Schema):

    role: str | core.StringOut = core.attr(str)

    rules: list[Rules] | core.ArrayOut[Rules] = core.attr(Rules, kind=core.Kind.array)

    def __init__(
        self,
        *,
        role: str | core.StringOut,
        rules: list[Rules] | core.ArrayOut[Rules],
    ):
        super().__init__(
            args=ReplicationConfiguration.Args(
                role=role,
                rules=rules,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role: str | core.StringOut = core.arg()

        rules: list[Rules] | core.ArrayOut[Rules] = core.arg()


@core.schema
class DefaultRetention(core.Schema):

    days: int | core.IntOut | None = core.attr(int, default=None)

    mode: str | core.StringOut = core.attr(str)

    years: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        mode: str | core.StringOut,
        days: int | core.IntOut | None = None,
        years: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DefaultRetention.Args(
                mode=mode,
                days=days,
                years=years,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: int | core.IntOut | None = core.arg(default=None)

        mode: str | core.StringOut = core.arg()

        years: int | core.IntOut | None = core.arg(default=None)


@core.schema
class ObjectLockConfigurationRule(core.Schema):

    default_retention: DefaultRetention = core.attr(DefaultRetention)

    def __init__(
        self,
        *,
        default_retention: DefaultRetention,
    ):
        super().__init__(
            args=ObjectLockConfigurationRule.Args(
                default_retention=default_retention,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_retention: DefaultRetention = core.arg()


@core.schema
class ObjectLockConfiguration(core.Schema):

    object_lock_enabled: str | core.StringOut | None = core.attr(str, default=None)

    rule: ObjectLockConfigurationRule | None = core.attr(ObjectLockConfigurationRule, default=None)

    def __init__(
        self,
        *,
        object_lock_enabled: str | core.StringOut | None = None,
        rule: ObjectLockConfigurationRule | None = None,
    ):
        super().__init__(
            args=ObjectLockConfiguration.Args(
                object_lock_enabled=object_lock_enabled,
                rule=rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object_lock_enabled: str | core.StringOut | None = core.arg(default=None)

        rule: ObjectLockConfigurationRule | None = core.arg(default=None)


@core.resource(type="aws_s3_bucket", namespace="aws_s3")
class Bucket(core.Resource):

    acceleration_status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    acl: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    bucket: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    bucket_domain_name: str | core.StringOut = core.attr(str, computed=True)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    bucket_regional_domain_name: str | core.StringOut = core.attr(str, computed=True)

    cors_rule: list[CorsRule] | core.ArrayOut[CorsRule] | None = core.attr(
        CorsRule, default=None, computed=True, kind=core.Kind.array
    )

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    grant: list[Grant] | core.ArrayOut[Grant] | None = core.attr(
        Grant, default=None, computed=True, kind=core.Kind.array
    )

    hosted_zone_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    lifecycle_rule: list[LifecycleRule] | core.ArrayOut[LifecycleRule] | None = core.attr(
        LifecycleRule, default=None, computed=True, kind=core.Kind.array
    )

    logging: Logging | None = core.attr(Logging, default=None, computed=True)

    object_lock_configuration: ObjectLockConfiguration | None = core.attr(
        ObjectLockConfiguration, default=None, computed=True
    )

    object_lock_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    region: str | core.StringOut = core.attr(str, computed=True)

    replication_configuration: ReplicationConfiguration | None = core.attr(
        ReplicationConfiguration, default=None, computed=True
    )

    request_payer: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = core.attr(
        ServerSideEncryptionConfiguration, default=None, computed=True
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    versioning: Versioning | None = core.attr(Versioning, default=None, computed=True)

    website: Website | None = core.attr(Website, default=None, computed=True)

    website_domain: str | core.StringOut = core.attr(str, computed=True)

    website_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        acceleration_status: str | core.StringOut | None = None,
        acl: str | core.StringOut | None = None,
        arn: str | core.StringOut | None = None,
        bucket: str | core.StringOut | None = None,
        bucket_prefix: str | core.StringOut | None = None,
        cors_rule: list[CorsRule] | core.ArrayOut[CorsRule] | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        grant: list[Grant] | core.ArrayOut[Grant] | None = None,
        hosted_zone_id: str | core.StringOut | None = None,
        lifecycle_rule: list[LifecycleRule] | core.ArrayOut[LifecycleRule] | None = None,
        logging: Logging | None = None,
        object_lock_configuration: ObjectLockConfiguration | None = None,
        object_lock_enabled: bool | core.BoolOut | None = None,
        policy: str | core.StringOut | None = None,
        replication_configuration: ReplicationConfiguration | None = None,
        request_payer: str | core.StringOut | None = None,
        server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        versioning: Versioning | None = None,
        website: Website | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Bucket.Args(
                acceleration_status=acceleration_status,
                acl=acl,
                arn=arn,
                bucket=bucket,
                bucket_prefix=bucket_prefix,
                cors_rule=cors_rule,
                force_destroy=force_destroy,
                grant=grant,
                hosted_zone_id=hosted_zone_id,
                lifecycle_rule=lifecycle_rule,
                logging=logging,
                object_lock_configuration=object_lock_configuration,
                object_lock_enabled=object_lock_enabled,
                policy=policy,
                replication_configuration=replication_configuration,
                request_payer=request_payer,
                server_side_encryption_configuration=server_side_encryption_configuration,
                tags=tags,
                tags_all=tags_all,
                versioning=versioning,
                website=website,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acceleration_status: str | core.StringOut | None = core.arg(default=None)

        acl: str | core.StringOut | None = core.arg(default=None)

        arn: str | core.StringOut | None = core.arg(default=None)

        bucket: str | core.StringOut | None = core.arg(default=None)

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        cors_rule: list[CorsRule] | core.ArrayOut[CorsRule] | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        grant: list[Grant] | core.ArrayOut[Grant] | None = core.arg(default=None)

        hosted_zone_id: str | core.StringOut | None = core.arg(default=None)

        lifecycle_rule: list[LifecycleRule] | core.ArrayOut[LifecycleRule] | None = core.arg(
            default=None
        )

        logging: Logging | None = core.arg(default=None)

        object_lock_configuration: ObjectLockConfiguration | None = core.arg(default=None)

        object_lock_enabled: bool | core.BoolOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        replication_configuration: ReplicationConfiguration | None = core.arg(default=None)

        request_payer: str | core.StringOut | None = core.arg(default=None)

        server_side_encryption_configuration: ServerSideEncryptionConfiguration | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        versioning: Versioning | None = core.arg(default=None)

        website: Website | None = core.arg(default=None)
