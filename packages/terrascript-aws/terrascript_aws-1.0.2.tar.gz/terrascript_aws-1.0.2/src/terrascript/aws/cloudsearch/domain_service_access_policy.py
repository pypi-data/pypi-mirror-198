import terrascript.core as core


@core.resource(type="aws_cloudsearch_domain_service_access_policy", namespace="aws_cloudsearch")
class DomainServiceAccessPolicy(core.Resource):

    access_policy: str | core.StringOut = core.attr(str)

    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_policy: str | core.StringOut,
        domain_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainServiceAccessPolicy.Args(
                access_policy=access_policy,
                domain_name=domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policy: str | core.StringOut = core.arg()

        domain_name: str | core.StringOut = core.arg()
