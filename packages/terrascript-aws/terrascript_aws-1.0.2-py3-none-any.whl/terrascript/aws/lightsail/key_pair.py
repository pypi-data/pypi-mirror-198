import terrascript.core as core


@core.resource(type="aws_lightsail_key_pair", namespace="aws_lightsail")
class KeyPair(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    encrypted_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    encrypted_private_key: str | core.StringOut = core.attr(str, computed=True)

    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None)

    pgp_key: str | core.StringOut | None = core.attr(str, default=None)

    private_key: str | core.StringOut = core.attr(str, computed=True)

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
