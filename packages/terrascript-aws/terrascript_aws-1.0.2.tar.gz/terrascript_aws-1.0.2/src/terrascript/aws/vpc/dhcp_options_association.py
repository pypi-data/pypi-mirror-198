import terrascript.core as core


@core.resource(type="aws_vpc_dhcp_options_association", namespace="aws_vpc")
class DhcpOptionsAssociation(core.Resource):

    dhcp_options_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
