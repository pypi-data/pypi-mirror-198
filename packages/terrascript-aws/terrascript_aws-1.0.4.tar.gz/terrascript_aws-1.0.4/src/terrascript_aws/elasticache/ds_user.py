import terrascript.core as core


@core.data(type="aws_elasticache_user", namespace="elasticache")
class DsUser(core.Data):
    """
    A string for what access a user possesses within the associated ElastiCache replication groups or cl
    usters.
    """

    access_string: str | core.StringOut | None = core.attr(str, default=None)

    engine: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    no_password_required: bool | core.BoolOut | None = core.attr(bool, default=None)

    passwords: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The identifier for the user.
    """
    user_id: str | core.StringOut = core.attr(str)

    """
    The user name of the user.
    """
    user_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        user_id: str | core.StringOut,
        access_string: str | core.StringOut | None = None,
        engine: str | core.StringOut | None = None,
        no_password_required: bool | core.BoolOut | None = None,
        passwords: list[str] | core.ArrayOut[core.StringOut] | None = None,
        user_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                user_id=user_id,
                access_string=access_string,
                engine=engine,
                no_password_required=no_password_required,
                passwords=passwords,
                user_name=user_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_string: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut | None = core.arg(default=None)

        no_password_required: bool | core.BoolOut | None = core.arg(default=None)

        passwords: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        user_id: str | core.StringOut = core.arg()

        user_name: str | core.StringOut | None = core.arg(default=None)
