import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_multicast_domain_association", namespace="transit_gateway"
)
class Ec2TransitGatewayMulticastDomainAssociation(core.Resource):
    """
    EC2 Transit Gateway Multicast Domain Association identifier.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the subnet to associate with the transit gateway multicast domain.
    """
    subnet_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the transit gateway attachment.
    """
    transit_gateway_attachment_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the transit gateway multicast domain.
    """
    transit_gateway_multicast_domain_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_id: str | core.StringOut,
        transit_gateway_attachment_id: str | core.StringOut,
        transit_gateway_multicast_domain_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayMulticastDomainAssociation.Args(
                subnet_id=subnet_id,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        subnet_id: str | core.StringOut = core.arg()

        transit_gateway_attachment_id: str | core.StringOut = core.arg()

        transit_gateway_multicast_domain_id: str | core.StringOut = core.arg()
