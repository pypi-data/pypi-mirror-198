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


@core.resource(type="aws_db_proxy", namespace="rds")
class DbProxy(core.Resource):
    """
    The Amazon Resource Name (ARN) for the proxy.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block(s) with authorization mechanisms to connect to the associated instanc
    es or clusters. Described below.
    """
    auth: list[Auth] | core.ArrayOut[Auth] = core.attr(Auth, kind=core.Kind.array)

    """
    (Optional) Whether the proxy includes detailed information about SQL statements in its logs. This in
    formation helps you to debug issues involving SQL behavior or the performance and scalability of the
    proxy connections. The debug information includes the text of SQL statements that you submit throug
    h the proxy. Thus, only enable this setting when needed for debugging, and only when you have securi
    ty measures in place to safeguard any sensitive information that appears in the logs.
    """
    debug_logging: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The endpoint that you can use to connect to the proxy. You include the endpoint value in the connect
    ion string for a database client application.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The kinds of databases that the proxy can connect to. This value det
    ermines which database network protocol the proxy recognizes when it interprets network traffic to a
    nd from the database. The engine family applies to MySQL and PostgreSQL for both RDS and Aurora. Val
    id values are `MYSQL` and `POSTGRESQL`.
    """
    engine_family: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the proxy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of seconds that a connection to the proxy can be inactive before the proxy dis
    connects it. You can set this value higher or lower than the connection timeout limit for the associ
    ated database.
    """
    idle_client_timeout: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Required) The identifier for the proxy. This name must be unique for all proxies owned by your AWS
    account in the specified AWS Region. An identifier must begin with a letter and must contain only AS
    CII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A Boolean parameter that specifies whether Transport Layer Security (TLS) encryption is r
    equired for connections to the proxy. By enabling this setting, you can enforce encrypted TLS connec
    tions to the proxy.
    """
    require_tls: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in A
    WS Secrets Manager.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) A mapping of tags to assign to the resource. If configured with a provider [`default_tags
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tag
    s-configuration-block) present, tags with matching keys will overwrite those defined at the provider
    level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) One or more VPC security group IDs to associate with the new proxy.
    """
    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) One or more VPC subnet IDs to associate with the new proxy.
    """
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
