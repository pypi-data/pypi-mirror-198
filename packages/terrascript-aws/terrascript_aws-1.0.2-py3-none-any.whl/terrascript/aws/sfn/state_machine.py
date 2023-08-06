import terrascript.core as core


@core.schema
class TracingConfiguration(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=TracingConfiguration.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class LoggingConfiguration(core.Schema):

    include_execution_data: bool | core.BoolOut | None = core.attr(bool, default=None)

    level: str | core.StringOut | None = core.attr(str, default=None)

    log_destination: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        include_execution_data: bool | core.BoolOut | None = None,
        level: str | core.StringOut | None = None,
        log_destination: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LoggingConfiguration.Args(
                include_execution_data=include_execution_data,
                level=level,
                log_destination=log_destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        include_execution_data: bool | core.BoolOut | None = core.arg(default=None)

        level: str | core.StringOut | None = core.arg(default=None)

        log_destination: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_sfn_state_machine", namespace="aws_sfn")
class StateMachine(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    creation_date: str | core.StringOut = core.attr(str, computed=True)

    definition: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    logging_configuration: LoggingConfiguration | None = core.attr(
        LoggingConfiguration, default=None, computed=True
    )

    name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tracing_configuration: TracingConfiguration | None = core.attr(
        TracingConfiguration, default=None, computed=True
    )

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        definition: str | core.StringOut,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        logging_configuration: LoggingConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tracing_configuration: TracingConfiguration | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StateMachine.Args(
                definition=definition,
                name=name,
                role_arn=role_arn,
                logging_configuration=logging_configuration,
                tags=tags,
                tags_all=tags_all,
                tracing_configuration=tracing_configuration,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        definition: str | core.StringOut = core.arg()

        logging_configuration: LoggingConfiguration | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tracing_configuration: TracingConfiguration | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)
