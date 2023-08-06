import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_stream", namespace="cloudwatch")
class LogStream(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the log stream.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the log group under which the log stream is to be created.
    """
    log_group_name: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the log stream. Must not be longer than 512 characters and must not contain `
    :`
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        log_group_name: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogStream.Args(
                log_group_name=log_group_name,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_group_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
