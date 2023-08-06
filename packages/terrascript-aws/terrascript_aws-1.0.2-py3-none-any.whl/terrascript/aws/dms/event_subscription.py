import terrascript.core as core


@core.resource(type="aws_dms_event_subscription", namespace="aws_dms")
class EventSubscription(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    event_categories: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    sns_topic_arn: str | core.StringOut = core.attr(str)

    source_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    source_type: str | core.StringOut | None = core.attr(str, default=None)

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
        event_categories: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        sns_topic_arn: str | core.StringOut,
        enabled: bool | core.BoolOut | None = None,
        source_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        source_type: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventSubscription.Args(
                event_categories=event_categories,
                name=name,
                sns_topic_arn=sns_topic_arn,
                enabled=enabled,
                source_ids=source_ids,
                source_type=source_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        event_categories: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        sns_topic_arn: str | core.StringOut = core.arg()

        source_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        source_type: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
