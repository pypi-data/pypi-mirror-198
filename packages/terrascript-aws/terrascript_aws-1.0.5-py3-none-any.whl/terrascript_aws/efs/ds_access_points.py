import terrascript.core as core


@core.data(type="aws_efs_access_points", namespace="efs")
class DsAccessPoints(core.Data):
    """
    Set of Amazon Resource Names (ARNs).
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) EFS File System identifier.
    """
    file_system_id: str | core.StringOut = core.attr(str)

    """
    EFS File System identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of identifiers.
    """
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
