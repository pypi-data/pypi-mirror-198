import terrascript.core as core


@core.data(type="aws_lex_bot_alias", namespace="lex")
class DsBotAlias(core.Data):
    """
    The ARN of the bot alias.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the bot.
    """
    bot_name: str | core.StringOut = core.attr(str)

    """
    The version of the bot that the alias points to.
    """
    bot_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Checksum of the bot alias.
    """
    checksum: str | core.StringOut = core.attr(str, computed=True)

    """
    The date that the bot alias was created.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    A description of the alias.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The date that the bot alias was updated. When you create a resource, the creation date and the last
    updated date are the same.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the bot alias. The name is case sensitive.
    """
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
