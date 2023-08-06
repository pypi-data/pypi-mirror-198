import terrascript.core as core


@core.resource(type="aws_appsync_domain_name", namespace="aws_appsync")
class DomainName(core.Resource):

    appsync_domain_name: str | core.StringOut = core.attr(str, computed=True)

    certificate_arn: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    domain_name: str | core.StringOut = core.attr(str)

    hosted_zone_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_arn: str | core.StringOut,
        domain_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainName.Args(
                certificate_arn=certificate_arn,
                domain_name=domain_name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()
