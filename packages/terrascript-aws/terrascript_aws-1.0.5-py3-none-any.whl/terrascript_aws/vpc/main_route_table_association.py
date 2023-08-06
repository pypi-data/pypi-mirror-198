import terrascript.core as core


@core.resource(type="aws_main_route_table_association", namespace="vpc")
class MainRouteTableAssociation(core.Resource):
    """
    The ID of the Route Table Association
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Used internally, see __Notes__ below
    """
    original_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the Route Table to set as the new
    """
    route_table_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the VPC whose main route table should be set
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MainRouteTableAssociation.Args(
                route_table_id=route_table_id,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        route_table_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()
