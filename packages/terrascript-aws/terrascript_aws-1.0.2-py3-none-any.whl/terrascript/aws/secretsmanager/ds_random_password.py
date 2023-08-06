import terrascript.core as core


@core.data(type="aws_secretsmanager_random_password", namespace="aws_secretsmanager")
class DsRandomPassword(core.Data):

    exclude_characters: str | core.StringOut | None = core.attr(str, default=None)

    exclude_lowercase: bool | core.BoolOut | None = core.attr(bool, default=None)

    exclude_numbers: bool | core.BoolOut | None = core.attr(bool, default=None)

    exclude_punctuation: bool | core.BoolOut | None = core.attr(bool, default=None)

    exclude_uppercase: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    include_space: bool | core.BoolOut | None = core.attr(bool, default=None)

    password_length: int | core.IntOut | None = core.attr(int, default=None)

    random_password: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    require_each_included_type: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        exclude_characters: str | core.StringOut | None = None,
        exclude_lowercase: bool | core.BoolOut | None = None,
        exclude_numbers: bool | core.BoolOut | None = None,
        exclude_punctuation: bool | core.BoolOut | None = None,
        exclude_uppercase: bool | core.BoolOut | None = None,
        include_space: bool | core.BoolOut | None = None,
        password_length: int | core.IntOut | None = None,
        random_password: str | core.StringOut | None = None,
        require_each_included_type: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRandomPassword.Args(
                exclude_characters=exclude_characters,
                exclude_lowercase=exclude_lowercase,
                exclude_numbers=exclude_numbers,
                exclude_punctuation=exclude_punctuation,
                exclude_uppercase=exclude_uppercase,
                include_space=include_space,
                password_length=password_length,
                random_password=random_password,
                require_each_included_type=require_each_included_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_characters: str | core.StringOut | None = core.arg(default=None)

        exclude_lowercase: bool | core.BoolOut | None = core.arg(default=None)

        exclude_numbers: bool | core.BoolOut | None = core.arg(default=None)

        exclude_punctuation: bool | core.BoolOut | None = core.arg(default=None)

        exclude_uppercase: bool | core.BoolOut | None = core.arg(default=None)

        include_space: bool | core.BoolOut | None = core.arg(default=None)

        password_length: int | core.IntOut | None = core.arg(default=None)

        random_password: str | core.StringOut | None = core.arg(default=None)

        require_each_included_type: bool | core.BoolOut | None = core.arg(default=None)
