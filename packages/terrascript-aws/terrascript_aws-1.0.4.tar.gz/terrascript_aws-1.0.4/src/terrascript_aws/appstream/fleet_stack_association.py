import terrascript.core as core


@core.resource(type="aws_appstream_fleet_stack_association", namespace="appstream")
class FleetStackAssociation(core.Resource):
    """
    (Required) Name of the fleet.
    """

    fleet_name: str | core.StringOut = core.attr(str)

    """
    Unique ID of the appstream stack fleet association, composed of the `fleet_name` and `stack_name` se
    parated by a slash (`/`).
    """
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
