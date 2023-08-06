import terrascript.core as core


@core.resource(type="aws_appconfig_hosted_configuration_version", namespace="appconfig")
class HostedConfigurationVersion(core.Resource):
    """
    (Required, Forces new resource) The application ID.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the AppConfig  hosted configuration version.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The configuration profile ID.
    """
    configuration_profile_id: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The content of the configuration or the configuration data.
    """
    content: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) A standard MIME type describing the format of the configuration cont
    ent. For more information, see [Content-Type](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.htm
    l#sec14.17).
    """
    content_type: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) A description of the configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The AppConfig application ID, configuration profile ID, and version number separated by a slash (`/`
    ).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The version number of the hosted configuration.
    """
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
