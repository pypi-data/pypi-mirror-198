import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_network_association", namespace="aws_vpn")
class Ec2ClientVpnNetworkAssociation(core.Resource):

    association_id: str | core.StringOut = core.attr(str, computed=True)

    client_vpn_endpoint_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        client_vpn_endpoint_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnNetworkAssociation.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                subnet_id=subnet_id,
                security_groups=security_groups,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_vpn_endpoint_id: str | core.StringOut = core.arg()

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnet_id: str | core.StringOut = core.arg()
