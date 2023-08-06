import terrascript.core as core


@core.resource(type="aws_servicecatalog_product_portfolio_association", namespace="servicecatalog")
class ProductPortfolioAssociation(core.Resource):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    Identifier of the association.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Portfolio identifier.
    """
    portfolio_id: str | core.StringOut = core.attr(str)

    """
    (Required) Product identifier.
    """
    product_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Identifier of the source portfolio.
    """
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
