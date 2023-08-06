import terrascript.core as core


@core.resource(type="aws_fms_admin_account", namespace="fms")
class AdminAccount(core.Resource):
    """
    (Optional) The AWS account ID to associate with AWS Firewall Manager as the AWS Firewall Manager adm
    inistrator account. This can be an AWS Organizations master account or a member account. Defaults to
    the current account. Must be configured to perform drift detection.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The AWS account ID of the AWS Firewall Manager administrator account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AdminAccount.Args(
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)
