import terrascript.core as core


@core.resource(type="aws_appconfig_deployment", namespace="aws_appconfig")
class Deployment(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    configuration_profile_id: str | core.StringOut = core.attr(str)

    configuration_version: str | core.StringOut = core.attr(str)

    deployment_number: int | core.IntOut = core.attr(int, computed=True)

    deployment_strategy_id: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    environment_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

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
        application_id: str | core.StringOut,
        configuration_profile_id: str | core.StringOut,
        configuration_version: str | core.StringOut,
        deployment_strategy_id: str | core.StringOut,
        environment_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                application_id=application_id,
                configuration_profile_id=configuration_profile_id,
                configuration_version=configuration_version,
                deployment_strategy_id=deployment_strategy_id,
                environment_id=environment_id,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        configuration_profile_id: str | core.StringOut = core.arg()

        configuration_version: str | core.StringOut = core.arg()

        deployment_strategy_id: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        environment_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
