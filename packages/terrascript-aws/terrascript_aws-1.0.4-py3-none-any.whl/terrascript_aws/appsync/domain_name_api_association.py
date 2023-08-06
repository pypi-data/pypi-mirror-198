import terrascript.core as core


@core.resource(type="aws_appsync_domain_name_api_association", namespace="appsync")
class DomainNameApiAssociation(core.Resource):
    """
    (Required) The API ID.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Required) The Appsync domain name.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    The Appsync domain name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        domain_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainNameApiAssociation.Args(
                api_id=api_id,
                domain_name=domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        domain_name: str | core.StringOut = core.arg()
