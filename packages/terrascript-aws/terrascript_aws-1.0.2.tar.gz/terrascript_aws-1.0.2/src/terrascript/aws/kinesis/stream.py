import terrascript.core as core


@core.schema
class StreamModeDetails(core.Schema):

    stream_mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        stream_mode: str | core.StringOut,
    ):
        super().__init__(
            args=StreamModeDetails.Args(
                stream_mode=stream_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stream_mode: str | core.StringOut = core.arg()


@core.resource(type="aws_kinesis_stream", namespace="aws_kinesis")
class Stream(core.Resource):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    encryption_type: str | core.StringOut | None = core.attr(str, default=None)

    enforce_consumer_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    retention_period: int | core.IntOut | None = core.attr(int, default=None)

    shard_count: int | core.IntOut | None = core.attr(int, default=None)

    shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    stream_mode_details: StreamModeDetails | None = core.attr(
        StreamModeDetails, default=None, computed=True
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        encryption_type: str | core.StringOut | None = None,
        enforce_consumer_deletion: bool | core.BoolOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        retention_period: int | core.IntOut | None = None,
        shard_count: int | core.IntOut | None = None,
        shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] | None = None,
        stream_mode_details: StreamModeDetails | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stream.Args(
                name=name,
                arn=arn,
                encryption_type=encryption_type,
                enforce_consumer_deletion=enforce_consumer_deletion,
                kms_key_id=kms_key_id,
                retention_period=retention_period,
                shard_count=shard_count,
                shard_level_metrics=shard_level_metrics,
                stream_mode_details=stream_mode_details,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: str | core.StringOut | None = core.arg(default=None)

        encryption_type: str | core.StringOut | None = core.arg(default=None)

        enforce_consumer_deletion: bool | core.BoolOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        retention_period: int | core.IntOut | None = core.arg(default=None)

        shard_count: int | core.IntOut | None = core.arg(default=None)

        shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        stream_mode_details: StreamModeDetails | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
