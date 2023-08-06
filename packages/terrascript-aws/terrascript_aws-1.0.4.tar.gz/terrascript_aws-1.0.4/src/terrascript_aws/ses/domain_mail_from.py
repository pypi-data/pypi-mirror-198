import terrascript.core as core


@core.resource(type="aws_ses_domain_mail_from", namespace="ses")
class DomainMailFrom(core.Resource):
    """
    (Optional) The action that you want Amazon SES to take if it cannot successfully read the required M
    X record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](http
    s://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more informa
    tion.
    """

    behavior_on_mx_failure: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Verified domain name or email identity to generate DKIM tokens for.
    """
    domain: str | core.StringOut = core.attr(str)

    """
    The domain name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC
    validation)
    """
    mail_from_domain: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        mail_from_domain: str | core.StringOut,
        behavior_on_mx_failure: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainMailFrom.Args(
                domain=domain,
                mail_from_domain=mail_from_domain,
                behavior_on_mx_failure=behavior_on_mx_failure,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        behavior_on_mx_failure: str | core.StringOut | None = core.arg(default=None)

        domain: str | core.StringOut = core.arg()

        mail_from_domain: str | core.StringOut = core.arg()
