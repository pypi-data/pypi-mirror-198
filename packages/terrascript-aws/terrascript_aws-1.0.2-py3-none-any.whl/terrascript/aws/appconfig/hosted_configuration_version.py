import terrascript.core as core


@core.resource(type="aws_appconfig_hosted_configuration_version", namespace="aws_appconfig")
class HostedConfigurationVersion(core.Resource):

    application_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    configuration_profile_id: str | core.StringOut = core.attr(str)

    content: str | core.StringOut = core.attr(str)

    content_type: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    version_number: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: str | core.StringOut,
        configuration_profile_id: str | core.StringOut,
        content: str | core.StringOut,
        content_type: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=HostedConfigurationVersion.Args(
                application_id=application_id,
                configuration_profile_id=configuration_profile_id,
                content=content,
                content_type=content_type,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: str | core.StringOut = core.arg()

        configuration_profile_id: str | core.StringOut = core.arg()

        content: str | core.StringOut = core.arg()

        content_type: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)
