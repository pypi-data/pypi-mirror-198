import terrascript.core as core


@core.data(type="aws_servicecatalog_portfolio", namespace="servicecatalog")
class DsPortfolio(core.Data):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    Portfolio ARN.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Time the portfolio was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the portfolio
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Portfolio identifier.
    """
    id: str | core.StringOut = core.attr(str)

    """
    Portfolio name.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    Name of the person or organization who owns the portfolio.
    """
    provider_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Tags applied to the portfolio.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPortfolio.Args(
                id=id,
                accept_language=accept_language,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
