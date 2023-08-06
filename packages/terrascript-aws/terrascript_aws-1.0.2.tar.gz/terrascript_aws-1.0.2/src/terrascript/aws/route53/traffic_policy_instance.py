import terrascript.core as core


@core.resource(type="aws_route53_traffic_policy_instance", namespace="aws_route53")
class TrafficPolicyInstance(core.Resource):

    hosted_zone_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    traffic_policy_id: str | core.StringOut = core.attr(str)

    traffic_policy_version: int | core.IntOut = core.attr(int)

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
