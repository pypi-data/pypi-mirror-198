import terrascript.core as core


@core.schema
class DefaultAction(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=DefaultAction.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class FieldToMatch(core.Schema):

    data: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                type=type,
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class RedactedFields(core.Schema):

    field_to_match: list[FieldToMatch] | core.ArrayOut[FieldToMatch] = core.attr(
        FieldToMatch, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field_to_match: list[FieldToMatch] | core.ArrayOut[FieldToMatch],
    ):
        super().__init__(
            args=RedactedFields.Args(
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: list[FieldToMatch] | core.ArrayOut[FieldToMatch] = core.arg()


@core.schema
class LoggingConfiguration(core.Schema):

    log_destination: str | core.StringOut = core.attr(str)

    redacted_fields: RedactedFields | None = core.attr(RedactedFields, default=None)

    def __init__(
        self,
        *,
        log_destination: str | core.StringOut,
        redacted_fields: RedactedFields | None = None,
    ):
        super().__init__(
            args=LoggingConfiguration.Args(
                log_destination=log_destination,
                redacted_fields=redacted_fields,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_destination: str | core.StringOut = core.arg()

        redacted_fields: RedactedFields | None = core.arg(default=None)


@core.schema
class OverrideAction(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=OverrideAction.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class Action(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Action.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class Rules(core.Schema):

    action: Action | None = core.attr(Action, default=None)

    override_action: OverrideAction | None = core.attr(OverrideAction, default=None)

    priority: int | core.IntOut = core.attr(int)

    rule_id: str | core.StringOut = core.attr(str)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        priority: int | core.IntOut,
        rule_id: str | core.StringOut,
        action: Action | None = None,
        override_action: OverrideAction | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Rules.Args(
                priority=priority,
                rule_id=rule_id,
                action=action,
                override_action=override_action,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action | None = core.arg(default=None)

        override_action: OverrideAction | None = core.arg(default=None)

        priority: int | core.IntOut = core.arg()

        rule_id: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_waf_web_acl", namespace="waf")
class WebAcl(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    default_action: DefaultAction = core.attr(DefaultAction)

    id: str | core.StringOut = core.attr(str, computed=True)

    logging_configuration: LoggingConfiguration | None = core.attr(
        LoggingConfiguration, default=None
    )

    metric_name: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    rules: list[Rules] | core.ArrayOut[Rules] | None = core.attr(
        Rules, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        default_action: DefaultAction,
        metric_name: str | core.StringOut,
        name: str | core.StringOut,
        logging_configuration: LoggingConfiguration | None = None,
        rules: list[Rules] | core.ArrayOut[Rules] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=WebAcl.Args(
                default_action=default_action,
                metric_name=metric_name,
                name=name,
                logging_configuration=logging_configuration,
                rules=rules,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_action: DefaultAction = core.arg()

        logging_configuration: LoggingConfiguration | None = core.arg(default=None)

        metric_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        rules: list[Rules] | core.ArrayOut[Rules] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
