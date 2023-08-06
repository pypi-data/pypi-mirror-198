import terrascript.core as core


@core.schema
class IpAddress(core.Schema):

    ip: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ip_id: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        ip_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
        ip: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=IpAddress.Args(
                ip_id=ip_id,
                subnet_id=subnet_id,
                ip=ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip: str | core.StringOut | None = core.arg(default=None)

        ip_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.resource(type="aws_route53_resolver_endpoint", namespace="aws_route53_resolver")
class Endpoint(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    direction: str | core.StringOut = core.attr(str)

    host_vpc_id: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    ip_address: list[IpAddress] | core.ArrayOut[IpAddress] = core.attr(
        IpAddress, kind=core.Kind.array
    )

    name: str | core.StringOut | None = core.attr(str, default=None)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        direction: str | core.StringOut,
        ip_address: list[IpAddress] | core.ArrayOut[IpAddress],
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                direction=direction,
                ip_address=ip_address,
                security_group_ids=security_group_ids,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        direction: str | core.StringOut = core.arg()

        ip_address: list[IpAddress] | core.ArrayOut[IpAddress] = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
