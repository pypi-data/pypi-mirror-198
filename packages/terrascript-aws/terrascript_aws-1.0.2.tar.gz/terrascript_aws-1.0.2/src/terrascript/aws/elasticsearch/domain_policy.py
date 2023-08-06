import terrascript.core as core


@core.resource(type="aws_elasticsearch_domain_policy", namespace="aws_elasticsearch")
class DomainPolicy(core.Resource):

    access_policies: str | core.StringOut = core.attr(str)

    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_policies: str | core.StringOut,
        domain_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainPolicy.Args(
                access_policies=access_policies,
                domain_name=domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policies: str | core.StringOut = core.arg()

        domain_name: str | core.StringOut = core.arg()
