import terrascript.core as core


@core.data(type="aws_dx_location", namespace="direct_connect")
class DsDxLocation(core.Data):
    """
    The available MAC Security (MACsec) port speeds for the location.
    """

    available_macsec_port_speeds: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The available port speeds for the location.
    """
    available_port_speeds: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The names of the service providers for the location.
    """
    available_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The code for the location to retrieve.
    """
    location_code: str | core.StringOut = core.attr(str)

    """
    The name of the location. This includes the name of the colocation partner and the physical site of
    the building.
    """
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
