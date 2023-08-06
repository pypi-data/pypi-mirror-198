import terrascript.core as core


@core.data(type="aws_cloudwatch_event_source", namespace="aws_eventbridge")
class DsCloudwatchEventSource(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    created_by: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

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
