import terrascript.core as core


@core.resource(type="aws_vpc_dhcp_options_association", namespace="vpc")
class DhcpOptionsAssociation(core.Resource):
    """
    (Required) The ID of the DHCP Options Set to associate to the VPC.
    """

    dhcp_options_id: str | core.StringOut = core.attr(str)

    """
    The ID of the DHCP Options Set Association.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the VPC to which we would like to associate a DHCP Options Set.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        dhcp_options_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DhcpOptionsAssociation.Args(
                dhcp_options_id=dhcp_options_id,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        dhcp_options_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()
