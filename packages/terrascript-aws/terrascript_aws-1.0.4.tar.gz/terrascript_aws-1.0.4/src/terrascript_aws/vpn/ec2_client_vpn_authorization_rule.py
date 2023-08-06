import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_authorization_rule", namespace="vpn")
class Ec2ClientVpnAuthorizationRule(core.Resource):
    """
    (Optional) The ID of the group to which the authorization rule grants access. One of `access_group_i
    d` or `authorize_all_groups` must be set.
    """

    access_group_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether the authorization rule grants access to all clients. One of `access_gro
    up_id` or `authorize_all_groups` must be set.
    """
    authorize_all_groups: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The ID of the Client VPN endpoint.
    """
    client_vpn_endpoint_id: str | core.StringOut = core.attr(str)

    """
    (Optional) A brief description of the authorization rule.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The IPv4 address range, in CIDR notation, of the network to which the authorization rule
    applies.
    """
    target_network_cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        client_vpn_endpoint_id: str | core.StringOut,
        target_network_cidr: str | core.StringOut,
        access_group_id: str | core.StringOut | None = None,
        authorize_all_groups: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnAuthorizationRule.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                target_network_cidr=target_network_cidr,
                access_group_id=access_group_id,
                authorize_all_groups=authorize_all_groups,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_group_id: str | core.StringOut | None = core.arg(default=None)

        authorize_all_groups: bool | core.BoolOut | None = core.arg(default=None)

        client_vpn_endpoint_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        target_network_cidr: str | core.StringOut = core.arg()
