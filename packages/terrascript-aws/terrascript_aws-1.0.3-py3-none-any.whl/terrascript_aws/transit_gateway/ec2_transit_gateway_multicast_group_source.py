import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_multicast_group_source", namespace="transit_gateway")
class Ec2TransitGatewayMulticastGroupSource(core.Resource):

    group_ip_address: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str)

    transit_gateway_multicast_domain_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_ip_address: str | core.StringOut,
        network_interface_id: str | core.StringOut,
        transit_gateway_multicast_domain_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayMulticastGroupSource.Args(
                group_ip_address=group_ip_address,
                network_interface_id=network_interface_id,
                transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_ip_address: str | core.StringOut = core.arg()

        network_interface_id: str | core.StringOut = core.arg()

        transit_gateway_multicast_domain_id: str | core.StringOut = core.arg()
