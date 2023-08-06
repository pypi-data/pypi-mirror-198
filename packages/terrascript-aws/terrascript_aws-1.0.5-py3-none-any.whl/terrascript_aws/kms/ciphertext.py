import terrascript.core as core


@core.resource(type="aws_kms_ciphertext", namespace="kms")
class Ciphertext(core.Resource):
    """
    Base64 encoded ciphertext
    """

    ciphertext_blob: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An optional mapping that makes up the encryption context.
    """
    context: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Globally unique key ID for the customer master key.
    """
    key_id: str | core.StringOut = core.attr(str)

    """
    (Required) Data to be encrypted. Note that this may show up in logs, and it will be stored in the st
    ate file.
    """
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
