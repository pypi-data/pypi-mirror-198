import terrascript.core as core


@core.resource(type="aws_ses_domain_dkim", namespace="ses")
class DomainDkim(core.Resource):

    dkim_tokens: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
            args=DomainDkim.Args(
                domain=domain,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: str | core.StringOut = core.arg()
