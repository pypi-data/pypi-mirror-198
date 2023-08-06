import terrascript.core as core


@core.schema
class EncryptionConfig(core.Schema):

    encryption_type: str | core.StringOut = core.attr(str)

    key_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        encryption_type: str | core.StringOut,
        key_id: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionConfig.Args(
                encryption_type=encryption_type,
                key_id=key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: str | core.StringOut = core.arg()

        key_id: str | core.StringOut = core.arg()


@core.schema
class S3Config(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut = core.attr(str)

    encryption_config: EncryptionConfig | None = core.attr(EncryptionConfig, default=None)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        bucket_prefix: str | core.StringOut,
        encryption_config: EncryptionConfig | None = None,
    ):
        super().__init__(
            args=S3Config.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                encryption_config=encryption_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut = core.arg()

        encryption_config: EncryptionConfig | None = core.arg(default=None)


@core.schema
class KinesisFirehoseConfig(core.Schema):

    firehose_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        firehose_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisFirehoseConfig.Args(
                firehose_arn=firehose_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        firehose_arn: str | core.StringOut = core.arg()


@core.schema
class KinesisStreamConfig(core.Schema):

    stream_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        stream_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisStreamConfig.Args(
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stream_arn: str | core.StringOut = core.arg()


@core.schema
class KinesisVideoStreamConfig(core.Schema):

    encryption_config: EncryptionConfig = core.attr(EncryptionConfig)

    prefix: str | core.StringOut = core.attr(str)

    retention_period_hours: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        encryption_config: EncryptionConfig,
        prefix: str | core.StringOut,
        retention_period_hours: int | core.IntOut,
    ):
        super().__init__(
            args=KinesisVideoStreamConfig.Args(
                encryption_config=encryption_config,
                prefix=prefix,
                retention_period_hours=retention_period_hours,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_config: EncryptionConfig = core.arg()

        prefix: str | core.StringOut = core.arg()

        retention_period_hours: int | core.IntOut = core.arg()


@core.schema
class StorageConfig(core.Schema):

    kinesis_firehose_config: KinesisFirehoseConfig | None = core.attr(
        KinesisFirehoseConfig, default=None
    )

    kinesis_stream_config: KinesisStreamConfig | None = core.attr(KinesisStreamConfig, default=None)

    kinesis_video_stream_config: KinesisVideoStreamConfig | None = core.attr(
        KinesisVideoStreamConfig, default=None
    )

    s3_config: S3Config | None = core.attr(S3Config, default=None)

    storage_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        storage_type: str | core.StringOut,
        kinesis_firehose_config: KinesisFirehoseConfig | None = None,
        kinesis_stream_config: KinesisStreamConfig | None = None,
        kinesis_video_stream_config: KinesisVideoStreamConfig | None = None,
        s3_config: S3Config | None = None,
    ):
        super().__init__(
            args=StorageConfig.Args(
                storage_type=storage_type,
                kinesis_firehose_config=kinesis_firehose_config,
                kinesis_stream_config=kinesis_stream_config,
                kinesis_video_stream_config=kinesis_video_stream_config,
                s3_config=s3_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kinesis_firehose_config: KinesisFirehoseConfig | None = core.arg(default=None)

        kinesis_stream_config: KinesisStreamConfig | None = core.arg(default=None)

        kinesis_video_stream_config: KinesisVideoStreamConfig | None = core.arg(default=None)

        s3_config: S3Config | None = core.arg(default=None)

        storage_type: str | core.StringOut = core.arg()


@core.resource(type="aws_connect_instance_storage_config", namespace="connect")
class InstanceStorageConfig(core.Resource):
    """
    The existing association identifier that uniquely identifies the resource type and storage config fo
    r the given instance ID.
    """

    association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance, `association_id`, and `resource_type` separat
    ed by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) A valid resource type. Valid Values: `CHAT_TRANSCRIPTS` | `CALL_RECORDINGS` | `SCHEDULED_
    REPORTS` | `MEDIA_STREAMS` | `CONTACT_TRACE_RECORDS` | `AGENT_EVENTS` | `REAL_TIME_CONTACT_ANALYSIS_
    SEGMENTS`.
    """
    resource_type: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the storage configuration options for the Connect Instance. [Documented below](
    #storage_config).
    """
    storage_config: StorageConfig = core.attr(StorageConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: str | core.StringOut,
        resource_type: str | core.StringOut,
        storage_config: StorageConfig,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceStorageConfig.Args(
                instance_id=instance_id,
                resource_type=resource_type,
                storage_config=storage_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_id: str | core.StringOut = core.arg()

        resource_type: str | core.StringOut = core.arg()

        storage_config: StorageConfig = core.arg()
