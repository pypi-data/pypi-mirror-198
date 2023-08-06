import terrascript.core as core


@core.resource(type="aws_iam_account_password_policy", namespace="iam")
class AccountPasswordPolicy(core.Resource):
    """
    (Optional) Whether to allow users to change their own password
    """

    allow_users_to_change_password: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Indicates whether passwords in the account expire. Returns `true` if `max_password_age` contains a v
    alue greater than `0`. Returns `false` if it is `0` or _not present_.
    """
    expire_passwords: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Whether users are prevented from setting a new password after their password has expired
    (i.e., require administrator reset)
    """
    hard_expiry: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of days that an user password is valid.
    """
    max_password_age: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Minimum length to require for user passwords.
    """
    minimum_password_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The number of previous passwords that users are prevented from reusing.
    """
    password_reuse_prevention: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) Whether to require lowercase characters for user passwords.
    """
    require_lowercase_characters: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Whether to require numbers for user passwords.
    """
    require_numbers: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Whether to require symbols for user passwords.
    """
    require_symbols: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Whether to require uppercase characters for user passwords.
    """
    require_uppercase_characters: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allow_users_to_change_password: bool | core.BoolOut | None = None,
        hard_expiry: bool | core.BoolOut | None = None,
        max_password_age: int | core.IntOut | None = None,
        minimum_password_length: int | core.IntOut | None = None,
        password_reuse_prevention: int | core.IntOut | None = None,
        require_lowercase_characters: bool | core.BoolOut | None = None,
        require_numbers: bool | core.BoolOut | None = None,
        require_symbols: bool | core.BoolOut | None = None,
        require_uppercase_characters: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccountPasswordPolicy.Args(
                allow_users_to_change_password=allow_users_to_change_password,
                hard_expiry=hard_expiry,
                max_password_age=max_password_age,
                minimum_password_length=minimum_password_length,
                password_reuse_prevention=password_reuse_prevention,
                require_lowercase_characters=require_lowercase_characters,
                require_numbers=require_numbers,
                require_symbols=require_symbols,
                require_uppercase_characters=require_uppercase_characters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_users_to_change_password: bool | core.BoolOut | None = core.arg(default=None)

        hard_expiry: bool | core.BoolOut | None = core.arg(default=None)

        max_password_age: int | core.IntOut | None = core.arg(default=None)

        minimum_password_length: int | core.IntOut | None = core.arg(default=None)

        password_reuse_prevention: int | core.IntOut | None = core.arg(default=None)

        require_lowercase_characters: bool | core.BoolOut | None = core.arg(default=None)

        require_numbers: bool | core.BoolOut | None = core.arg(default=None)

        require_symbols: bool | core.BoolOut | None = core.arg(default=None)

        require_uppercase_characters: bool | core.BoolOut | None = core.arg(default=None)
