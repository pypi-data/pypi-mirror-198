import terrascript.core as core


@core.resource(type="aws_lightsail_key_pair", namespace="lightsail")
class KeyPair(core.Resource):
    """
    The ARN of the Lightsail key pair
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The MD5 public key fingerprint for the encrypted
    """
    encrypted_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    encrypted_private_key: str | core.StringOut = core.attr(str, computed=True)

    """
    The MD5 public key fingerprint as specified in section 4 of RFC 4716.
    """
    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    """
    The name used for this key pair
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the Lightsail Key Pair. If omitted, a unique
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    pgp_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    the private key, base64 encoded. This is only populated
    """
    private_key: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The public key material. This public key will be
    """
    public_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        pgp_key: str | core.StringOut | None = None,
        public_key: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeyPair.Args(
                name=name,
                name_prefix=name_prefix,
                pgp_key=pgp_key,
                public_key=public_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        pgp_key: str | core.StringOut | None = core.arg(default=None)

        public_key: str | core.StringOut | None = core.arg(default=None)
