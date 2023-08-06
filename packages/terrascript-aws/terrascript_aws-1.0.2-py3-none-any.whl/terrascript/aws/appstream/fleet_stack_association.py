import terrascript.core as core


@core.resource(type="aws_appstream_fleet_stack_association", namespace="aws_appstream")
class FleetStackAssociation(core.Resource):

    fleet_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    stack_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        fleet_name: str | core.StringOut,
        stack_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FleetStackAssociation.Args(
                fleet_name=fleet_name,
                stack_name=stack_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        fleet_name: str | core.StringOut = core.arg()

        stack_name: str | core.StringOut = core.arg()
