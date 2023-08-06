import terrascript.core as core


@core.resource(type="aws_iam_user_login_profile", namespace="aws_iam")
class UserLoginProfile(core.Resource):

    encrypted_password: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    password: str | core.StringOut = core.attr(str, computed=True)

    password_length: int | core.IntOut | None = core.attr(int, default=None)

    password_reset_required: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    pgp_key: str | core.StringOut | None = core.attr(str, default=None)

    user: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user: str | core.StringOut,
        password_length: int | core.IntOut | None = None,
        password_reset_required: bool | core.BoolOut | None = None,
        pgp_key: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserLoginProfile.Args(
                user=user,
                password_length=password_length,
                password_reset_required=password_reset_required,
                pgp_key=pgp_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        password_length: int | core.IntOut | None = core.arg(default=None)

        password_reset_required: bool | core.BoolOut | None = core.arg(default=None)

        pgp_key: str | core.StringOut | None = core.arg(default=None)

        user: str | core.StringOut = core.arg()
