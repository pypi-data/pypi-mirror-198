import terrascript.core as core


@core.data(type="aws_lex_intent", namespace="aws_lex")
class DsIntent(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    checksum: str | core.StringOut = core.attr(str, computed=True)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    parent_intent_signature: str | core.StringOut = core.attr(str, computed=True)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsIntent.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        version: str | core.StringOut | None = core.arg(default=None)
