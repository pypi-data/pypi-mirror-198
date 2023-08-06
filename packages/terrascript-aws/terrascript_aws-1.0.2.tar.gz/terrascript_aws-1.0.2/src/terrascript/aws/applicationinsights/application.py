import terrascript.core as core


@core.resource(type="aws_applicationinsights_application", namespace="aws_applicationinsights")
class Application(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_config_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    auto_create: bool | core.BoolOut | None = core.attr(bool, default=None)

    cwe_monitor_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    grouping_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ops_center_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    ops_item_sns_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    resource_group_name: str | core.StringOut = core.attr(str)

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
        resource_group_name: str | core.StringOut,
        auto_config_enabled: bool | core.BoolOut | None = None,
        auto_create: bool | core.BoolOut | None = None,
        cwe_monitor_enabled: bool | core.BoolOut | None = None,
        grouping_type: str | core.StringOut | None = None,
        ops_center_enabled: bool | core.BoolOut | None = None,
        ops_item_sns_topic_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                resource_group_name=resource_group_name,
                auto_config_enabled=auto_config_enabled,
                auto_create=auto_create,
                cwe_monitor_enabled=cwe_monitor_enabled,
                grouping_type=grouping_type,
                ops_center_enabled=ops_center_enabled,
                ops_item_sns_topic_arn=ops_item_sns_topic_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_config_enabled: bool | core.BoolOut | None = core.arg(default=None)

        auto_create: bool | core.BoolOut | None = core.arg(default=None)

        cwe_monitor_enabled: bool | core.BoolOut | None = core.arg(default=None)

        grouping_type: str | core.StringOut | None = core.arg(default=None)

        ops_center_enabled: bool | core.BoolOut | None = core.arg(default=None)

        ops_item_sns_topic_arn: str | core.StringOut | None = core.arg(default=None)

        resource_group_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
