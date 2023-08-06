import terrascript.core as core


@core.schema
class LogDestinationConfig(core.Schema):

    log_destination: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, kind=core.Kind.map
    )

    log_destination_type: str | core.StringOut = core.attr(str)

    log_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        log_destination: dict[str, str] | core.MapOut[core.StringOut],
        log_destination_type: str | core.StringOut,
        log_type: str | core.StringOut,
    ):
        super().__init__(
            args=LogDestinationConfig.Args(
                log_destination=log_destination,
                log_destination_type=log_destination_type,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_destination: dict[str, str] | core.MapOut[core.StringOut] = core.arg()

        log_destination_type: str | core.StringOut = core.arg()

        log_type: str | core.StringOut = core.arg()


@core.schema
class LoggingConfigurationBlk(core.Schema):

    log_destination_config: list[LogDestinationConfig] | core.ArrayOut[
        LogDestinationConfig
    ] = core.attr(LogDestinationConfig, kind=core.Kind.array)

    def __init__(
        self,
        *,
        log_destination_config: list[LogDestinationConfig] | core.ArrayOut[LogDestinationConfig],
    ):
        super().__init__(
            args=LoggingConfigurationBlk.Args(
                log_destination_config=log_destination_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_destination_config: list[LogDestinationConfig] | core.ArrayOut[
            LogDestinationConfig
        ] = core.arg()


@core.resource(type="aws_networkfirewall_logging_configuration", namespace="networkfirewall")
class LoggingConfiguration(core.Resource):
    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the Network Firewall firewall.
    """

    firewall_arn: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the associated firewall.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A configuration block describing how AWS Network Firewall performs logging for a firewall
    . See [Logging Configuration](#logging-configuration) below for details.
    """
    logging_configuration: LoggingConfigurationBlk = core.attr(LoggingConfigurationBlk)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_arn: str | core.StringOut,
        logging_configuration: LoggingConfigurationBlk,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoggingConfiguration.Args(
                firewall_arn=firewall_arn,
                logging_configuration=logging_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        firewall_arn: str | core.StringOut = core.arg()

        logging_configuration: LoggingConfigurationBlk = core.arg()
