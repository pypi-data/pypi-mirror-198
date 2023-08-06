import terrascript.core as core


@core.schema
class Target(core.Schema):

    address: str | core.StringOut = core.attr(str)

    status: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        status: str | core.StringOut,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Target.Args(
                address=address,
                status=status,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)


@core.resource(
    type="aws_codestarnotifications_notification_rule", namespace="codestarnotifications"
)
class NotificationRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    detail_type: str | core.StringOut = core.attr(str)

    event_type_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    resource: str | core.StringOut = core.attr(str)

    status: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target: list[Target] | core.ArrayOut[Target] | None = core.attr(
        Target, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        detail_type: str | core.StringOut,
        event_type_ids: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        resource: str | core.StringOut,
        status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target: list[Target] | core.ArrayOut[Target] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NotificationRule.Args(
                detail_type=detail_type,
                event_type_ids=event_type_ids,
                name=name,
                resource=resource,
                status=status,
                tags=tags,
                tags_all=tags_all,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        detail_type: str | core.StringOut = core.arg()

        event_type_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        resource: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target: list[Target] | core.ArrayOut[Target] | None = core.arg(default=None)
