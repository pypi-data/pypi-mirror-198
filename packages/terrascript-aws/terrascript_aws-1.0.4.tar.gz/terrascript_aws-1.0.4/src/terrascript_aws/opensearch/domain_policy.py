import terrascript.core as core


@core.resource(type="aws_opensearch_domain_policy", namespace="opensearch")
class DomainPolicy(core.Resource):
    """
    (Optional) IAM policy document specifying the access policies for the domain
    """

    access_policies: str | core.StringOut = core.attr(str)

    """
    (Required) Name of the domain.
    """
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
