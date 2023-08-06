import terrascript.core as core


@core.schema
class KinesisStreamConfig(core.Schema):

    role_arn: str | core.StringOut = core.attr(str)

    stream_arn: str | core.StringOut = core.attr(str)

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

    kinesis_stream_config: KinesisStreamConfig = core.attr(KinesisStreamConfig)

    stream_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        kinesis_stream_config: KinesisStreamConfig,
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
        kinesis_stream_config: KinesisStreamConfig = core.arg()

        stream_type: str | core.StringOut = core.arg()


@core.resource(type="aws_cloudfront_realtime_log_config", namespace="aws_cloudfront")
class RealtimeLogConfig(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    endpoint: Endpoint = core.attr(Endpoint)

    fields: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    sampling_rate: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint: Endpoint,
        fields: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        sampling_rate: int | core.IntOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RealtimeLogConfig.Args(
                endpoint=endpoint,
                fields=fields,
                name=name,
                sampling_rate=sampling_rate,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        endpoint: Endpoint = core.arg()

        fields: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        sampling_rate: int | core.IntOut = core.arg()
