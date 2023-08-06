import terrascript.core as core


@core.data(type="aws_ssm_parameters_by_path", namespace="aws_ssm")
class DsParametersByPath(core.Data):

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    path: str | core.StringOut = core.attr(str)

    recursive: bool | core.BoolOut | None = core.attr(bool, default=None)

    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    with_decryption: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        path: str | core.StringOut,
        recursive: bool | core.BoolOut | None = None,
        with_decryption: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsParametersByPath.Args(
                path=path,
                recursive=recursive,
                with_decryption=with_decryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: str | core.StringOut = core.arg()

        recursive: bool | core.BoolOut | None = core.arg(default=None)

        with_decryption: bool | core.BoolOut | None = core.arg(default=None)
