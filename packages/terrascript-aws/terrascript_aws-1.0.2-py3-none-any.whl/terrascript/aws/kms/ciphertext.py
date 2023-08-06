import terrascript.core as core


@core.resource(type="aws_kms_ciphertext", namespace="aws_kms")
class Ciphertext(core.Resource):

    ciphertext_blob: str | core.StringOut = core.attr(str, computed=True)

    context: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    key_id: str | core.StringOut = core.attr(str)

    plaintext: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key_id: str | core.StringOut,
        plaintext: str | core.StringOut,
        context: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ciphertext.Args(
                key_id=key_id,
                plaintext=plaintext,
                context=context,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        context: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        key_id: str | core.StringOut = core.arg()

        plaintext: str | core.StringOut = core.arg()
