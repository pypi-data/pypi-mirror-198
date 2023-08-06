import terrascript.core as core


@core.schema
class LogSettings(core.Schema):

    destination: str | core.StringOut = core.attr(str)

    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    log_type: str | core.StringOut = core.attr(str)

    resource_arn: str | core.StringOut = core.attr(str)

    resource_prefix: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination: str | core.StringOut,
        log_type: str | core.StringOut,
        resource_arn: str | core.StringOut,
        resource_prefix: str | core.StringOut,
        kms_key_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LogSettings.Args(
                destination=destination,
                log_type=log_type,
                resource_arn=resource_arn,
                resource_prefix=resource_prefix,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: str | core.StringOut = core.arg()

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        log_type: str | core.StringOut = core.arg()

        resource_arn: str | core.StringOut = core.arg()

        resource_prefix: str | core.StringOut = core.arg()


@core.schema
class ConversationLogs(core.Schema):

    iam_role_arn: str | core.StringOut = core.attr(str)

    log_settings: list[LogSettings] | core.ArrayOut[LogSettings] | None = core.attr(
        LogSettings, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        iam_role_arn: str | core.StringOut,
        log_settings: list[LogSettings] | core.ArrayOut[LogSettings] | None = None,
    ):
        super().__init__(
            args=ConversationLogs.Args(
                iam_role_arn=iam_role_arn,
                log_settings=log_settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam_role_arn: str | core.StringOut = core.arg()

        log_settings: list[LogSettings] | core.ArrayOut[LogSettings] | None = core.arg(default=None)


@core.resource(type="aws_lex_bot_alias", namespace="aws_lex")
class BotAlias(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bot_name: str | core.StringOut = core.attr(str)

    bot_version: str | core.StringOut = core.attr(str)

    checksum: str | core.StringOut = core.attr(str, computed=True)

    conversation_logs: ConversationLogs | None = core.attr(ConversationLogs, default=None)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bot_name: str | core.StringOut,
        bot_version: str | core.StringOut,
        name: str | core.StringOut,
        conversation_logs: ConversationLogs | None = None,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BotAlias.Args(
                bot_name=bot_name,
                bot_version=bot_version,
                name=name,
                conversation_logs=conversation_logs,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bot_name: str | core.StringOut = core.arg()

        bot_version: str | core.StringOut = core.arg()

        conversation_logs: ConversationLogs | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
