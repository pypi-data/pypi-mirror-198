import terrascript.core as core


@core.data(type="aws_iam_account_alias", namespace="iam")
class DsAccountAlias(core.Data):
    """
    The alias associated with the AWS account.
    """

    account_alias: str | core.StringOut = core.attr(str, computed=True)

    """
    The alias associated with the AWS account.
    """
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
