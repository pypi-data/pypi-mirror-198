import terrascript.core as core


@core.schema
class Vpc(core.Schema):

    vpc_id: str | core.StringOut = core.attr(str)

    vpc_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        vpc_id: str | core.StringOut,
        vpc_region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Vpc.Args(
                vpc_id=vpc_id,
                vpc_region=vpc_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_id: str | core.StringOut = core.arg()

        vpc_region: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_route53_zone", namespace="aws_route53")
class Zone(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    comment: str | core.StringOut | None = core.attr(str, default=None)

    delegation_set_id: str | core.StringOut | None = core.attr(str, default=None)

    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc: list[Vpc] | core.ArrayOut[Vpc] | None = core.attr(Vpc, default=None, kind=core.Kind.array)

    zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        delegation_set_id: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc: list[Vpc] | core.ArrayOut[Vpc] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Zone.Args(
                name=name,
                comment=comment,
                delegation_set_id=delegation_set_id,
                force_destroy=force_destroy,
                tags=tags,
                tags_all=tags_all,
                vpc=vpc,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        delegation_set_id: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc: list[Vpc] | core.ArrayOut[Vpc] | None = core.arg(default=None)
