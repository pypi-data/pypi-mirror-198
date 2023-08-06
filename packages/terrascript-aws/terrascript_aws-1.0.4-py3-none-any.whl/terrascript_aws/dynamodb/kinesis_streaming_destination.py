import terrascript.core as core


@core.resource(type="aws_dynamodb_kinesis_streaming_destination", namespace="dynamodb")
class KinesisStreamingDestination(core.Resource):
    """
    The `table_name` and `stream_arn` separated by a comma (`,`).
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN for a Kinesis data stream. This must exist in the same account and region as the
    DynamoDB table.
    """
    stream_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the DynamoDB table. There
    """
    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        stream_arn: str | core.StringOut,
        table_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=KinesisStreamingDestination.Args(
                stream_arn=stream_arn,
                table_name=table_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        stream_arn: str | core.StringOut = core.arg()

        table_name: str | core.StringOut = core.arg()
