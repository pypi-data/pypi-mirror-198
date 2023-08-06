import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_bus_policy", namespace="aws_eventbridge")
class CloudwatchEventBusPolicy(core.Resource):

    event_bus_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        event_bus_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventBusPolicy.Args(
                policy=policy,
                event_bus_name=event_bus_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        event_bus_name: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut = core.arg()
