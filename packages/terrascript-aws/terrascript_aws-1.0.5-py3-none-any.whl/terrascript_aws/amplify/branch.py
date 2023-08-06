import terrascript.core as core


@core.resource(type="aws_amplify_branch", namespace="amplify")
class Branch(core.Resource):
    """
    (Required) The unique ID for an Amplify app.
    """

    app_id: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) for the branch.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of custom resources that are linked to this branch.
    """
    associated_resources: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app.
    """
    backend_environment_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The basic authorization credentials for the branch.
    """
    basic_auth_credentials: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name for the branch.
    """
    branch_name: str | core.StringOut = core.attr(str)

    """
    The custom domains for the branch.
    """
    custom_domains: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The description for the branch.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The destination branch if the branch is a pull request branch.
    """
    destination_branch: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The display name for a branch. This is used as the default domain prefix.
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Enables auto building for the branch.
    """
    enable_auto_build: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables basic authorization for the branch.
    """
    enable_basic_auth: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables notifications for the branch.
    """
    enable_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables performance mode for the branch.
    """
    enable_performance_mode: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables pull request previews for this branch.
    """
    enable_pull_request_preview: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The environment variables for the branch.
    """
    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) The framework for the branch.
    """
    framework: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Amplify environment name for the pull request.
    """
    pull_request_environment_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    The source branch if the branch is a pull request branch.
    """
    source_branch: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Describes the current stage for the branch. Valid values: `PRODUCTION`, `BETA`, `DEVELOPM
    ENT`, `EXPERIMENTAL`, `PULL_REQUEST`.
    """
    stage: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) The content Time To Live (TTL) for the website in seconds.
    """
    ttl: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        app_id: str | core.StringOut,
        branch_name: str | core.StringOut,
        backend_environment_arn: str | core.StringOut | None = None,
        basic_auth_credentials: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        display_name: str | core.StringOut | None = None,
        enable_auto_build: bool | core.BoolOut | None = None,
        enable_basic_auth: bool | core.BoolOut | None = None,
        enable_notification: bool | core.BoolOut | None = None,
        enable_performance_mode: bool | core.BoolOut | None = None,
        enable_pull_request_preview: bool | core.BoolOut | None = None,
        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        framework: str | core.StringOut | None = None,
        pull_request_environment_name: str | core.StringOut | None = None,
        stage: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        ttl: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Branch.Args(
                app_id=app_id,
                branch_name=branch_name,
                backend_environment_arn=backend_environment_arn,
                basic_auth_credentials=basic_auth_credentials,
                description=description,
                display_name=display_name,
                enable_auto_build=enable_auto_build,
                enable_basic_auth=enable_basic_auth,
                enable_notification=enable_notification,
                enable_performance_mode=enable_performance_mode,
                enable_pull_request_preview=enable_pull_request_preview,
                environment_variables=environment_variables,
                framework=framework,
                pull_request_environment_name=pull_request_environment_name,
                stage=stage,
                tags=tags,
                tags_all=tags_all,
                ttl=ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_id: str | core.StringOut = core.arg()

        backend_environment_arn: str | core.StringOut | None = core.arg(default=None)

        basic_auth_credentials: str | core.StringOut | None = core.arg(default=None)

        branch_name: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        enable_auto_build: bool | core.BoolOut | None = core.arg(default=None)

        enable_basic_auth: bool | core.BoolOut | None = core.arg(default=None)

        enable_notification: bool | core.BoolOut | None = core.arg(default=None)

        enable_performance_mode: bool | core.BoolOut | None = core.arg(default=None)

        enable_pull_request_preview: bool | core.BoolOut | None = core.arg(default=None)

        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        framework: str | core.StringOut | None = core.arg(default=None)

        pull_request_environment_name: str | core.StringOut | None = core.arg(default=None)

        stage: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        ttl: str | core.StringOut | None = core.arg(default=None)
