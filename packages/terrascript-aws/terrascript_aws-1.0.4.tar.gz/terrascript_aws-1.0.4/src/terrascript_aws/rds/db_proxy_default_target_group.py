import terrascript.core as core


@core.schema
class ConnectionPoolConfig(core.Schema):

    connection_borrow_timeout: int | core.IntOut | None = core.attr(int, default=None)

    init_query: str | core.StringOut | None = core.attr(str, default=None)

    max_connections_percent: int | core.IntOut | None = core.attr(int, default=None)

    max_idle_connections_percent: int | core.IntOut | None = core.attr(int, default=None)

    session_pinning_filters: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        connection_borrow_timeout: int | core.IntOut | None = None,
        init_query: str | core.StringOut | None = None,
        max_connections_percent: int | core.IntOut | None = None,
        max_idle_connections_percent: int | core.IntOut | None = None,
        session_pinning_filters: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=ConnectionPoolConfig.Args(
                connection_borrow_timeout=connection_borrow_timeout,
                init_query=init_query,
                max_connections_percent=max_connections_percent,
                max_idle_connections_percent=max_idle_connections_percent,
                session_pinning_filters=session_pinning_filters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_borrow_timeout: int | core.IntOut | None = core.arg(default=None)

        init_query: str | core.StringOut | None = core.arg(default=None)

        max_connections_percent: int | core.IntOut | None = core.arg(default=None)

        max_idle_connections_percent: int | core.IntOut | None = core.arg(default=None)

        session_pinning_filters: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_db_proxy_default_target_group", namespace="rds")
class DbProxyDefaultTargetGroup(core.Resource):
    """
    The Amazon Resource Name (ARN) representing the target group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The settings that determine the size and behavior of the connection pool for the target g
    roup.
    """
    connection_pool_config: ConnectionPoolConfig | None = core.attr(
        ConnectionPoolConfig, default=None, computed=True
    )

    """
    (Required) Name of the RDS DB Proxy.
    """
    db_proxy_name: str | core.StringOut = core.attr(str)

    """
    Name of the RDS DB Proxy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the default target group.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        db_proxy_name: str | core.StringOut,
        connection_pool_config: ConnectionPoolConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxyDefaultTargetGroup.Args(
                db_proxy_name=db_proxy_name,
                connection_pool_config=connection_pool_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_pool_config: ConnectionPoolConfig | None = core.arg(default=None)

        db_proxy_name: str | core.StringOut = core.arg()
