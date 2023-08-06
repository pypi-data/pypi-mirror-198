import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_principal_portfolio_association", namespace="aws_servicecatalog"
)
class PrincipalPortfolioAssociation(core.Resource):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    portfolio_id: str | core.StringOut = core.attr(str)

    principal_arn: str | core.StringOut = core.attr(str)

    principal_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        portfolio_id: str | core.StringOut,
        principal_arn: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        principal_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PrincipalPortfolioAssociation.Args(
                portfolio_id=portfolio_id,
                principal_arn=principal_arn,
                accept_language=accept_language,
                principal_type=principal_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        portfolio_id: str | core.StringOut = core.arg()

        principal_arn: str | core.StringOut = core.arg()

        principal_type: str | core.StringOut | None = core.arg(default=None)
