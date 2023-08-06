import terrascript.core as core


@core.data(type="aws_outposts_sites", namespace="aws_outposts")
class DsSites(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsSites.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
