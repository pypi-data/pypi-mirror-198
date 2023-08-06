import terrascript.core as core


@core.resource(type="aws_iam_user_login_profile", namespace="iam")
class UserLoginProfile(core.Resource):
    """
    The encrypted password, base64 encoded. Only available if password was handled on Terraform resource
    creation, not import.
    """

    encrypted_password: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The fingerprint of the PGP key used to encrypt the password. Only available if password was handled
    on Terraform resource creation, not import.
    """
    key_fingerprint: str | core.StringOut = core.attr(str, computed=True)

    """
    The plain text password, only available when `pgp_key` is not provided.
    """
    password: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The length of the generated password on resource creation. Only applies on resource creat
    ion. Drift detection is not possible with this argument. Default value is `20`.
    """
    password_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Whether the user should be forced to reset the generated password on resource creation. O
    nly applies on resource creation.
    """
    password_reset_required: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:usern
    ame`. Only applies on resource creation. Drift detection is not possible with this argument.
    """
    pgp_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The IAM user's name.
    """
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
