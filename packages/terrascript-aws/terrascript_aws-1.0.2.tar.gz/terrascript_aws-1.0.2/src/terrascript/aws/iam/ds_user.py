import terrascript.core as core


@core.data(type="aws_iam_user", namespace="aws_iam")
class DsUser(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut = core.attr(str, computed=True)

    permissions_boundary: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_id: str | core.StringOut = core.attr(str, computed=True)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        user_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                user_name=user_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
