import terrascript.core as core


@core.resource(type="aws_dx_gateway_association_proposal", namespace="direct_connect")
class DxGatewayAssociationProposal(core.Resource):
    """
    (Optional) VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR blo
    ck of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
    """

    allowed_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
    """
    associated_gateway_id: str | core.StringOut = core.attr(str)

    """
    The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Co
    nnect gateway.
    """
    associated_gateway_owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The type of the associated gateway, `transitGateway` or `virtualPrivateGateway`.
    """
    associated_gateway_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Direct Connect Gateway identifier.
    """
    dx_gateway_id: str | core.StringOut = core.attr(str)

    """
    (Required) AWS Account identifier of the Direct Connect Gateway's owner.
    """
    dx_gateway_owner_account_id: str | core.StringOut = core.attr(str)

    """
    Direct Connect Gateway Association Proposal identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        associated_gateway_id: str | core.StringOut,
        dx_gateway_id: str | core.StringOut,
        dx_gateway_owner_account_id: str | core.StringOut,
        allowed_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxGatewayAssociationProposal.Args(
                associated_gateway_id=associated_gateway_id,
                dx_gateway_id=dx_gateway_id,
                dx_gateway_owner_account_id=dx_gateway_owner_account_id,
                allowed_prefixes=allowed_prefixes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        associated_gateway_id: str | core.StringOut = core.arg()

        dx_gateway_id: str | core.StringOut = core.arg()

        dx_gateway_owner_account_id: str | core.StringOut = core.arg()
