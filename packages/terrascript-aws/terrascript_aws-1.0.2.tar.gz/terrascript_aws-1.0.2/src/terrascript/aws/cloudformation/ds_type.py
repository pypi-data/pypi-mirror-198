import terrascript.core as core


@core.schema
class LoggingConfig(core.Schema):

    log_group_name: str | core.StringOut = core.attr(str, computed=True)

    log_role_arn: str | core.StringOut = core.attr(str, computed=True)

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


@core.data(type="aws_cloudformation_type", namespace="aws_cloudformation")
class DsType(core.Data):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    default_version_id: str | core.StringOut = core.attr(str, computed=True)

    deprecated_status: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    documentation_url: str | core.StringOut = core.attr(str, computed=True)

    execution_role_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    is_default_version: bool | core.BoolOut = core.attr(bool, computed=True)

    logging_config: list[LoggingConfig] | core.ArrayOut[LoggingConfig] = core.attr(
        LoggingConfig, computed=True, kind=core.Kind.array
    )

    provisioning_type: str | core.StringOut = core.attr(str, computed=True)

    schema: str | core.StringOut = core.attr(str, computed=True)

    source_url: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    type_arn: str | core.StringOut = core.attr(str, computed=True)

    type_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version_id: str | core.StringOut | None = core.attr(str, default=None)

    visibility: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
        type_name: str | core.StringOut | None = None,
        version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsType.Args(
                arn=arn,
                type=type,
                type_name=type_name,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut | None = core.arg(default=None)

        version_id: str | core.StringOut | None = core.arg(default=None)
