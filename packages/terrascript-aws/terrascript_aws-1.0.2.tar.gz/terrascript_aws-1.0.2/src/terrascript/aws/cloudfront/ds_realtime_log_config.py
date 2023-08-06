import terrascript.core as core


@core.schema
class KinesisStreamConfig(core.Schema):

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    stream_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        stream_arn: str | core.StringOut,
    ):
        super().__init__(
            args=KinesisStreamConfig.Args(
                role_arn=role_arn,
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: str | core.StringOut = core.arg()

        stream_arn: str | core.StringOut = core.arg()


@core.schema
class Endpoint(core.Schema):

    kinesis_stream_config: list[KinesisStreamConfig] | core.ArrayOut[
        KinesisStreamConfig
    ] = core.attr(KinesisStreamConfig, computed=True, kind=core.Kind.array)

    stream_type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        kinesis_stream_config: list[KinesisStreamConfig] | core.ArrayOut[KinesisStreamConfig],
        stream_type: str | core.StringOut,
    ):
        super().__init__(
            args=Endpoint.Args(
                kinesis_stream_config=kinesis_stream_config,
                stream_type=stream_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kinesis_stream_config: list[KinesisStreamConfig] | core.ArrayOut[
            KinesisStreamConfig
        ] = core.arg()

        stream_type: str | core.StringOut = core.arg()


@core.data(type="aws_cloudfront_realtime_log_config", namespace="aws_cloudfront")
class DsRealtimeLogConfig(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    endpoint: list[Endpoint] | core.ArrayOut[Endpoint] = core.attr(
        Endpoint, computed=True, kind=core.Kind.array
    )

    fields: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    sampling_rate: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsRealtimeLogConfig.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
