import terrascript.core as core


@core.data(type="aws_cloudwatch_event_source", namespace="eventbridge")
class DsCloudwatchEventSource(core.Data):
    """
    The ARN of the partner event source
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the SaaS partner that created the event source
    """
    created_by: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the event source
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifying this limits the results to only those partner event sources with names that st
    art with the specified prefix
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    The state of the event source (`ACTIVE` or `PENDING`)
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCloudwatchEventSource.Args(
                name_prefix=name_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_prefix: str | core.StringOut | None = core.arg(default=None)
