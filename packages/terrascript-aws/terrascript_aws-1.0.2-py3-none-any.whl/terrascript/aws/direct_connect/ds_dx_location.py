import terrascript.core as core


@core.data(type="aws_dx_location", namespace="aws_direct_connect")
class DsDxLocation(core.Data):

    available_macsec_port_speeds: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    available_port_speeds: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    available_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    location_code: str | core.StringOut = core.attr(str)

    location_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        location_code: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDxLocation.Args(
                location_code=location_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        location_code: str | core.StringOut = core.arg()
