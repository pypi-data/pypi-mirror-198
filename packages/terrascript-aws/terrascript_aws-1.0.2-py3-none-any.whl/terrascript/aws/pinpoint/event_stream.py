import terrascript.core as core


@core.resource(type="aws_pinpoint_event_stream", namespace="aws_pinpoint")
class EventStream(core.Resource):
    """
    (Required) The application ID.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream t
    o which you want to publish events.
    """
    destination_stream_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your acco
    unt.
    """
    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        destination_stream_arn: str | core.StringOut,
        role_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventStream.Args(
                application_id=application_id,
                destination_stream_arn=destination_stream_arn,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        destination_stream_arn: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()
