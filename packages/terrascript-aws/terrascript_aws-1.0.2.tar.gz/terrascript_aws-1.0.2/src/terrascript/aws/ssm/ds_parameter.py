import terrascript.core as core


@core.data(type="aws_ssm_parameter", namespace="aws_ssm")
class DsParameter(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    version: int | core.IntOut = core.attr(int, computed=True)

    with_decryption: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        with_decryption: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsParameter.Args(
                name=name,
                with_decryption=with_decryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        with_decryption: bool | core.BoolOut | None = core.arg(default=None)
