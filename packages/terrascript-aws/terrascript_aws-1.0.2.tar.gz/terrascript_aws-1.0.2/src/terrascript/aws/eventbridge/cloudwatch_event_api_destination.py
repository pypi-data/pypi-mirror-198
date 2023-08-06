import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_api_destination", namespace="aws_eventbridge")
class CloudwatchEventApiDestination(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    connection_arn: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    invocation_endpoint: str | core.StringOut = core.attr(str)

    invocation_rate_limit_per_second: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_arn: str | core.StringOut,
        http_method: str | core.StringOut,
        invocation_endpoint: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        invocation_rate_limit_per_second: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventApiDestination.Args(
                connection_arn=connection_arn,
                http_method=http_method,
                invocation_endpoint=invocation_endpoint,
                name=name,
                description=description,
                invocation_rate_limit_per_second=invocation_rate_limit_per_second,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_arn: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        http_method: str | core.StringOut = core.arg()

        invocation_endpoint: str | core.StringOut = core.arg()

        invocation_rate_limit_per_second: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
