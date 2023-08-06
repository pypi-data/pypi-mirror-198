import terrascript.core as core


@core.data(type="aws_lex_bot", namespace="aws_lex")
class DsBot(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    checksum: str | core.StringOut = core.attr(str, computed=True)

    child_directed: bool | core.BoolOut = core.attr(bool, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    detect_sentiment: bool | core.BoolOut = core.attr(bool, computed=True)

    enable_model_improvements: bool | core.BoolOut = core.attr(bool, computed=True)

    failure_reason: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_session_ttl_in_seconds: int | core.IntOut = core.attr(int, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    locale: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    nlu_intent_confidence_threshold: float | core.FloatOut = core.attr(float, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    version: str | core.StringOut | None = core.attr(str, default=None)

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
