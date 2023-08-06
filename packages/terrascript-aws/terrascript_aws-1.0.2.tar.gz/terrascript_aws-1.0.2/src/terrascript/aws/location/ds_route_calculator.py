import terrascript.core as core


@core.data(type="aws_location_route_calculator", namespace="aws_location")
class DsRouteCalculator(core.Data):

    calculator_arn: str | core.StringOut = core.attr(str, computed=True)

    calculator_name: str | core.StringOut = core.attr(str)

    create_time: str | core.StringOut = core.attr(str, computed=True)

    data_source: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
