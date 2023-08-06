import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_product_portfolio_association", namespace="aws_servicecatalog"
)
class ProductPortfolioAssociation(core.Resource):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    portfolio_id: str | core.StringOut = core.attr(str)

    product_id: str | core.StringOut = core.attr(str)

    source_portfolio_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        portfolio_id: str | core.StringOut,
        product_id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        source_portfolio_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProductPortfolioAssociation.Args(
                portfolio_id=portfolio_id,
                product_id=product_id,
                accept_language=accept_language,
                source_portfolio_id=source_portfolio_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        portfolio_id: str | core.StringOut = core.arg()

        product_id: str | core.StringOut = core.arg()

        source_portfolio_id: str | core.StringOut | None = core.arg(default=None)
