import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_principal_portfolio_association", namespace="servicecatalog"
)
class PrincipalPortfolioAssociation(core.Resource):
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
    (Required) Principal ARN.
    """
    principal_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Principal type. Setting this argument empty (e.g., `principal_type = ""`) will result in
    an error. Valid value is `IAM`. Default is `IAM`.
    """
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
