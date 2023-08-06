import terrascript.core as core


@core.schema
class LoggingConfig(core.Schema):

    log_group_name: str | core.StringOut = core.attr(str)

    log_role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        log_group_name: str | core.StringOut,
        log_role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=LoggingConfig.Args(
                log_group_name=log_group_name,
                log_role_arn=log_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name: str | core.StringOut = core.arg()

        log_role_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_cloudformation_type", namespace="aws_cloudformation")
class Type(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_version_id: str | core.StringOut = core.attr(str, computed=True)

    deprecated_status: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    documentation_url: str | core.StringOut = core.attr(str, computed=True)

    execution_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    is_default_version: bool | core.BoolOut = core.attr(bool, computed=True)

    logging_config: LoggingConfig | None = core.attr(LoggingConfig, default=None)

    provisioning_type: str | core.StringOut = core.attr(str, computed=True)

    schema: str | core.StringOut = core.attr(str, computed=True)

    schema_handler_package: str | core.StringOut = core.attr(str)

    source_url: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    type_arn: str | core.StringOut = core.attr(str, computed=True)

    type_name: str | core.StringOut = core.attr(str)

    version_id: str | core.StringOut = core.attr(str, computed=True)

    visibility: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        schema_handler_package: str | core.StringOut,
        type_name: str | core.StringOut,
        execution_role_arn: str | core.StringOut | None = None,
        logging_config: LoggingConfig | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Type.Args(
                schema_handler_package=schema_handler_package,
                type_name=type_name,
                execution_role_arn=execution_role_arn,
                logging_config=logging_config,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        execution_role_arn: str | core.StringOut | None = core.arg(default=None)

        logging_config: LoggingConfig | None = core.arg(default=None)

        schema_handler_package: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut = core.arg()
