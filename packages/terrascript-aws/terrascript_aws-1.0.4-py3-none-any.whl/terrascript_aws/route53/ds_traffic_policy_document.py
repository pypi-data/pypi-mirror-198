import terrascript.core as core


@core.schema
class Endpoint(core.Schema):

    id: str | core.StringOut = core.attr(str)

    region: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        region: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Endpoint.Args(
                id=id,
                region=region,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        region: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Location(core.Schema):

    continent: str | core.StringOut | None = core.attr(str, default=None)

    country: str | core.StringOut | None = core.attr(str, default=None)

    endpoint_reference: str | core.StringOut | None = core.attr(str, default=None)

    evaluate_target_health: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check: str | core.StringOut | None = core.attr(str, default=None)

    is_default: bool | core.BoolOut | None = core.attr(bool, default=None)

    rule_reference: str | core.StringOut | None = core.attr(str, default=None)

    subdivision: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        continent: str | core.StringOut | None = None,
        country: str | core.StringOut | None = None,
        endpoint_reference: str | core.StringOut | None = None,
        evaluate_target_health: bool | core.BoolOut | None = None,
        health_check: str | core.StringOut | None = None,
        is_default: bool | core.BoolOut | None = None,
        rule_reference: str | core.StringOut | None = None,
        subdivision: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Location.Args(
                continent=continent,
                country=country,
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                is_default=is_default,
                rule_reference=rule_reference,
                subdivision=subdivision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        continent: str | core.StringOut | None = core.arg(default=None)

        country: str | core.StringOut | None = core.arg(default=None)

        endpoint_reference: str | core.StringOut | None = core.arg(default=None)

        evaluate_target_health: bool | core.BoolOut | None = core.arg(default=None)

        health_check: str | core.StringOut | None = core.arg(default=None)

        is_default: bool | core.BoolOut | None = core.arg(default=None)

        rule_reference: str | core.StringOut | None = core.arg(default=None)

        subdivision: str | core.StringOut | None = core.arg(default=None)


@core.schema
class GeoProximityLocation(core.Schema):

    bias: str | core.StringOut | None = core.attr(str, default=None)

    endpoint_reference: str | core.StringOut | None = core.attr(str, default=None)

    evaluate_target_health: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check: str | core.StringOut | None = core.attr(str, default=None)

    latitude: str | core.StringOut | None = core.attr(str, default=None)

    longitude: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None)

    rule_reference: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bias: str | core.StringOut | None = None,
        endpoint_reference: str | core.StringOut | None = None,
        evaluate_target_health: bool | core.BoolOut | None = None,
        health_check: str | core.StringOut | None = None,
        latitude: str | core.StringOut | None = None,
        longitude: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        rule_reference: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=GeoProximityLocation.Args(
                bias=bias,
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                latitude=latitude,
                longitude=longitude,
                region=region,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bias: str | core.StringOut | None = core.arg(default=None)

        endpoint_reference: str | core.StringOut | None = core.arg(default=None)

        evaluate_target_health: bool | core.BoolOut | None = core.arg(default=None)

        health_check: str | core.StringOut | None = core.arg(default=None)

        latitude: str | core.StringOut | None = core.arg(default=None)

        longitude: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        rule_reference: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Region(core.Schema):

    endpoint_reference: str | core.StringOut | None = core.attr(str, default=None)

    evaluate_target_health: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None)

    rule_reference: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: str | core.StringOut | None = None,
        evaluate_target_health: bool | core.BoolOut | None = None,
        health_check: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        rule_reference: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Region.Args(
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                region=region,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: str | core.StringOut | None = core.arg(default=None)

        evaluate_target_health: bool | core.BoolOut | None = core.arg(default=None)

        health_check: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        rule_reference: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Items(core.Schema):

    endpoint_reference: str | core.StringOut | None = core.attr(str, default=None)

    health_check: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: str | core.StringOut | None = None,
        health_check: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Items.Args(
                endpoint_reference=endpoint_reference,
                health_check=health_check,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: str | core.StringOut | None = core.arg(default=None)

        health_check: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Primary(core.Schema):

    endpoint_reference: str | core.StringOut | None = core.attr(str, default=None)

    evaluate_target_health: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check: str | core.StringOut | None = core.attr(str, default=None)

    rule_reference: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: str | core.StringOut | None = None,
        evaluate_target_health: bool | core.BoolOut | None = None,
        health_check: str | core.StringOut | None = None,
        rule_reference: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Primary.Args(
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: str | core.StringOut | None = core.arg(default=None)

        evaluate_target_health: bool | core.BoolOut | None = core.arg(default=None)

        health_check: str | core.StringOut | None = core.arg(default=None)

        rule_reference: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Secondary(core.Schema):

    endpoint_reference: str | core.StringOut | None = core.attr(str, default=None)

    evaluate_target_health: bool | core.BoolOut | None = core.attr(bool, default=None)

    health_check: str | core.StringOut | None = core.attr(str, default=None)

    rule_reference: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: str | core.StringOut | None = None,
        evaluate_target_health: bool | core.BoolOut | None = None,
        health_check: str | core.StringOut | None = None,
        rule_reference: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Secondary.Args(
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: str | core.StringOut | None = core.arg(default=None)

        evaluate_target_health: bool | core.BoolOut | None = core.arg(default=None)

        health_check: str | core.StringOut | None = core.arg(default=None)

        rule_reference: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    geo_proximity_location: list[GeoProximityLocation] | core.ArrayOut[
        GeoProximityLocation
    ] | None = core.attr(GeoProximityLocation, default=None, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str)

    items: list[Items] | core.ArrayOut[Items] | None = core.attr(
        Items, default=None, kind=core.Kind.array
    )

    location: list[Location] | core.ArrayOut[Location] | None = core.attr(
        Location, default=None, kind=core.Kind.array
    )

    primary: Primary | None = core.attr(Primary, default=None)

    region: list[Region] | core.ArrayOut[Region] | None = core.attr(
        Region, default=None, kind=core.Kind.array
    )

    secondary: Secondary | None = core.attr(Secondary, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        geo_proximity_location: list[GeoProximityLocation]
        | core.ArrayOut[GeoProximityLocation]
        | None = None,
        items: list[Items] | core.ArrayOut[Items] | None = None,
        location: list[Location] | core.ArrayOut[Location] | None = None,
        primary: Primary | None = None,
        region: list[Region] | core.ArrayOut[Region] | None = None,
        secondary: Secondary | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Rule.Args(
                id=id,
                geo_proximity_location=geo_proximity_location,
                items=items,
                location=location,
                primary=primary,
                region=region,
                secondary=secondary,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        geo_proximity_location: list[GeoProximityLocation] | core.ArrayOut[
            GeoProximityLocation
        ] | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()

        items: list[Items] | core.ArrayOut[Items] | None = core.arg(default=None)

        location: list[Location] | core.ArrayOut[Location] | None = core.arg(default=None)

        primary: Primary | None = core.arg(default=None)

        region: list[Region] | core.ArrayOut[Region] | None = core.arg(default=None)

        secondary: Secondary | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.data(type="aws_route53_traffic_policy_document", namespace="route53")
class DsTrafficPolicyDocument(core.Data):

    endpoint: list[Endpoint] | core.ArrayOut[Endpoint] | None = core.attr(
        Endpoint, default=None, kind=core.Kind.array
    )

    """
    (Required) ID of an endpoint you want to assign.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Standard JSON policy document rendered based on the arguments above.
    """
    json: str | core.StringOut = core.attr(str, computed=True)

    record_type: str | core.StringOut | None = core.attr(str, default=None)

    rule: list[Rule] | core.ArrayOut[Rule] | None = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    start_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    start_rule: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        endpoint: list[Endpoint] | core.ArrayOut[Endpoint] | None = None,
        record_type: str | core.StringOut | None = None,
        rule: list[Rule] | core.ArrayOut[Rule] | None = None,
        start_endpoint: str | core.StringOut | None = None,
        start_rule: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTrafficPolicyDocument.Args(
                endpoint=endpoint,
                record_type=record_type,
                rule=rule,
                start_endpoint=start_endpoint,
                start_rule=start_rule,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: list[Endpoint] | core.ArrayOut[Endpoint] | None = core.arg(default=None)

        record_type: str | core.StringOut | None = core.arg(default=None)

        rule: list[Rule] | core.ArrayOut[Rule] | None = core.arg(default=None)

        start_endpoint: str | core.StringOut | None = core.arg(default=None)

        start_rule: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)
