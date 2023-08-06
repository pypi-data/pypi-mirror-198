import terrascript.core as core


@core.resource(type="aws_ses_domain_mail_from", namespace="aws_ses")
class DomainMailFrom(core.Resource):

    behavior_on_mx_failure: str | core.StringOut | None = core.attr(str, default=None)

    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
