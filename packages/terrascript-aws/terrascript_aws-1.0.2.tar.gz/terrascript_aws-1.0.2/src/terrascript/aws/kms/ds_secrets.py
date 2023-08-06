import terrascript.core as core


@core.schema
class Secret(core.Schema):

    context: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    payload: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        payload: str | core.StringOut,
        context: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Secret.Args(
                name=name,
                payload=payload,
                context=context,
                grant_tokens=grant_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        context: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        payload: str | core.StringOut = core.arg()


@core.data(type="aws_kms_secrets", namespace="aws_kms")
class DsSecrets(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    plaintext: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    secret: list[Secret] | core.ArrayOut[Secret] = core.attr(Secret, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        secret: list[Secret] | core.ArrayOut[Secret],
    ):
        super().__init__(
            name=data_name,
            args=DsSecrets.Args(
                secret=secret,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret: list[Secret] | core.ArrayOut[Secret] = core.arg()
