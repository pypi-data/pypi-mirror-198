import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_route", namespace="aws_vpn")
class Ec2ClientVpnRoute(core.Resource):

    client_vpn_endpoint_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    destination_cidr_block: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    origin: str | core.StringOut = core.attr(str, computed=True)

    target_vpc_subnet_id: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        client_vpn_endpoint_id: str | core.StringOut,
        destination_cidr_block: str | core.StringOut,
        target_vpc_subnet_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnRoute.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                destination_cidr_block=destination_cidr_block,
                target_vpc_subnet_id=target_vpc_subnet_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_vpn_endpoint_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        destination_cidr_block: str | core.StringOut = core.arg()

        target_vpc_subnet_id: str | core.StringOut = core.arg()
