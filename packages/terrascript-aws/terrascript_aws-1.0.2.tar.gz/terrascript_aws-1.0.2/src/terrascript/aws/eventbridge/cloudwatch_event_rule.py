import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_rule", namespace="aws_eventbridge")
class CloudwatchEventRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    event_bus_name: str | core.StringOut | None = core.attr(str, default=None)

    event_pattern: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    is_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    schedule_expression: str | core.StringOut | None = core.attr(str, default=None)

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
        description: str | core.StringOut | None = None,
        event_bus_name: str | core.StringOut | None = None,
        event_pattern: str | core.StringOut | None = None,
        is_enabled: bool | core.BoolOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        schedule_expression: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventRule.Args(
                description=description,
                event_bus_name=event_bus_name,
                event_pattern=event_pattern,
                is_enabled=is_enabled,
                name=name,
                name_prefix=name_prefix,
                role_arn=role_arn,
                schedule_expression=schedule_expression,
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

        event_bus_name: str | core.StringOut | None = core.arg(default=None)

        event_pattern: str | core.StringOut | None = core.arg(default=None)

        is_enabled: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        schedule_expression: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
