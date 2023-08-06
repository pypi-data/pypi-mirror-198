import terrascript.core as core


@core.schema
class Auth(core.Schema):

    auth_scheme: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    iam_auth: str | core.StringOut = core.attr(str, computed=True)

    secret_arn: str | core.StringOut = core.attr(str, computed=True)

    username: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        auth_scheme: str | core.StringOut,
        description: str | core.StringOut,
        iam_auth: str | core.StringOut,
        secret_arn: str | core.StringOut,
        username: str | core.StringOut,
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
        auth_scheme: str | core.StringOut = core.arg()

        description: str | core.StringOut = core.arg()

        iam_auth: str | core.StringOut = core.arg()

        secret_arn: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.data(type="aws_db_proxy", namespace="aws_rds")
class DsDbProxy(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auth: list[Auth] | core.ArrayOut[Auth] = core.attr(Auth, computed=True, kind=core.Kind.array)

    debug_logging: bool | core.BoolOut = core.attr(bool, computed=True)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    engine_family: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    idle_client_timeout: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

    require_tls: bool | core.BoolOut = core.attr(bool, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDbProxy.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
