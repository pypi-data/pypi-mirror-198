import terrascript.core as core


@core.data(type="aws_servicecatalog_constraint", namespace="servicecatalog")
class DsConstraint(core.Data):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    Description of the constraint.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Constraint identifier.
    """
    id: str | core.StringOut = core.attr(str)

    """
    Owner of the constraint.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    Constraint parameters in JSON format.
    """
    parameters: str | core.StringOut = core.attr(str, computed=True)

    """
    Portfolio identifier.
    """
    portfolio_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Product identifier.
    """
    product_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Constraint status.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    Type of constraint. Valid values are `LAUNCH`, `NOTIFICATION`, `RESOURCE_UPDATE`, `STACKSET`, and `T
    EMPLATE`.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConstraint.Args(
                id=id,
                accept_language=accept_language,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()
