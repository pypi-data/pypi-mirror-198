import terrascript.core as core


@core.data(type="aws_servicecatalog_constraint", namespace="aws_servicecatalog")
class DsConstraint(core.Data):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str)

    owner: str | core.StringOut = core.attr(str, computed=True)

    parameters: str | core.StringOut = core.attr(str, computed=True)

    portfolio_id: str | core.StringOut = core.attr(str, computed=True)

    product_id: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

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
