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


@core.resource(type="aws_sfn_state_machine", namespace="sfn")
class StateMachine(core.Resource):
    """
    The ARN of the state machine.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date the state machine was created.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concept
    s-amazon-states-language.html) definition of the state machine.
    """
    definition: str | core.StringOut = core.attr(str)

    """
    The ARN of the state machine.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Defines what execution history events are logged and where they are logged. The `logging_
    configuration` parameter is only valid when `type` is set to `EXPRESS`. Defaults to `OFF`. For more
    information see [Logging Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/cw-
    logs.html) and [Log Levels](https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-leve
    l.html) in the AWS Step Functions User Guide.
    """
    logging_configuration: LoggingConfiguration | None = core.attr(
        LoggingConfiguration, default=None, computed=True
    )

    """
    (Required) The name of the state machine. To enable logging with CloudWatch Logs, the name should on
    ly contain `0`-`9`, `A`-`Z`, `a`-`z`, `-` and `_`.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    The current status of the state machine. Either `ACTIVE` or `DELETING`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Selects whether AWS X-Ray tracing is enabled.
    """
    tracing_configuration: TracingConfiguration | None = core.attr(
        TracingConfiguration, default=None, computed=True
    )

    """
    (Optional) Determines whether a Standard or Express state machine is created. The default is `STANDA
    RD`. You cannot update the type of a state machine once it has been created. Valid values: `STANDARD
    , `EXPRESS`.
    """
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
