import terrascript.core as core


@core.resource(type="aws_iam_account_alias", namespace="iam")
class AccountAlias(core.Resource):
    """
    (Required) The account alias
    """

    account_alias: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_alias: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccountAlias.Args(
                account_alias=account_alias,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_alias: str | core.StringOut = core.arg()
