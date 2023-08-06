import terrascript.core as core


@core.resource(type="aws_iam_access_key", namespace="aws_iam")
class AccessKey(core.Resource):

    create_date: str | core.StringOut = core.attr(str, computed=True)

    encrypted_secret: str | core.StringOut = core.attr(str, computed=True)

    encrypted_ses_smtp_password_v4: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    pgp_key: str | core.StringOut | None = core.attr(str, default=None)

    secret: str | core.StringOut = core.attr(str, computed=True)

    ses_smtp_password_v4: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut | None = core.attr(str, default=None)

    user: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user: str | core.StringOut,
        pgp_key: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessKey.Args(
                user=user,
                pgp_key=pgp_key,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        pgp_key: str | core.StringOut | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        user: str | core.StringOut = core.arg()
