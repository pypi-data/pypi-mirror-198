import terrascript.core as core


@core.resource(type="aws_servicecatalog_constraint", namespace="aws_servicecatalog")
class Constraint(core.Resource):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner: str | core.StringOut = core.attr(str, computed=True)

    parameters: str | core.StringOut = core.attr(str)

    portfolio_id: str | core.StringOut = core.attr(str)

    product_id: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        parameters: str | core.StringOut,
        portfolio_id: str | core.StringOut,
        product_id: str | core.StringOut,
        type: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Constraint.Args(
                parameters=parameters,
                portfolio_id=portfolio_id,
                product_id=product_id,
                type=type,
                accept_language=accept_language,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        parameters: str | core.StringOut = core.arg()

        portfolio_id: str | core.StringOut = core.arg()

        product_id: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()
