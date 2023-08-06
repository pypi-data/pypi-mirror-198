import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_multicast_domain", namespace="aws_transit_gateway")
class Ec2TransitGatewayMulticastDomain(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_accept_shared_associations: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    igmpv2_support: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    static_sources_support: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_id: str | core.StringOut,
        auto_accept_shared_associations: str | core.StringOut | None = None,
        igmpv2_support: str | core.StringOut | None = None,
        static_sources_support: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayMulticastDomain.Args(
                transit_gateway_id=transit_gateway_id,
                auto_accept_shared_associations=auto_accept_shared_associations,
                igmpv2_support=igmpv2_support,
                static_sources_support=static_sources_support,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_accept_shared_associations: str | core.StringOut | None = core.arg(default=None)

        igmpv2_support: str | core.StringOut | None = core.arg(default=None)

        static_sources_support: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut = core.arg()
