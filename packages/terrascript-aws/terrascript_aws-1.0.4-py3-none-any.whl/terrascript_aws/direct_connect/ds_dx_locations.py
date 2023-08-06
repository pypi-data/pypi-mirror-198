import terrascript.core as core


@core.data(type="aws_dx_locations", namespace="direct_connect")
class DsDxLocations(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The code for the locations.
    """
    location_codes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsDxLocations.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
