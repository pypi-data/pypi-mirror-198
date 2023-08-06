import terrascript.core as core


@core.schema
class Intent(core.Schema):

    intent_name: str | core.StringOut = core.attr(str)

    intent_version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        intent_name: str | core.StringOut,
        intent_version: str | core.StringOut,
    ):
        super().__init__(
            args=Intent.Args(
                intent_name=intent_name,
                intent_version=intent_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intent_name: str | core.StringOut = core.arg()

        intent_version: str | core.StringOut = core.arg()


@core.schema
class Message(core.Schema):

    content: str | core.StringOut = core.attr(str)

    content_type: str | core.StringOut = core.attr(str)

    group_number: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        content: str | core.StringOut,
        content_type: str | core.StringOut,
        group_number: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Message.Args(
                content=content,
                content_type=content_type,
                group_number=group_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: str | core.StringOut = core.arg()

        content_type: str | core.StringOut = core.arg()

        group_number: int | core.IntOut | None = core.arg(default=None)


@core.schema
class AbortStatement(core.Schema):

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AbortStatement.Args(
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ClarificationPrompt(core.Schema):

    max_attempts: int | core.IntOut = core.attr(int)

    message: list[Message] | core.ArrayOut[Message] = core.attr(Message, kind=core.Kind.array)

    response_card: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: int | core.IntOut,
        message: list[Message] | core.ArrayOut[Message],
        response_card: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ClarificationPrompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: int | core.IntOut = core.arg()

        message: list[Message] | core.ArrayOut[Message] = core.arg()

        response_card: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_lex_bot", namespace="aws_lex")
class Bot(core.Resource):

    abort_statement: AbortStatement = core.attr(AbortStatement)

    arn: str | core.StringOut = core.attr(str, computed=True)

    checksum: str | core.StringOut = core.attr(str, computed=True)

    child_directed: bool | core.BoolOut = core.attr(bool)

    clarification_prompt: ClarificationPrompt | None = core.attr(ClarificationPrompt, default=None)

    create_version: bool | core.BoolOut | None = core.attr(bool, default=None)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    detect_sentiment: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_model_improvements: bool | core.BoolOut | None = core.attr(bool, default=None)

    failure_reason: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_session_ttl_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    intent: list[Intent] | core.ArrayOut[Intent] = core.attr(Intent, kind=core.Kind.array)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    locale: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    nlu_intent_confidence_threshold: float | core.FloatOut | None = core.attr(float, default=None)

    process_behavior: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    version: str | core.StringOut = core.attr(str, computed=True)

    voice_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        abort_statement: AbortStatement,
        child_directed: bool | core.BoolOut,
        intent: list[Intent] | core.ArrayOut[Intent],
        name: str | core.StringOut,
        clarification_prompt: ClarificationPrompt | None = None,
        create_version: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        detect_sentiment: bool | core.BoolOut | None = None,
        enable_model_improvements: bool | core.BoolOut | None = None,
        idle_session_ttl_in_seconds: int | core.IntOut | None = None,
        locale: str | core.StringOut | None = None,
        nlu_intent_confidence_threshold: float | core.FloatOut | None = None,
        process_behavior: str | core.StringOut | None = None,
        voice_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Bot.Args(
                abort_statement=abort_statement,
                child_directed=child_directed,
                intent=intent,
                name=name,
                clarification_prompt=clarification_prompt,
                create_version=create_version,
                description=description,
                detect_sentiment=detect_sentiment,
                enable_model_improvements=enable_model_improvements,
                idle_session_ttl_in_seconds=idle_session_ttl_in_seconds,
                locale=locale,
                nlu_intent_confidence_threshold=nlu_intent_confidence_threshold,
                process_behavior=process_behavior,
                voice_id=voice_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        abort_statement: AbortStatement = core.arg()

        child_directed: bool | core.BoolOut = core.arg()

        clarification_prompt: ClarificationPrompt | None = core.arg(default=None)

        create_version: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        detect_sentiment: bool | core.BoolOut | None = core.arg(default=None)

        enable_model_improvements: bool | core.BoolOut | None = core.arg(default=None)

        idle_session_ttl_in_seconds: int | core.IntOut | None = core.arg(default=None)

        intent: list[Intent] | core.ArrayOut[Intent] = core.arg()

        locale: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        nlu_intent_confidence_threshold: float | core.FloatOut | None = core.arg(default=None)

        process_behavior: str | core.StringOut | None = core.arg(default=None)

        voice_id: str | core.StringOut | None = core.arg(default=None)
