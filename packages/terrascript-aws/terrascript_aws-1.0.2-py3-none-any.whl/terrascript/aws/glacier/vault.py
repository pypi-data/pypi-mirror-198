import terrascript.core as core


@core.schema
class Notification(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    sns_topic: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut],
        sns_topic: str | core.StringOut,
    ):
        super().__init__(
            args=Notification.Args(
                events=events,
                sns_topic=sns_topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        sns_topic: str | core.StringOut = core.arg()


@core.resource(type="aws_glacier_vault", namespace="aws_glacier")
class Vault(core.Resource):

    access_policy: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    location: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    notification: Notification | None = core.attr(Notification, default=None)

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
        name: str | core.StringOut,
        access_policy: str | core.StringOut | None = None,
        notification: Notification | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Vault.Args(
                name=name,
                access_policy=access_policy,
                notification=notification,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policy: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        notification: Notification | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
