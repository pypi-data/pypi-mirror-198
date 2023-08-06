import terrascript.core as core


@core.resource(type="aws_route53_zone_association", namespace="aws_route53")
class ZoneAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    owning_account: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str)

    vpc_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    zone_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: str | core.StringOut,
        zone_id: str | core.StringOut,
        vpc_region: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ZoneAssociation.Args(
                vpc_id=vpc_id,
                zone_id=zone_id,
                vpc_region=vpc_region,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        vpc_id: str | core.StringOut = core.arg()

        vpc_region: str | core.StringOut | None = core.arg(default=None)

        zone_id: str | core.StringOut = core.arg()
