import terrascript.core as core


@core.resource(
    type="aws_route53_resolver_query_log_config_association", namespace="route53_resolver"
)
class QueryLogConfigAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the [Route 53 Resolver query logging configuration](route53_resolver_query_log_
    config.html) that you want to associate a VPC with.
    """
    resolver_query_log_config_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of a VPC that you want this query logging configuration to log queries for.
    """
    resource_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resolver_query_log_config_id: str | core.StringOut,
        resource_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueryLogConfigAssociation.Args(
                resolver_query_log_config_id=resolver_query_log_config_id,
                resource_id=resource_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resolver_query_log_config_id: str | core.StringOut = core.arg()

        resource_id: str | core.StringOut = core.arg()
