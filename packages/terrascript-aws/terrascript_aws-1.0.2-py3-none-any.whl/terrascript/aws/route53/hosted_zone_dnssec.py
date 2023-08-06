import terrascript.core as core


@core.resource(type="aws_route53_hosted_zone_dnssec", namespace="aws_route53")
class HostedZoneDnssec(core.Resource):

    hosted_zone_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    signing_status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        hosted_zone_id: str | core.StringOut,
        signing_status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HostedZoneDnssec.Args(
                hosted_zone_id=hosted_zone_id,
                signing_status=signing_status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hosted_zone_id: str | core.StringOut = core.arg()

        signing_status: str | core.StringOut | None = core.arg(default=None)
