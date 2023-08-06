import terrascript.core as core


@core.data(type="aws_iam_account_alias", namespace="aws_iam")
class DsAccountAlias(core.Data):

    account_alias: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsAccountAlias.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
