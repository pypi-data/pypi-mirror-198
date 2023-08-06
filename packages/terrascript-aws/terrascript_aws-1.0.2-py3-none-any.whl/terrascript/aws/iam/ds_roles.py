import terrascript.core as core


@core.data(type="aws_iam_roles", namespace="aws_iam")
class DsRoles(core.Data):

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    path_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: str | core.StringOut | None = None,
        path_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRoles.Args(
                name_regex=name_regex,
                path_prefix=path_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_regex: str | core.StringOut | None = core.arg(default=None)

        path_prefix: str | core.StringOut | None = core.arg(default=None)
