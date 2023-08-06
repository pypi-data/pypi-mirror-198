import terrascript.core as core


@core.resource(type="aws_ses_domain_identity", namespace="ses")
class DomainIdentity(core.Resource):
    """
    The ARN of the domain identity.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The domain name to assign to SES
    """
    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A code which when added to the domain as a TXT record
    """
    verification_token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainIdentity.Args(
                domain=domain,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: str | core.StringOut = core.arg()
