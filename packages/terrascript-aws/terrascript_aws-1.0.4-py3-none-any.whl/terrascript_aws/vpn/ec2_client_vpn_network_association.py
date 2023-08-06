import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_network_association", namespace="vpn")
class Ec2ClientVpnNetworkAssociation(core.Resource):
    """
    The unique ID of the target network association.
    """

    association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Client VPN endpoint.
    """
    client_vpn_endpoint_id: str | core.StringOut = core.attr(str)

    """
    The unique ID of the target network association.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, **Deprecated** use the `security_group_ids` argument of the `aws_ec2_client_vpn_endpoint`
    resource instead) A list of up to five custom security groups to apply to the target network. If no
    t specified, the VPC's default security group is assigned.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    **Deprecated** The current state of the target network association.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the subnet to associate with the Client VPN endpoint.
    """
    subnet_id: str | core.StringOut = core.attr(str)

    """
    The ID of the VPC in which the target subnet is located.
    """
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
