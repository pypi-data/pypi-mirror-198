import terrascript.core as core


@core.schema
class LexBot(core.Schema):

    lex_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        lex_region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LexBot.Args(
                name=name,
                lex_region=lex_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lex_region: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()


@core.data(type="aws_connect_bot_association", namespace="connect")
class DsBotAssociation(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    lex_bot: LexBot = core.attr(LexBot)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        lex_bot: LexBot,
    ):
        super().__init__(
            name=data_name,
            args=DsBotAssociation.Args(
                instance_id=instance_id,
                lex_bot=lex_bot,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()

        lex_bot: LexBot = core.arg()
