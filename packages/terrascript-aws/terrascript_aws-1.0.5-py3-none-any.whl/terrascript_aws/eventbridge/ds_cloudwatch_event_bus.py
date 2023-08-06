import terrascript.core as core


@core.data(type="aws_cloudwatch_event_bus", namespace="eventbridge")
class DsCloudwatchEventBus(core.Data):
    """
    The Amazon Resource Name (ARN) specifying the role.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly EventBridge event bus name.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsCloudwatchEventBus.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
