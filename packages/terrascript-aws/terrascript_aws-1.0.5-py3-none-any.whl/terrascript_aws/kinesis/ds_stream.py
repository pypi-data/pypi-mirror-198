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


@core.data(type="aws_kinesis_stream", namespace="kinesis")
class DsStream(core.Data):
    """
    The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The list of shard ids in the CLOSED state. See [Shard State][2] for more.
    """
    closed_shards: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The approximate UNIX timestamp that the stream was created.
    """
    creation_timestamp: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Kinesis Stream.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The list of shard ids in the OPEN state. See [Shard State][2] for more.
    """
    open_shards: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Length of time (in hours) data records are accessible after they are added to the stream.
    """
    retention_period: int | core.IntOut = core.attr(int, computed=True)

    """
    A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with Clou
    dWatch][3] for more.
    """
    shard_level_metrics: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATIN
    G.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates the [capacity mode][4] of the data stream. Detailed below.
    """
    stream_mode_details: list[StreamModeDetails] | core.ArrayOut[StreamModeDetails] = core.attr(
        StreamModeDetails, computed=True, kind=core.Kind.array
    )

    """
    A map of tags to assigned to the stream.
    """
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
