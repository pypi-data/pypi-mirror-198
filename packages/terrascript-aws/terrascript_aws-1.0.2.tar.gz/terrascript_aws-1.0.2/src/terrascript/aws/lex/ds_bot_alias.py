import terrascript.core as core


@core.data(type="aws_lex_bot_alias", namespace="aws_lex")
class DsBotAlias(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bot_name: str | core.StringOut = core.attr(str)

    bot_version: str | core.StringOut = core.attr(str, computed=True)

    checksum: str | core.StringOut = core.attr(str, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        bot_name: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsBotAlias.Args(
                bot_name=bot_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bot_name: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
