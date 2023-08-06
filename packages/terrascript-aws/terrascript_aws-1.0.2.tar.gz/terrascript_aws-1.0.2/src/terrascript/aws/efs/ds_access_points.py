import terrascript.core as core


@core.data(type="aws_efs_access_points", namespace="aws_efs")
class DsAccessPoints(core.Data):

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    file_system_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        file_system_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsAccessPoints.Args(
                file_system_id=file_system_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_system_id: str | core.StringOut = core.arg()
