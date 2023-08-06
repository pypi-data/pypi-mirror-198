import terrascript.core as core


@core.resource(type="aws_servicecatalog_portfolio_share", namespace="servicecatalog")
class PortfolioShare(core.Resource):
    """
    (Optional) Language code. Valid values: `en` (English), `jp` (Japanese), `zh` (Chinese). Default val
    ue is `en`.
    """

    accept_language: str | core.StringOut | None = core.attr(str, default=None)

    """
    Whether the shared portfolio is imported by the recipient account. If the recipient is organizationa
    l, the share is automatically imported, and the field is always set to true.
    """
    accepted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Portfolio identifier.
    """
    portfolio_id: str | core.StringOut = core.attr(str)

    """
    (Required) Identifier of the principal with whom you will share the portfolio. Valid values AWS acco
    unt IDs and ARNs of AWS Organizations and organizational units.
    """
    principal_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to enable sharing of `aws_servicecatalog_tag_option` resources when creating the
    portfolio share.
    """
    share_tag_options: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) Type of portfolio share. Valid values are `ACCOUNT` (an external account), `ORGANIZATION`
    (a share to every account in an organization), `ORGANIZATIONAL_UNIT`, `ORGANIZATION_MEMBER_ACCOUNT`
    (a share to an account in an organization).
    """
    type: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to wait (up to the timeout) for the share to be accepted. Organizational shares a
    re automatically accepted.
    """
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
