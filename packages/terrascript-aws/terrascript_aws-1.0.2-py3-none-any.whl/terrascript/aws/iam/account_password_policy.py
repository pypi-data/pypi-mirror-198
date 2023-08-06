import terrascript.core as core


@core.resource(type="aws_iam_account_password_policy", namespace="aws_iam")
class AccountPasswordPolicy(core.Resource):

    allow_users_to_change_password: bool | core.BoolOut | None = core.attr(bool, default=None)

    expire_passwords: bool | core.BoolOut = core.attr(bool, computed=True)

    hard_expiry: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    max_password_age: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    minimum_password_length: int | core.IntOut | None = core.attr(int, default=None)

    password_reuse_prevention: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    require_lowercase_characters: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    require_numbers: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    require_symbols: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

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
