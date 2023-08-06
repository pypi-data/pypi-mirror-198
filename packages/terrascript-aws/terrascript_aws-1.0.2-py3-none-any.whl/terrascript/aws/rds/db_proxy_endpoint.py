import terrascript.core as core


@core.resource(type="aws_db_proxy_endpoint", namespace="aws_rds")
class DbProxyEndpoint(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    db_proxy_endpoint_name: str | core.StringOut = core.attr(str)

    db_proxy_name: str | core.StringOut = core.attr(str)

    endpoint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    is_default: bool | core.BoolOut = core.attr(bool, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_role: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    vpc_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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
