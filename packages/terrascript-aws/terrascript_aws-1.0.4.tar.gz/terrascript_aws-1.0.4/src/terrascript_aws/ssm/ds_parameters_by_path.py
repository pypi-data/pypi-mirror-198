import terrascript.core as core


@core.data(type="aws_ssm_parameters_by_path", namespace="ssm")
class DsParametersByPath(core.Data):
    """
    The ARNs of the parameters.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The names of the parameters.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) The prefix path of the parameter.
    """
    path: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether to recursively return parameters under `path`. Defaults to `false`.
    """
    recursive: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The types of the parameters.
    """
    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The value of the parameters.
    """
    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Whether to return decrypted `SecureString` value. Defaults to `true`.
    """
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
