import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_security_group_association", namespace="vpc")
class EndpointSecurityGroupAssociation(core.Resource):
    """
    The ID of the association.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether this association should replace the association with the VPC's default security g
    roup that is created when no security groups are specified during VPC endpoint creation. At most 1 a
    ssociation per-VPC endpoint should be configured with `replace_default_association = true`.
    """
    replace_default_association: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The ID of the security group to be associated with the VPC endpoint.
    """
    security_group_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the VPC endpoint with which the security group will be associated.
    """
    vpc_endpoint_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        security_group_id: str | core.StringOut,
        vpc_endpoint_id: str | core.StringOut,
        replace_default_association: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointSecurityGroupAssociation.Args(
                security_group_id=security_group_id,
                vpc_endpoint_id=vpc_endpoint_id,
                replace_default_association=replace_default_association,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        replace_default_association: bool | core.BoolOut | None = core.arg(default=None)

        security_group_id: str | core.StringOut = core.arg()

        vpc_endpoint_id: str | core.StringOut = core.arg()
