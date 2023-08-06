import terrascript.core as core


@core.data(type="aws_kms_public_key", namespace="aws_kms")
class DsPublicKey(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    customer_master_key_spec: str | core.StringOut = core.attr(str, computed=True)

    encryption_algorithms: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    key_id: str | core.StringOut = core.attr(str)

    key_usage: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut = core.attr(str, computed=True)

    public_key_pem: str | core.StringOut = core.attr(str, computed=True)

    signing_algorithms: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        key_id: str | core.StringOut,
        grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPublicKey.Args(
                key_id=key_id,
                grant_tokens=grant_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        key_id: str | core.StringOut = core.arg()
