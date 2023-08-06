import terrascript.core as core


@core.resource(type="aws_route53_delegation_set", namespace="route53")
class DelegationSet(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Delegation Set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The delegation set ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of authoritative name servers for the hosted zone
    """
    name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) This is a reference name used in Caller Reference
    """
    reference_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        reference_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DelegationSet.Args(
                reference_name=reference_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        reference_name: str | core.StringOut | None = core.arg(default=None)
