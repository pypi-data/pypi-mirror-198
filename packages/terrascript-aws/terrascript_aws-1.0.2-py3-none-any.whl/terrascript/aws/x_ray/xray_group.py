import terrascript.core as core


@core.schema
class InsightsConfiguration(core.Schema):

    insights_enabled: bool | core.BoolOut = core.attr(bool)

    notifications_enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        insights_enabled: bool | core.BoolOut,
        notifications_enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=InsightsConfiguration.Args(
                insights_enabled=insights_enabled,
                notifications_enabled=notifications_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insights_enabled: bool | core.BoolOut = core.arg()

        notifications_enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_xray_group", namespace="aws_x_ray")
class XrayGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    filter_expression: str | core.StringOut = core.attr(str)

    group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    insights_configuration: InsightsConfiguration | None = core.attr(
        InsightsConfiguration, default=None, computed=True
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
        filter_expression: str | core.StringOut,
        group_name: str | core.StringOut,
        insights_configuration: InsightsConfiguration | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=XrayGroup.Args(
                filter_expression=filter_expression,
                group_name=group_name,
                insights_configuration=insights_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        filter_expression: str | core.StringOut = core.arg()

        group_name: str | core.StringOut = core.arg()

        insights_configuration: InsightsConfiguration | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
