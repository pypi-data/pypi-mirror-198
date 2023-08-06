import terrascript.core as core


@core.resource(type="aws_elasticache_user", namespace="aws_elasticache")
class User(core.Resource):

    access_string: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    engine: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    no_password_required: bool | core.BoolOut | None = core.attr(bool, default=None)

    passwords: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_id: str | core.StringOut = core.attr(str)

    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_string: str | core.StringOut,
        engine: str | core.StringOut,
        user_id: str | core.StringOut,
        user_name: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        no_password_required: bool | core.BoolOut | None = None,
        passwords: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                access_string=access_string,
                engine=engine,
                user_id=user_id,
                user_name=user_name,
                arn=arn,
                no_password_required=no_password_required,
                passwords=passwords,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_string: str | core.StringOut = core.arg()

        arn: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut = core.arg()

        no_password_required: bool | core.BoolOut | None = core.arg(default=None)

        passwords: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_id: str | core.StringOut = core.arg()

        user_name: str | core.StringOut = core.arg()
