import terrascript.core as core


@core.resource(type="aws_route53_traffic_policy", namespace="route53")
class TrafficPolicy(core.Resource):
    """
    (Optional) Comment for the traffic policy.
    """

    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Policy document. This is a JSON formatted string. For more information about building Rou
    te53 traffic policy documents, see the [AWS Route53 Traffic Policy document format](https://docs.aws
    .amazon.com/Route53/latest/APIReference/api-policies-traffic-policy-document-format.html)
    """
    document: str | core.StringOut = core.attr(str)

    """
    ID of the traffic policy
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the traffic policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to c
    reate a traffic policy instance.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    """
    Version number of the traffic policy. This value is automatically incremented by AWS after each upda
    te of this resource.
    """
    version: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        document: str | core.StringOut,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrafficPolicy.Args(
                document=document,
                name=name,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        document: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
