import terrascript.core as core


@core.data(type="aws_location_route_calculator", namespace="location")
class DsRouteCalculator(core.Data):
    """
    The Amazon Resource Name (ARN) for the Route calculator resource. Use the ARN when you specify a res
    ource across AWS.
    """

    calculator_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the route calculator resource.
    """
    calculator_name: str | core.StringOut = core.attr(str)

    """
    The timestamp for when the route calculator resource was created in ISO 8601 format.
    """
    create_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The data provider of traffic and road network data.
    """
    data_source: str | core.StringOut = core.attr(str, computed=True)

    """
    The optional description of the route calculator resource.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags for the route calculator.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The timestamp for when the route calculator resource was last updated in ISO 8601 format.
    """
    update_time: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        calculator_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRouteCalculator.Args(
                calculator_name=calculator_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        calculator_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
