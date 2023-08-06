import terrascript.core as core


@core.resource(type="aws_route53_resolver_rule_association", namespace="route53_resolver")
class RuleAssociation(core.Resource):
    """
    The ID of the resolver rule association.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A name for the association that you're creating between a resolver rule and a VPC.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the resolver rule that you want to associate with the VPC.
    """
    resolver_rule_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the VPC that you want to associate the resolver rule with.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resolver_rule_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RuleAssociation.Args(
                resolver_rule_id=resolver_rule_id,
                vpc_id=vpc_id,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        resolver_rule_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()
