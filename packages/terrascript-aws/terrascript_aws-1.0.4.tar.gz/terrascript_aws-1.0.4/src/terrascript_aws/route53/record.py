import terrascript.core as core


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


@core.resource(type="aws_route53_record", namespace="route53")
class Record(core.Resource):
    """
    (Optional) An alias block. Conflicts with `ttl` & `records`.
    """

    alias: list[Alias] | core.ArrayOut[Alias] | None = core.attr(
        Alias, default=None, kind=core.Kind.array
    )

    """
    (Optional) Allow creation of this record in Terraform to overwrite an existing record, if any. This
    does not affect the ability to update the record in Terraform and does not prevent other resources w
    ithin Terraform or manual Route 53 changes outside Terraform from overwriting this record. `false` b
    y default. This configuration is not recommended for most environments.
    """
    allow_overwrite: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) A block indicating the routing behavior when associated health check fails. Conflicts wit
    h any other routing policy. [Documented below](#failover-routing-policy).
    """
    failover_routing_policy: list[FailoverRoutingPolicy] | core.ArrayOut[
        FailoverRoutingPolicy
    ] | None = core.attr(FailoverRoutingPolicy, default=None, kind=core.Kind.array)

    """
    [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `n
    ame`.
    """
    fqdn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A block indicating a routing policy based on the geolocation of the requestor. Conflicts
    with any other routing policy. [Documented below](#geolocation-routing-policy).
    """
    geolocation_routing_policy: list[GeolocationRoutingPolicy] | core.ArrayOut[
        GeolocationRoutingPolicy
    ] | None = core.attr(GeolocationRoutingPolicy, default=None, kind=core.Kind.array)

    """
    (Optional) The health check the record should be associated with.
    """
    health_check_id: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A block indicating a routing policy based on the latency between the requestor and an AWS
    region. Conflicts with any other routing policy. [Documented below](#latency-routing-policy).
    """
    latency_routing_policy: list[LatencyRoutingPolicy] | core.ArrayOut[
        LatencyRoutingPolicy
    ] | None = core.attr(LatencyRoutingPolicy, default=None, kind=core.Kind.array)

    """
    (Optional) Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other ro
    uting policy.
    """
    multivalue_answer_routing_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The name of the record.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required for non-alias records) A string list of records. To specify a single record value longer t
    han 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration stri
    ng (e.g., `"first255characters\"\"morecharacters"`).
    """
    records: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Unique identifier to differentiate records with routing policies from one another. Requir
    ed if using `failover`, `geolocation`, `latency`, `multivalue_answer`, or `weighted` routing policie
    s documented below.
    """
    set_identifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required for non-alias records) The TTL of the record.
    """
    ttl: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The record type. Valid values are `A`, `AAAA`, `CAA`, `CNAME`, `DS`, `MX`, `NAPTR`, `NS`,
    PTR`, `SOA`, `SPF`, `SRV` and `TXT`.
    """
    type: str | core.StringOut = core.attr(str)

    """
    (Optional) A block indicating a weighted routing policy. Conflicts with any other routing policy. [D
    ocumented below](#weighted-routing-policy).
    """
    weighted_routing_policy: list[WeightedRoutingPolicy] | core.ArrayOut[
        WeightedRoutingPolicy
    ] | None = core.attr(WeightedRoutingPolicy, default=None, kind=core.Kind.array)

    """
    (Required) The ID of the hosted zone to contain this record.
    """
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
