import terrascript.core as core


@core.data(type="aws_iam_role", namespace="aws_iam")
class DsRole(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    assume_role_policy: str | core.StringOut = core.attr(str, computed=True)

    create_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    max_session_duration: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

    path: str | core.StringOut = core.attr(str, computed=True)

    permissions_boundary: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRole.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
