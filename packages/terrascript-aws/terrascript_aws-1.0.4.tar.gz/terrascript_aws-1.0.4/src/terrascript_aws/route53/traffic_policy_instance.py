import terrascript.core as core


@core.resource(type="aws_route53_traffic_policy_instance", namespace="route53")
class TrafficPolicyInstance(core.Resource):
    """
    (Required) ID of the hosted zone that you want Amazon Route 53 to create resource record sets in by
    using the configuration in a traffic policy.
    """

    hosted_zone_id: str | core.StringOut = core.attr(str)

    """
    ID of traffic policy instance.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Domain name for which Amazon Route 53 responds to DNS queries by using the resource recor
    d sets that Route 53 creates for this traffic policy instance.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) ID of the traffic policy that you want to use to create resource record sets in the speci
    fied hosted zone.
    """
    traffic_policy_id: str | core.StringOut = core.attr(str)

    """
    (Required) Version of the traffic policy
    """
    traffic_policy_version: int | core.IntOut = core.attr(int)

    """
    (Required) TTL that you want Amazon Route 53 to assign to all the resource record sets that it creat
    es in the specified hosted zone.
    """
    ttl: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        hosted_zone_id: str | core.StringOut,
        name: str | core.StringOut,
        traffic_policy_id: str | core.StringOut,
        traffic_policy_version: int | core.IntOut,
        ttl: int | core.IntOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrafficPolicyInstance.Args(
                hosted_zone_id=hosted_zone_id,
                name=name,
                traffic_policy_id=traffic_policy_id,
                traffic_policy_version=traffic_policy_version,
                ttl=ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hosted_zone_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        traffic_policy_id: str | core.StringOut = core.arg()

        traffic_policy_version: int | core.IntOut = core.arg()

        ttl: int | core.IntOut = core.arg()
