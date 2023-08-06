import terrascript.core as core


@core.resource(type="aws_kinesis_stream_consumer", namespace="aws_kinesis")
class StreamConsumer(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    creation_timestamp: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

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
