import terrascript.core as core


@core.resource(type="aws_sagemaker_studio_lifecycle_config", namespace="sagemaker")
class StudioLifecycleConfig(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    studio_lifecycle_config_app_type: str | core.StringOut = core.attr(str)

    studio_lifecycle_config_content: str | core.StringOut = core.attr(str)

    studio_lifecycle_config_name: str | core.StringOut = core.attr(str)

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
        studio_lifecycle_config_app_type: str | core.StringOut,
        studio_lifecycle_config_content: str | core.StringOut,
        studio_lifecycle_config_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=StudioLifecycleConfig.Args(
                studio_lifecycle_config_app_type=studio_lifecycle_config_app_type,
                studio_lifecycle_config_content=studio_lifecycle_config_content,
                studio_lifecycle_config_name=studio_lifecycle_config_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        studio_lifecycle_config_app_type: str | core.StringOut = core.arg()

        studio_lifecycle_config_content: str | core.StringOut = core.arg()

        studio_lifecycle_config_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
