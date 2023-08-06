import terrascript.core as core


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


@core.resource(type="aws_lex_bot", namespace="lex")
class Bot(core.Resource):
    """
    (Required) The message that Amazon Lex uses to abort a conversation. Attributes are documented under
    [statement](#statement).
    """

    abort_statement: AbortStatement = core.attr(AbortStatement)

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Checksum identifying the version of the bot that was created. The checksum is not
    """
    checksum: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) By specifying true, you confirm that your use of Amazon Lex is related to a website, prog
    ram, or other application that is directed or targeted, in whole or in part, to children under age 1
    3 and subject to COPPA. For more information see the [Amazon Lex FAQ](https://aws.amazon.com/lex/faq
    s#data-security) and the [Amazon Lex PutBot API Docs](https://docs.aws.amazon.com/lex/latest/dg/API_
    PutBot.html#lex-PutBot-request-childDirected).
    """
    child_directed: bool | core.BoolOut = core.attr(bool)

    """
    (Required) The message that Amazon Lex uses when it doesn't understand the user's request. Attribute
    s are documented under [prompt](#prompt).
    """
    clarification_prompt: ClarificationPrompt | None = core.attr(ClarificationPrompt, default=None)

    """
    (Optional) Determines if a new bot version is created when the initial resource is created and on ea
    ch update. Defaults to `false`.
    """
    create_version: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The date when the bot version was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the bot. Must be less than or equal to 200 characters in length.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) When set to true user utterances are sent to Amazon Comprehend for sentiment analysis. If
    you don't specify detectSentiment, the default is `false`.
    """
    detect_sentiment: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Set to `true` to enable access to natural language understanding improvements. When you s
    et the `enable_model_improvements` parameter to true you can use the `nlu_intent_confidence_threshol
    d` parameter to configure confidence scores. For more information, see [Confidence Scores](https://d
    ocs.aws.amazon.com/lex/latest/dg/confidence-scores.html). You can only set the `enable_model_improve
    ments` parameter in certain Regions. If you set the parameter to true, your bot has access to accura
    cy improvements. For more information see the [Amazon Lex Bot PutBot API Docs](https://docs.aws.amaz
    on.com/lex/latest/dg/API_PutBot.html#lex-PutBot-request-enableModelImprovements).
    """
    enable_model_improvements: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    If status is FAILED, Amazon Lex provides the reason that it failed to build the bot.
    """
    failure_reason: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.
    Default is `300`. Must be a number between 60 and 86400 (inclusive).
    """
    idle_session_ttl_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) A set of Intent objects. Each intent represents a command that a user can express. Attrib
    utes are documented under [intent](#intent). Can have up to 250 Intent objects.
    """
    intent: list[Intent] | core.ArrayOut[Intent] = core.attr(Intent, kind=core.Kind.array)

    """
    The date when the $LATEST version of this bot was updated.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the target locale for the bot. Any intent used in the bot must be compatible wi
    th the locale of the bot. For available locales, see [Amazon Lex Bot PutBot API Docs](https://docs.a
    ws.amazon.com/lex/latest/dg/API_PutBot.html#lex-PutBot-request-locale). Default is `en-US`.
    """
    locale: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the bot that you want to create, case sensitive. Must be between 2 and 50 cha
    racters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Determines the threshold where Amazon Lex will insert the AMAZON.FallbackIntent, AMAZON.K
    endraSearchIntent, or both when returning alternative intents in a PostContent or PostText response.
    AMAZON.FallbackIntent and AMAZON.KendraSearchIntent are only inserted if they are configured for th
    e bot. For more information see [Amazon Lex Bot PutBot API Docs](https://docs.aws.amazon.com/lex/lat
    est/dg/API_PutBot.html#lex-PutBot-request-nluIntentConfidenceThreshold) This value requires `enable_
    model_improvements` to be set to `true` and the default is `0`. Must be a float between 0 and 1.
    """
    nlu_intent_confidence_threshold: float | core.FloatOut | None = core.attr(float, default=None)

    """
    (Optional) If you set the `process_behavior` element to `BUILD`, Amazon Lex builds the bot so that i
    t can be run. If you set the element to `SAVE` Amazon Lex saves the bot, but doesn't build it. Defau
    lt is `SAVE`.
    """
    process_behavior: str | core.StringOut | None = core.attr(str, default=None)

    """
    When you send a request to create or update a bot, Amazon Lex sets the status response
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    The version of the bot.
    """
    version: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the
    user. The locale configured for the voice must match the locale of the bot. For more information, s
    ee [Available Voices](http://docs.aws.amazon.com/polly/latest/dg/voicelist.html) in the Amazon Polly
    Developer Guide.
    """
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
