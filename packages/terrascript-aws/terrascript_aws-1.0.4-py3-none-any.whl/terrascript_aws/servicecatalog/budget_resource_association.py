import terrascript.core as core


@core.resource(type="aws_servicecatalog_budget_resource_association", namespace="servicecatalog")
class BudgetResourceAssociation(core.Resource):
    """
    (Required) Budget name.
    """

    budget_name: str | core.StringOut = core.attr(str)

    """
    Identifier of the association.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Resource identifier.
    """
    resource_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        budget_name: str | core.StringOut,
        resource_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BudgetResourceAssociation.Args(
                budget_name=budget_name,
                resource_id=resource_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        budget_name: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()
