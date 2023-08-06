import terrascript.core as core


@core.resource(type="aws_db_proxy_endpoint", namespace="rds")
class DbProxyEndpoint(core.Resource):
    """
    The Amazon Resource Name (ARN) for the proxy endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The identifier for the proxy endpoint. An identifier must begin with a letter and must co
    ntain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive
    hyphens.
    """
    db_proxy_endpoint_name: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the DB proxy associated with the DB proxy endpoint that you create.
    """
    db_proxy_name: str | core.StringOut = core.attr(str)

    """
    The endpoint that you can use to connect to the proxy. You include the endpoint value in the connect
    ion string for a database client application.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the proxy and proxy endpoint separated by `/`, `DB-PROXY-NAME/DB-PROXY-ENDPOINT-NAME`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Indicates whether this endpoint is the default endpoint for the associated DB proxy.
    """
    is_default: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) A mapping of tags to assign to the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Indicates whether the DB proxy endpoint can be used for read/write or read-only operation
    s. The default is `READ_WRITE`. Valid values are `READ_WRITE` and `READ_ONLY`.
    """
    target_role: str | core.StringOut | None = core.attr(str, default=None)

    """
    The VPC ID of the DB proxy endpoint.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

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
        db_proxy_endpoint_name: str | core.StringOut,
        db_proxy_name: str | core.StringOut,
        vpc_subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_role: str | core.StringOut | None = None,
        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbProxyEndpoint.Args(
                db_proxy_endpoint_name=db_proxy_endpoint_name,
                db_proxy_name=db_proxy_name,
                vpc_subnet_ids=vpc_subnet_ids,
                tags=tags,
                tags_all=tags_all,
                target_role=target_role,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        db_proxy_endpoint_name: str | core.StringOut = core.arg()

        db_proxy_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_role: str | core.StringOut | None = core.arg(default=None)

        vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpc_subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()
