import terrascript.core as core


@core.resource(type="aws_servicecatalog_portfolio_share", namespace="aws_servicecatalog")
class PortfolioShare(core.Resource):

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    accepted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    portfolio_id: str | core.StringOut = core.attr(str)

    principal_id: str | core.StringOut = core.attr(str)

    share_tag_options: bool | core.BoolOut | None = core.attr(bool, default=None)

    type: str | core.StringOut = core.attr(str)

    wait_for_acceptance: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        portfolio_id: str | core.StringOut,
        principal_id: str | core.StringOut,
        type: str | core.StringOut,
        accept_language: str | core.StringOut | None = None,
        share_tag_options: bool | core.BoolOut | None = None,
        wait_for_acceptance: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PortfolioShare.Args(
                portfolio_id=portfolio_id,
                principal_id=principal_id,
                type=type,
                accept_language=accept_language,
                share_tag_options=share_tag_options,
                wait_for_acceptance=wait_for_acceptance,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: str | core.StringOut | None = core.arg(default=None)

        portfolio_id: str | core.StringOut = core.arg()

        principal_id: str | core.StringOut = core.arg()

        share_tag_options: bool | core.BoolOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        wait_for_acceptance: bool | core.BoolOut | None = core.arg(default=None)
