import terrascript.core as core


@core.schema
class GeoMatchConstraint(core.Schema):

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=GeoMatchConstraint.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_waf_geo_match_set", namespace="waf")
class GeoMatchSet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    geo_match_constraint: list[GeoMatchConstraint] | core.ArrayOut[
        GeoMatchConstraint
    ] | None = core.attr(GeoMatchConstraint, default=None, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        geo_match_constraint: list[GeoMatchConstraint]
        | core.ArrayOut[GeoMatchConstraint]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GeoMatchSet.Args(
                name=name,
                geo_match_constraint=geo_match_constraint,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        geo_match_constraint: list[GeoMatchConstraint] | core.ArrayOut[
            GeoMatchConstraint
        ] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
