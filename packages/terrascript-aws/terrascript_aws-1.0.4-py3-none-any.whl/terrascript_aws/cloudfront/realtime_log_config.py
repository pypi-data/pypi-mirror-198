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


@core.resource(type="aws_cloudfront_realtime_log_config", namespace="cloudfront")
class RealtimeLogConfig(core.Resource):
    """
    The ARN (Amazon Resource Name) of the CloudFront real-time log configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Kinesis data streams where real-time log data is sent.
    """
    endpoint: Endpoint = core.attr(Endpoint)

    """
    (Required) The fields that are included in each real-time log record. See the [AWS documentation](ht
    tps://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real
    time-log-config-fields) for supported values.
    """
    fields: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    The ID of the CloudFront real-time log configuration.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The unique name to identify this real-time log configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The sampling rate for this real-time log configuration. The sampling rate determines the
    percentage of viewer requests that are represented in the real-time log data. An integer between `1`
    and `100`, inclusive.
    """
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
