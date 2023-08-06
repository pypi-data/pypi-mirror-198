import terrascript.core as core


@core.resource(type="aws_dx_gateway_association", namespace="direct_connect")
class DxGatewayAssociation(core.Resource):
    """
    (Optional) VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR blo
    ck of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
    """

    allowed_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
    """
    associated_gateway_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The ID of the AWS account that owns the VGW or transit gateway with which to associate th
    e Direct Connect gateway.
    """
    associated_gateway_owner_account_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
    """
    associated_gateway_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the Direct Connect gateway association.
    """
    dx_gateway_association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Direct Connect gateway.
    """
    dx_gateway_id: str | core.StringOut = core.attr(str)

    """
    The ID of the AWS account that owns the Direct Connect gateway.
    """
    dx_gateway_owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the Direct Connect gateway association resource.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the Direct Connect gateway association proposal.
    """
    proposal_id: str | core.StringOut | None = core.attr(str, default=None)

    vpn_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        dx_gateway_id: str | core.StringOut,
        allowed_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        associated_gateway_id: str | core.StringOut | None = None,
        associated_gateway_owner_account_id: str | core.StringOut | None = None,
        proposal_id: str | core.StringOut | None = None,
        vpn_gateway_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxGatewayAssociation.Args(
                dx_gateway_id=dx_gateway_id,
                allowed_prefixes=allowed_prefixes,
                associated_gateway_id=associated_gateway_id,
                associated_gateway_owner_account_id=associated_gateway_owner_account_id,
                proposal_id=proposal_id,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        associated_gateway_id: str | core.StringOut | None = core.arg(default=None)

        associated_gateway_owner_account_id: str | core.StringOut | None = core.arg(default=None)

        dx_gateway_id: str | core.StringOut = core.arg()

        proposal_id: str | core.StringOut | None = core.arg(default=None)

        vpn_gateway_id: str | core.StringOut | None = core.arg(default=None)
