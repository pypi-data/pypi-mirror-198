import terrascript.core as core


@core.schema
class FailoverRoutingPolicy(core.Schema):

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=FailoverRoutingPolicy.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()


@core.schema
class GeolocationRoutingPolicy(core.Schema):

    continent: str | core.StringOut | None = core.attr(str, default=None)

    country: str | core.StringOut | None = core.attr(str, default=None)

    subdivision: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        continent: str | core.StringOut | None = None,
        country: str | core.StringOut | None = None,
        subdivision: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=GeolocationRoutingPolicy.Args(
                continent=continent,
                country=country,
                subdivision=subdivision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        continent: str | core.StringOut | None = core.arg(default=None)

        country: str | core.StringOut | None = core.arg(default=None)

        subdivision: str | core.StringOut | None = core.arg(default=None)


@core.schema
class LatencyRoutingPolicy(core.Schema):

    region: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        region: str | core.StringOut,
    ):
        super().__init__(
            args=LatencyRoutingPolicy.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: str | core.StringOut = core.arg()


@core.schema
class WeightedRoutingPolicy(core.Schema):

    weight: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        weight: int | core.IntOut,
    ):
        super().__init__(
            args=WeightedRoutingPolicy.Args(
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        weight: int | core.IntOut = core.arg()


@core.schema
class Alias(core.Schema):

    evaluate_target_health: bool | core.BoolOut = core.attr(bool)

    name: str | core.StringOut = core.attr(str)

    zone_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        evaluate_target_health: bool | core.BoolOut,
        name: str | core.StringOut,
        zone_id: str | core.StringOut,
    ):
        super().__init__(
            args=Alias.Args(
                evaluate_target_health=evaluate_target_health,
                name=name,
                zone_id=zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        evaluate_target_health: bool | core.BoolOut = core.arg()

        name: str | core.StringOut = core.arg()

        zone_id: str | core.StringOut = core.arg()


@core.resource(type="aws_route53_record", namespace="aws_route53")
class Record(core.Resource):

    alias: list[Alias] | core.ArrayOut[Alias] | None = core.attr(
        Alias, default=None, kind=core.Kind.array
    )

    allow_overwrite: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    failover_routing_policy: list[FailoverRoutingPolicy] | core.ArrayOut[
        FailoverRoutingPolicy
    ] | None = core.attr(FailoverRoutingPolicy, default=None, kind=core.Kind.array)

    fqdn: str | core.StringOut = core.attr(str, computed=True)

    geolocation_routing_policy: list[GeolocationRoutingPolicy] | core.ArrayOut[
        GeolocationRoutingPolicy
    ] | None = core.attr(GeolocationRoutingPolicy, default=None, kind=core.Kind.array)

    health_check_id: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    latency_routing_policy: list[LatencyRoutingPolicy] | core.ArrayOut[
        LatencyRoutingPolicy
    ] | None = core.attr(LatencyRoutingPolicy, default=None, kind=core.Kind.array)

    multivalue_answer_routing_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str)

    records: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    set_identifier: str | core.StringOut | None = core.attr(str, default=None)

    ttl: int | core.IntOut | None = core.attr(int, default=None)

    type: str | core.StringOut = core.attr(str)

    weighted_routing_policy: list[WeightedRoutingPolicy] | core.ArrayOut[
        WeightedRoutingPolicy
    ] | None = core.attr(WeightedRoutingPolicy, default=None, kind=core.Kind.array)

    zone_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        type: str | core.StringOut,
        zone_id: str | core.StringOut,
        alias: list[Alias] | core.ArrayOut[Alias] | None = None,
        allow_overwrite: bool | core.BoolOut | None = None,
        failover_routing_policy: list[FailoverRoutingPolicy]
        | core.ArrayOut[FailoverRoutingPolicy]
        | None = None,
        geolocation_routing_policy: list[GeolocationRoutingPolicy]
        | core.ArrayOut[GeolocationRoutingPolicy]
        | None = None,
        health_check_id: str | core.StringOut | None = None,
        latency_routing_policy: list[LatencyRoutingPolicy]
        | core.ArrayOut[LatencyRoutingPolicy]
        | None = None,
        multivalue_answer_routing_policy: bool | core.BoolOut | None = None,
        records: list[str] | core.ArrayOut[core.StringOut] | None = None,
        set_identifier: str | core.StringOut | None = None,
        ttl: int | core.IntOut | None = None,
        weighted_routing_policy: list[WeightedRoutingPolicy]
        | core.ArrayOut[WeightedRoutingPolicy]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Record.Args(
                name=name,
                type=type,
                zone_id=zone_id,
                alias=alias,
                allow_overwrite=allow_overwrite,
                failover_routing_policy=failover_routing_policy,
                geolocation_routing_policy=geolocation_routing_policy,
                health_check_id=health_check_id,
                latency_routing_policy=latency_routing_policy,
                multivalue_answer_routing_policy=multivalue_answer_routing_policy,
                records=records,
                set_identifier=set_identifier,
                ttl=ttl,
                weighted_routing_policy=weighted_routing_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: list[Alias] | core.ArrayOut[Alias] | None = core.arg(default=None)

        allow_overwrite: bool | core.BoolOut | None = core.arg(default=None)

        failover_routing_policy: list[FailoverRoutingPolicy] | core.ArrayOut[
            FailoverRoutingPolicy
        ] | None = core.arg(default=None)

        geolocation_routing_policy: list[GeolocationRoutingPolicy] | core.ArrayOut[
            GeolocationRoutingPolicy
        ] | None = core.arg(default=None)

        health_check_id: str | core.StringOut | None = core.arg(default=None)

        latency_routing_policy: list[LatencyRoutingPolicy] | core.ArrayOut[
            LatencyRoutingPolicy
        ] | None = core.arg(default=None)

        multivalue_answer_routing_policy: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        records: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        set_identifier: str | core.StringOut | None = core.arg(default=None)

        ttl: int | core.IntOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        weighted_routing_policy: list[WeightedRoutingPolicy] | core.ArrayOut[
            WeightedRoutingPolicy
        ] | None = core.arg(default=None)

        zone_id: str | core.StringOut = core.arg()
