import terrascript.core as core


@core.schema
class Auth(core.Schema):

    auth_scheme: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    iam_auth: str | core.StringOut | None = core.attr(str, default=None)

    secret_arn: str | core.StringOut | None = core.attr(str, default=None)

    username: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auth_scheme: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        iam_auth: str | core.StringOut | None = None,
        secret_arn: str | core.StringOut | None = None,
        username: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Auth.Args(
                auth_scheme=auth_scheme,
                description=description,
                iam_auth=iam_auth,
                secret_arn=secret_arn,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_scheme: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        iam_auth: str | core.StringOut | None = core.arg(default=None)

        secret_arn: str | core.StringOut | None = core.arg(default=None)

        username: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_db_proxy", namespace="aws_rds")
class DbProxy(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auth: list[Auth] | core.ArrayOut[Auth] = core.attr(Auth, kind=core.Kind.array)

    debug_logging: bool | core.BoolOut | None = core.attr(bool, default=None)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine_family: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_client_timeout: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    require_tls: bool | core.BoolOut | None = core.attr(bool, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    vpc_subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        auth: list[Auth] | core.ArrayOut[Auth],
        engine_family: str | core.StringOut,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        vpc_subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        debug_logging: bool | core.BoolOut | None = None,
        idle_client_timeout: int | core.IntOut | None = None,
        require_tls: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxy.Args(
                auth=auth,
                engine_family=engine_family,
                name=name,
                role_arn=role_arn,
                vpc_subnet_ids=vpc_subnet_ids,
                debug_logging=debug_logging,
                idle_client_timeout=idle_client_timeout,
                require_tls=require_tls,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth: list[Auth] | core.ArrayOut[Auth] = core.arg()

        debug_logging: bool | core.BoolOut | None = core.arg(default=None)

        engine_family: str | core.StringOut = core.arg()

        idle_client_timeout: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        require_tls: bool | core.BoolOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpc_subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()
