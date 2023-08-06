import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_authorization_rule", namespace="aws_vpn")
class Ec2ClientVpnAuthorizationRule(core.Resource):

    access_group_id: str | core.StringOut | None = core.attr(str, default=None)

    authorize_all_groups: bool | core.BoolOut | None = core.attr(bool, default=None)

    client_vpn_endpoint_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

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
