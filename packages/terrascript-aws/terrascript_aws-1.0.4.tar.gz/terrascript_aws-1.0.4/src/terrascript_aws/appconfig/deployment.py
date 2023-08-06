import terrascript.core as core


@core.resource(type="aws_appconfig_deployment", namespace="appconfig")
class Deployment(core.Resource):
    """
    (Required, Forces new resource) The application ID. Must be between 4 and 7 characters in length.
    """

    application_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the AppConfig Deployment.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The configuration profile ID. Must be between 4 and 7 characters in
    length.
    """
    configuration_profile_id: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The configuration version to deploy. Can be at most 1024 characters.
    """
    configuration_version: str | core.StringOut = core.attr(str)

    """
    The deployment number.
    """
    deployment_number: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required, Forces new resource) The deployment strategy ID or name of a predefined deployment strate
    gy. See [Predefined Deployment Strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/ap
    pconfig-creating-deployment-strategy.html#appconfig-creating-deployment-strategy-predefined) for mor
    e details.
    """
    deployment_strategy_id: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The description of the deployment. Can be at most 1024 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, Forces new resource) The environment ID. Must be between 4 and 7 characters in length.
    """
    environment_id: str | core.StringOut = core.attr(str)

    """
    The AppConfig application ID, environment ID, and deployment number separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the deployment.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
