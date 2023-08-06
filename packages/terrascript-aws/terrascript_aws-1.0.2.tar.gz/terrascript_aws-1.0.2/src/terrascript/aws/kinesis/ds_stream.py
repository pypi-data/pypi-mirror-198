import terrascript.core as core


@core.schema
class StreamModeDetails(core.Schema):

    stream_mode: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_kinesis_stream", namespace="aws_kinesis")
class DsStream(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    closed_shards: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    creation_timestamp: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    open_shards: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    retention_period: int | core.IntOut = core.attr(int, computed=True)

    shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    stream_mode_details: list[StreamModeDetails] | core.ArrayOut[StreamModeDetails] = core.attr(
        StreamModeDetails, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsStream.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
