import terrascript.core as core


@core.schema
class Details(core.Schema):

    constraint_id: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    owner: str | core.StringOut = core.attr(str, computed=True)

    portfolio_id: str | core.StringOut = core.attr(str, computed=True)

    product_id: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        constraint_id: str | core.StringOut,
        description: str | core.StringOut,
        owner: str | core.StringOut,
        portfolio_id: str | core.StringOut,
        product_id: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Details.Args(
                constraint_id=constraint_id,
                description=description,
                owner=owner,
                portfolio_id=portfolio_id,
                product_id=product_id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        constraint_id: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()

        owner: str | core.StringOut = core.arg()

        portfolio_id: str | core.StringOut = core.arg()

        product_id: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_servicecatalog_portfolio_constraints", namespace="aws_servicecatalog")
class DsPortfolioConstraints(core.Data):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    details: list[Details] | core.ArrayOut[Details] = core.attr(
        Details, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    portfolio_id: str | core.StringOut = core.attr(str)

    product_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        portfolio_id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        product_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPortfolioConstraints.Args(
                portfolio_id=portfolio_id,
                accept_language=accept_language,
                product_id=product_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        portfolio_id: str | core.StringOut = core.arg()

        product_id: str | core.StringOut | None = core.arg(default=None)
