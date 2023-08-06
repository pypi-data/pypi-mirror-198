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


@core.data(type="aws_db_proxy", namespace="rds")
class DsDbProxy(core.Data):
    """
    The ARN of the DB Proxy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The configuration(s) with authorization mechanisms to connect to the associated instance or cluster.
    """
    auth: list[Auth] | core.ArrayOut[Auth] = core.attr(Auth, computed=True, kind=core.Kind.array)

    """
    Whether the proxy includes detailed information about SQL statements in its logs.
    """
    debug_logging: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The endpoint that you can use to connect to the DB proxy.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The kinds of databases that the proxy can connect to.
    """
    engine_family: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The number of seconds a connection to the proxy can have no activity before the proxy drops the clie
    nt connection.
    """
    idle_client_timeout: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The name of the DB proxy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Indicates whether Transport Layer Security (TLS) encryption is required for connections to the proxy
    .
    """
    require_tls: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The Amazon Resource Name (ARN) for the IAM role that the proxy uses to access Amazon Secrets Manager
    .
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides the VPC ID of the DB proxy.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Provides a list of VPC security groups that the proxy belongs to.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The EC2 subnet IDs for the proxy.
    """
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
