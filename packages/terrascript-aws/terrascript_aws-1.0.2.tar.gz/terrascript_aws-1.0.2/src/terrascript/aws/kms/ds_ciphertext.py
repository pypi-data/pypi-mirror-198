import terrascript.core as core


@core.data(type="aws_kms_ciphertext", namespace="aws_kms")
class DsCiphertext(core.Data):

    ciphertext_blob: str | core.StringOut = core.attr(str, computed=True)

    context: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    key_id: str | core.StringOut = core.attr(str)

    plaintext: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        key_id: str | core.StringOut,
        plaintext: str | core.StringOut,
        context: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCiphertext.Args(
                key_id=key_id,
                plaintext=plaintext,
                context=context,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        context: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        key_id: str | core.StringOut = core.arg()

        plaintext: str | core.StringOut = core.arg()
