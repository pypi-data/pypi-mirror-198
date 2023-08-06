import terrascript.core as core


@core.schema
class Ingress(core.Schema):

    cidr: str | core.StringOut | None = core.attr(str, default=None)

    security_group_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    security_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    security_group_owner_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cidr: str | core.StringOut | None = None,
        security_group_id: str | core.StringOut | None = None,
        security_group_name: str | core.StringOut | None = None,
        security_group_owner_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Ingress.Args(
                cidr=cidr,
                security_group_id=security_group_id,
                security_group_name=security_group_name,
                security_group_owner_id=security_group_owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut | None = core.arg(default=None)

        security_group_id: str | core.StringOut | None = core.arg(default=None)

        security_group_name: str | core.StringOut | None = core.arg(default=None)

        security_group_owner_id: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_db_security_group", namespace="aws_rds")
class DbSecurityGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ingress: list[Ingress] | core.ArrayOut[Ingress] = core.attr(Ingress, kind=core.Kind.array)

    name: str | core.StringOut = core.attr(str)

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
        ingress: list[Ingress] | core.ArrayOut[Ingress],
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSecurityGroup.Args(
                ingress=ingress,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        ingress: list[Ingress] | core.ArrayOut[Ingress] = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
