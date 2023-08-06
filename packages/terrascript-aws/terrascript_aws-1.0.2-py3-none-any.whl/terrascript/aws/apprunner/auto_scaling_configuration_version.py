import terrascript.core as core


@core.resource(type="aws_apprunner_auto_scaling_configuration_version", namespace="aws_apprunner")
class AutoScalingConfigurationVersion(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_scaling_configuration_name: str | core.StringOut = core.attr(str)

    auto_scaling_configuration_revision: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    latest: bool | core.BoolOut = core.attr(bool, computed=True)

    max_concurrency: int | core.IntOut | None = core.attr(int, default=None)

    max_size: int | core.IntOut | None = core.attr(int, default=None)

    min_size: int | core.IntOut | None = core.attr(int, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

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
        auto_scaling_configuration_name: str | core.StringOut,
        max_concurrency: int | core.IntOut | None = None,
        max_size: int | core.IntOut | None = None,
        min_size: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AutoScalingConfigurationVersion.Args(
                auto_scaling_configuration_name=auto_scaling_configuration_name,
                max_concurrency=max_concurrency,
                max_size=max_size,
                min_size=min_size,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_configuration_name: str | core.StringOut = core.arg()

        max_concurrency: int | core.IntOut | None = core.arg(default=None)

        max_size: int | core.IntOut | None = core.arg(default=None)

        min_size: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
