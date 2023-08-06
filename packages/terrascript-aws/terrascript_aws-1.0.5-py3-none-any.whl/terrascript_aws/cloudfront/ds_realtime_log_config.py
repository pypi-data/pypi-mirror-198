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


@core.data(type="aws_cloudfront_realtime_log_config", namespace="cloudfront")
class DsRealtimeLogConfig(core.Data):
    """
    The ARN (Amazon Resource Name) of the CloudFront real-time log configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Amazon Kinesis data streams where real-time log data is sent.
    """
    endpoint: list[Endpoint] | core.ArrayOut[Endpoint] = core.attr(
        Endpoint, computed=True, kind=core.Kind.array
    )

    """
    (Required) The fields that are included in each real-time log record. See the [AWS documentation](ht
    tps://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real
    time-log-config-fields) for supported values.
    """
    fields: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

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
