import terrascript.core as core


@core.resource(type="aws_cloudsearch_domain_service_access_policy", namespace="cloudsearch")
class DomainServiceAccessPolicy(core.Resource):
    """
    (Required) The access rules you want to configure. These rules replace any existing rules. See the [
    AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.
    html) for details.
    """

    access_policy: str | core.StringOut = core.attr(str)

    """
    (Required) The CloudSearch domain name the policy applies to.
    """
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
