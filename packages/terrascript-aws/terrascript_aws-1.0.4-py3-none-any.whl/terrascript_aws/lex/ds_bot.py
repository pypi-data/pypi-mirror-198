import terrascript.core as core


@core.data(type="aws_lex_bot", namespace="lex")
class DsBot(core.Data):
    """
    The ARN of the bot.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Checksum of the bot used to identify a specific revision of the bot's `$LATEST` version.
    """
    checksum: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies if this Amazon Lex Bot is related to a website, program, or other application that is dire
    cted or targeted, in whole or in part, to children under age 13 and subject to COPPA.
    """
    child_directed: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The date that the bot was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    A description of the bot.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    When set to true user utterances are sent to Amazon Comprehend for sentiment analysis.
    """
    detect_sentiment: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Set to true if natural language understanding improvements are enabled.
    """
    enable_model_improvements: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    If the `status` is `FAILED`, the reason why the bot failed to build.
    """
    failure_reason: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.
    """
    idle_session_ttl_in_seconds: int | core.IntOut = core.attr(int, computed=True)

    """
    The date that the bot was updated.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Specifies the target locale for the bot. Any intent used in the bot must be compatible with the loca
    le of the bot.
    """
    locale: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the bot. The name is case sensitive.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The threshold where Amazon Lex will insert the AMAZON.FallbackIntent, AMAZON.KendraSearchIntent, or
    both when returning alternative intents in a PostContent or PostText response. AMAZON.FallbackIntent
    and AMAZON.KendraSearchIntent are only inserted if they are configured for the bot.
    """
    nlu_intent_confidence_threshold: float | core.FloatOut = core.attr(float, computed=True)

    """
    The status of the bot.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The version or alias of the bot.
    """
    version: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Polly voice ID that the Amazon Lex Bot uses for voice interactions with the user.
    """
    voice_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBot.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        version: str | core.StringOut | None = core.arg(default=None)
