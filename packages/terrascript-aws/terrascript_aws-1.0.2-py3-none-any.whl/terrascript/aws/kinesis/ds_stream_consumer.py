import terrascript.core as core


@core.data(type="aws_kinesis_stream_consumer", namespace="aws_kinesis")
class DsStreamConsumer(core.Data):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    creation_timestamp: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

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
