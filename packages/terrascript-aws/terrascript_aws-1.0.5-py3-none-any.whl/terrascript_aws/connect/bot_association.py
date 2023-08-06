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


@core.resource(type="aws_connect_bot_association", namespace="connect")
class BotAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    lex_bot: LexBot = core.attr(LexBot)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: str | core.StringOut,
        lex_bot: LexBot,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BotAssociation.Args(
                instance_id=instance_id,
                lex_bot=lex_bot,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_id: str | core.StringOut = core.arg()

        lex_bot: LexBot = core.arg()
