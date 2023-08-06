import terrascript.core as core


@core.resource(type="aws_route_table_association", namespace="aws_vpc")
class RouteTableAssociation(core.Resource):

    gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    route_table_id: str | core.StringOut = core.attr(str)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: str | core.StringOut,
        gateway_id: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RouteTableAssociation.Args(
                route_table_id=route_table_id,
                gateway_id=gateway_id,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        gateway_id: str | core.StringOut | None = core.arg(default=None)

        route_table_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut | None = core.arg(default=None)
