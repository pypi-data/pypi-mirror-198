import terrascript.core as core


@core.resource(type="aws_kinesis_stream_consumer", namespace="kinesis")
class StreamConsumer(core.Resource):
    """
    Amazon Resource Name (ARN) of the stream consumer.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

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
    (Required, Forces new resource) Name of the stream consumer.
    """
    name: str | core.StringOut = core.attr(str)

    stream_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        stream_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StreamConsumer.Args(
                name=name,
                stream_arn=stream_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        stream_arn: str | core.StringOut = core.arg()
