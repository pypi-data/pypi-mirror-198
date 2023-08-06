import terrascript.core as core


@core.resource(type="aws_macie2_account", namespace="macie2")
class Account(core.Resource):
    """
    The date and time, in UTC and extended RFC 3339 format, when the Amazon Macie account was created.
    """

    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies how often to publish updates to policy findings for the account. This includes
    publishing updates to AWS Security Hub and Amazon EventBridge (formerly called Amazon CloudWatch Ev
    ents). Valid values are `FIFTEEN_MINUTES`, `ONE_HOUR` or `SIX_HOURS`.
    """
    finding_publishing_frequency: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The unique identifier (ID) of the macie account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the service-linked role that allows Macie to monitor and analyze d
    ata in AWS resources for the account.
    """
    service_role: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the status for the account. To enable Amazon Macie and start all Macie activiti
    es for the account, set this value to `ENABLED`. Valid values are `ENABLED` or `PAUSED`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The date and time, in UTC and extended RFC 3339 format, of the most recent change to the status of t
    he Macie account.
    """
    updated_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        finding_publishing_frequency: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                finding_publishing_frequency=finding_publishing_frequency,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        finding_publishing_frequency: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)
