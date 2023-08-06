import terrascript.core as core


@core.schema
class ReplicaModifications(core.Schema):

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=ReplicaModifications.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()


@core.schema
class SseKmsEncryptedObjects(core.Schema):

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=SseKmsEncryptedObjects.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()


@core.schema
class SourceSelectionCriteria(core.Schema):

    replica_modifications: ReplicaModifications | None = core.attr(
        ReplicaModifications, default=None
    )

    sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = core.attr(
        SseKmsEncryptedObjects, default=None
    )

    def __init__(
        self,
        *,
        replica_modifications: ReplicaModifications | None = None,
        sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = None,
    ):
        super().__init__(
            args=SourceSelectionCriteria.Args(
                replica_modifications=replica_modifications,
                sse_kms_encrypted_objects=sse_kms_encrypted_objects,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replica_modifications: ReplicaModifications | None = core.arg(default=None)

        sse_kms_encrypted_objects: SseKmsEncryptedObjects | None = core.arg(default=None)


@core.schema
class DeleteMarkerReplication(core.Schema):

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=DeleteMarkerReplication.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()


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
class EncryptionConfiguration(core.Schema):

    replica_kms_key_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        replica_kms_key_id: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                replica_kms_key_id=replica_kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replica_kms_key_id: str | core.StringOut = core.arg()


@core.schema
class EventThreshold(core.Schema):

    minutes: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        minutes: int | core.IntOut,
    ):
        super().__init__(
            args=EventThreshold.Args(
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: int | core.IntOut = core.arg()


@core.schema
class Metrics(core.Schema):

    event_threshold: EventThreshold | None = core.attr(EventThreshold, default=None)

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
        event_threshold: EventThreshold | None = None,
    ):
        super().__init__(
            args=Metrics.Args(
                status=status,
                event_threshold=event_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_threshold: EventThreshold | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()


@core.schema
class Time(core.Schema):

    minutes: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        minutes: int | core.IntOut,
    ):
        super().__init__(
            args=Time.Args(
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: int | core.IntOut = core.arg()


@core.schema
class ReplicationTime(core.Schema):

    status: str | core.StringOut = core.attr(str)

    time: Time = core.attr(Time)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
        time: Time,
    ):
        super().__init__(
            args=ReplicationTime.Args(
                status=status,
                time=time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()

        time: Time = core.arg()


@core.schema
class Destination(core.Schema):

    access_control_translation: AccessControlTranslation | None = core.attr(
        AccessControlTranslation, default=None
    )

    account: str | core.StringOut | None = core.attr(str, default=None)

    bucket: str | core.StringOut = core.attr(str)

    encryption_configuration: EncryptionConfiguration | None = core.attr(
        EncryptionConfiguration, default=None
    )

    metrics: Metrics | None = core.attr(Metrics, default=None)

    replication_time: ReplicationTime | None = core.attr(ReplicationTime, default=None)

    storage_class: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        access_control_translation: AccessControlTranslation | None = None,
        account: str | core.StringOut | None = None,
        encryption_configuration: EncryptionConfiguration | None = None,
        metrics: Metrics | None = None,
        replication_time: ReplicationTime | None = None,
        storage_class: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Destination.Args(
                bucket=bucket,
                access_control_translation=access_control_translation,
                account=account,
                encryption_configuration=encryption_configuration,
                metrics=metrics,
                replication_time=replication_time,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_translation: AccessControlTranslation | None = core.arg(default=None)

        account: str | core.StringOut | None = core.arg(default=None)

        bucket: str | core.StringOut = core.arg()

        encryption_configuration: EncryptionConfiguration | None = core.arg(default=None)

        metrics: Metrics | None = core.arg(default=None)

        replication_time: ReplicationTime | None = core.arg(default=None)

        storage_class: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ExistingObjectReplication(core.Schema):

    status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=ExistingObjectReplication.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: str | core.StringOut = core.arg()


@core.schema
class And(core.Schema):

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
            args=And.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Tag(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Filter(core.Schema):

    and_: And | None = core.attr(And, default=None, alias="and")

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    tag: Tag | None = core.attr(Tag, default=None)

    def __init__(
        self,
        *,
        and_: And | None = None,
        prefix: str | core.StringOut | None = None,
        tag: Tag | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                and_=and_,
                prefix=prefix,
                tag=tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: And | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        tag: Tag | None = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    delete_marker_replication: DeleteMarkerReplication | None = core.attr(
        DeleteMarkerReplication, default=None
    )

    destination: Destination = core.attr(Destination)

    existing_object_replication: ExistingObjectReplication | None = core.attr(
        ExistingObjectReplication, default=None
    )

    filter: Filter | None = core.attr(Filter, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

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
        delete_marker_replication: DeleteMarkerReplication | None = None,
        existing_object_replication: ExistingObjectReplication | None = None,
        filter: Filter | None = None,
        id: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        priority: int | core.IntOut | None = None,
        source_selection_criteria: SourceSelectionCriteria | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                destination=destination,
                status=status,
                delete_marker_replication=delete_marker_replication,
                existing_object_replication=existing_object_replication,
                filter=filter,
                id=id,
                prefix=prefix,
                priority=priority,
                source_selection_criteria=source_selection_criteria,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_marker_replication: DeleteMarkerReplication | None = core.arg(default=None)

        destination: Destination = core.arg()

        existing_object_replication: ExistingObjectReplication | None = core.arg(default=None)

        filter: Filter | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)

        priority: int | core.IntOut | None = core.arg(default=None)

        source_selection_criteria: SourceSelectionCriteria | None = core.arg(default=None)

        status: str | core.StringOut = core.arg()


@core.resource(type="aws_s3_bucket_replication_configuration", namespace="s3")
class BucketReplicationConfiguration(core.Resource):
    """
    (Required) The name of the source S3 bucket you want Amazon S3 to monitor.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Unique identifier for the rule. Must be less than or equal to 255 characters in length.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of the IAM role for Amazon S3 to assume when replicating the objects.
    """
    role: str | core.StringOut = core.attr(str)

    """
    (Required) List of configuration blocks describing the rules managing the replication [documented be
    low](#rule).
    """
    rule: list[Rule] | core.ArrayOut[Rule] = core.attr(Rule, kind=core.Kind.array)

    """
    (Optional) A token to allow replication to be enabled on an Object Lock-enabled bucket. You must con
    tact AWS support for the bucket's "Object Lock token".
    """
    token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        role: str | core.StringOut,
        rule: list[Rule] | core.ArrayOut[Rule],
        token: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketReplicationConfiguration.Args(
                bucket=bucket,
                role=role,
                rule=rule,
                token=token,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        role: str | core.StringOut = core.arg()

        rule: list[Rule] | core.ArrayOut[Rule] = core.arg()

        token: str | core.StringOut | None = core.arg(default=None)
