import terrascript.core as core


@core.data(type="aws_kms_public_key", namespace="kms")
class DsPublicKey(core.Data):
    """
    Key ARN of the asymmetric CMK from which the public key was downloaded.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Type of the public key that was downloaded.
    """
    customer_master_key_spec: str | core.StringOut = core.attr(str, computed=True)

    """
    Encryption algorithms that AWS KMS supports for this key. Only set when the `key_usage` of the publi
    c key is `ENCRYPT_DECRYPT`.
    """
    encryption_algorithms: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) List of grant tokens
    """
    grant_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    Key ARN of the asymmetric CMK from which the public key was downloaded.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Key identifier which can be one of the following format:
    """
    key_id: str | core.StringOut = core.attr(str)

    """
    Permitted use of the public key. Valid values are `ENCRYPT_DECRYPT` or `SIGN_VERIFY`
    """
    key_usage: str | core.StringOut = core.attr(str, computed=True)

    """
    Exported public key. The value is a DER-encoded X.509 public key, also known as SubjectPublicKeyInfo
    (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280). The value is Base64-encoded.
    """
    public_key: str | core.StringOut = core.attr(str, computed=True)

    """
    Exported public key. The value is Privacy Enhanced Mail (PEM) encoded.
    """
    public_key_pem: str | core.StringOut = core.attr(str, computed=True)

    """
    Signing algorithms that AWS KMS supports for this key. Only set when the `key_usage` of the public k
    ey is `SIGN_VERIFY`.
    """
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
