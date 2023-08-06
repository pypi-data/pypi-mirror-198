import terrascript.core as core


@core.resource(type="aws_cloudwatch_composite_alarm", namespace="aws_cloudwatch")
class CompositeAlarm(core.Resource):

    actions_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    alarm_description: str | core.StringOut | None = core.attr(str, default=None)

    alarm_name: str | core.StringOut = core.attr(str)

    alarm_rule: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
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
        alarm_name: str | core.StringOut,
        alarm_rule: str | core.StringOut,
        actions_enabled: bool | core.BoolOut | None = None,
        alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        alarm_description: str | core.StringOut | None = None,
        insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CompositeAlarm.Args(
                alarm_name=alarm_name,
                alarm_rule=alarm_rule,
                actions_enabled=actions_enabled,
                alarm_actions=alarm_actions,
                alarm_description=alarm_description,
                insufficient_data_actions=insufficient_data_actions,
                ok_actions=ok_actions,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions_enabled: bool | core.BoolOut | None = core.arg(default=None)

        alarm_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        alarm_description: str | core.StringOut | None = core.arg(default=None)

        alarm_name: str | core.StringOut = core.arg()

        alarm_rule: str | core.StringOut = core.arg()

        insufficient_data_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        ok_actions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
