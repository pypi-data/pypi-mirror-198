import terrascript.core as core


@core.resource(type="aws_iot_logging_options", namespace="aws_iot")
class LoggingOptions(core.Resource):

    default_log_level: str | core.StringOut = core.attr(str)

    disable_all_logs: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        default_log_level: str | core.StringOut,
        role_arn: str | core.StringOut,
        disable_all_logs: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoggingOptions.Args(
                default_log_level=default_log_level,
                role_arn=role_arn,
                disable_all_logs=disable_all_logs,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_log_level: str | core.StringOut = core.arg()

        disable_all_logs: bool | core.BoolOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()
