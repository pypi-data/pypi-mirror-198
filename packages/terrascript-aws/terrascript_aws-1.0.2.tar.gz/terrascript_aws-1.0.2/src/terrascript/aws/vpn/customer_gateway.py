import terrascript.core as core


@core.resource(type="aws_customer_gateway", namespace="aws_vpn")
class CustomerGateway(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    bgp_asn: str | core.StringOut = core.attr(str)

    certificate_arn: str | core.StringOut | None = core.attr(str, default=None)

    device_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bgp_asn: str | core.StringOut,
        ip_address: str | core.StringOut,
        type: str | core.StringOut,
        certificate_arn: str | core.StringOut | None = None,
        device_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomerGateway.Args(
                bgp_asn=bgp_asn,
                ip_address=ip_address,
                type=type,
                certificate_arn=certificate_arn,
                device_name=device_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bgp_asn: str | core.StringOut = core.arg()

        certificate_arn: str | core.StringOut | None = core.arg(default=None)

        device_name: str | core.StringOut | None = core.arg(default=None)

        ip_address: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
