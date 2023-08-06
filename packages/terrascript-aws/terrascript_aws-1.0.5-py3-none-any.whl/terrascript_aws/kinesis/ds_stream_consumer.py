import terrascript.core as core


@core.data(type="aws_kinesis_stream_consumer", namespace="kinesis")
class DsStreamConsumer(core.Data):
    """
    (Optional) Amazon Resource Name (ARN) of the stream consumer.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Approximate timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of when t
    he stream consumer was created.
    """
    creation_timestamp: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the stream consumer.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Name of the stream consumer.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The current status of the stream consumer.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the data stream the consumer is registered with.
    """
    stream_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        stream_arn: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsStreamConsumer.Args(
                stream_arn=stream_arn,
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        stream_arn: str | core.StringOut = core.arg()
