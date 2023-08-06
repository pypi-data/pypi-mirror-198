import terrascript.core as core


@core.schema
class CustomRule(core.Schema):

    condition: str | core.StringOut | None = core.attr(str, default=None)

    source: str | core.StringOut = core.attr(str)

    status: str | core.StringOut | None = core.attr(str, default=None)

    target: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        source: str | core.StringOut,
        target: str | core.StringOut,
        condition: str | core.StringOut | None = None,
        status: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomRule.Args(
                source=source,
                target=target,
                condition=condition,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        condition: str | core.StringOut | None = core.arg(default=None)

        source: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)

        target: str | core.StringOut = core.arg()


@core.schema
class ProductionBranch(core.Schema):

    branch_name: str | core.StringOut = core.attr(str, computed=True)

    last_deploy_time: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    thumbnail_url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        branch_name: str | core.StringOut,
        last_deploy_time: str | core.StringOut,
        status: str | core.StringOut,
        thumbnail_url: str | core.StringOut,
    ):
        super().__init__(
            args=ProductionBranch.Args(
                branch_name=branch_name,
                last_deploy_time=last_deploy_time,
                status=status,
                thumbnail_url=thumbnail_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branch_name: str | core.StringOut = core.arg()

        last_deploy_time: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

        thumbnail_url: str | core.StringOut = core.arg()


@core.schema
class AutoBranchCreationConfig(core.Schema):

    basic_auth_credentials: str | core.StringOut | None = core.attr(str, default=None)

    build_spec: str | core.StringOut | None = core.attr(str, default=None)

    enable_auto_build: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_basic_auth: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_performance_mode: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_pull_request_preview: bool | core.BoolOut | None = core.attr(bool, default=None)

    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    framework: str | core.StringOut | None = core.attr(str, default=None)

    pull_request_environment_name: str | core.StringOut | None = core.attr(str, default=None)

    stage: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        basic_auth_credentials: str | core.StringOut | None = None,
        build_spec: str | core.StringOut | None = None,
        enable_auto_build: bool | core.BoolOut | None = None,
        enable_basic_auth: bool | core.BoolOut | None = None,
        enable_performance_mode: bool | core.BoolOut | None = None,
        enable_pull_request_preview: bool | core.BoolOut | None = None,
        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        framework: str | core.StringOut | None = None,
        pull_request_environment_name: str | core.StringOut | None = None,
        stage: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AutoBranchCreationConfig.Args(
                basic_auth_credentials=basic_auth_credentials,
                build_spec=build_spec,
                enable_auto_build=enable_auto_build,
                enable_basic_auth=enable_basic_auth,
                enable_performance_mode=enable_performance_mode,
                enable_pull_request_preview=enable_pull_request_preview,
                environment_variables=environment_variables,
                framework=framework,
                pull_request_environment_name=pull_request_environment_name,
                stage=stage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        basic_auth_credentials: str | core.StringOut | None = core.arg(default=None)

        build_spec: str | core.StringOut | None = core.arg(default=None)

        enable_auto_build: bool | core.BoolOut | None = core.arg(default=None)

        enable_basic_auth: bool | core.BoolOut | None = core.arg(default=None)

        enable_performance_mode: bool | core.BoolOut | None = core.arg(default=None)

        enable_pull_request_preview: bool | core.BoolOut | None = core.arg(default=None)

        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        framework: str | core.StringOut | None = core.arg(default=None)

        pull_request_environment_name: str | core.StringOut | None = core.arg(default=None)

        stage: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_amplify_app", namespace="amplify")
class App(core.Resource):
    """
    (Optional) The personal access token for a third-party source control system for an Amplify app. The
    personal access token is used to create a webhook and a read-only deploy key. The token is not stor
    ed.
    """

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Name (ARN) of the Amplify app.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The automated branch creation configuration for an Amplify app. An `auto_branch_creation_
    config` block is documented below.
    """
    auto_branch_creation_config: AutoBranchCreationConfig | None = core.attr(
        AutoBranchCreationConfig, default=None, computed=True
    )

    """
    (Optional) The automated branch creation glob patterns for an Amplify app.
    """
    auto_branch_creation_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The credentials for basic authorization for an Amplify app.
    """
    basic_auth_credentials: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The [build specification](https://docs.aws.amazon.com/amplify/latest/userguide/build-sett
    ings.html) (build spec) for an Amplify app.
    """
    build_spec: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The custom rewrite and redirect rules for an Amplify app. A `custom_rule` block is docume
    nted below.
    """
    custom_rule: list[CustomRule] | core.ArrayOut[CustomRule] | None = core.attr(
        CustomRule, default=None, kind=core.Kind.array
    )

    """
    The default domain for the Amplify app.
    """
    default_domain: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description for an Amplify app.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Enables automated branch creation for an Amplify app.
    """
    enable_auto_branch_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables basic authorization for an Amplify app. This will apply to all branches that are
    part of this app.
    """
    enable_basic_auth: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Enables auto-building of branches for the Amplify App.
    """
    enable_branch_auto_build: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Automatically disconnects a branch in the Amplify Console when you delete a branch from y
    our Git repository.
    """
    enable_branch_auto_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The environment variables map for an Amplify app.
    """
    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) The AWS Identity and Access Management (IAM) service role for an Amplify app.
    """
    iam_service_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique ID of the Amplify app.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for an Amplify app.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The OAuth token for a third-party source control system for an Amplify app. The OAuth tok
    en is used to create a webhook and a read-only deploy key. The OAuth token is not stored.
    """
    oauth_token: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The platform or framework for an Amplify app. Valid values: `WEB`.
    """
    platform: str | core.StringOut | None = core.attr(str, default=None)

    """
    Describes the information about a production branch for an Amplify app. A `production_branch` block
    is documented below.
    """
    production_branch: list[ProductionBranch] | core.ArrayOut[ProductionBranch] = core.attr(
        ProductionBranch, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The repository for an Amplify app.
    """
    repository: str | core.StringOut | None = core.attr(str, default=None)

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

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        access_token: str | core.StringOut | None = None,
        auto_branch_creation_config: AutoBranchCreationConfig | None = None,
        auto_branch_creation_patterns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        basic_auth_credentials: str | core.StringOut | None = None,
        build_spec: str | core.StringOut | None = None,
        custom_rule: list[CustomRule] | core.ArrayOut[CustomRule] | None = None,
        description: str | core.StringOut | None = None,
        enable_auto_branch_creation: bool | core.BoolOut | None = None,
        enable_basic_auth: bool | core.BoolOut | None = None,
        enable_branch_auto_build: bool | core.BoolOut | None = None,
        enable_branch_auto_deletion: bool | core.BoolOut | None = None,
        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        iam_service_role_arn: str | core.StringOut | None = None,
        oauth_token: str | core.StringOut | None = None,
        platform: str | core.StringOut | None = None,
        repository: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=App.Args(
                name=name,
                access_token=access_token,
                auto_branch_creation_config=auto_branch_creation_config,
                auto_branch_creation_patterns=auto_branch_creation_patterns,
                basic_auth_credentials=basic_auth_credentials,
                build_spec=build_spec,
                custom_rule=custom_rule,
                description=description,
                enable_auto_branch_creation=enable_auto_branch_creation,
                enable_basic_auth=enable_basic_auth,
                enable_branch_auto_build=enable_branch_auto_build,
                enable_branch_auto_deletion=enable_branch_auto_deletion,
                environment_variables=environment_variables,
                iam_service_role_arn=iam_service_role_arn,
                oauth_token=oauth_token,
                platform=platform,
                repository=repository,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_token: str | core.StringOut | None = core.arg(default=None)

        auto_branch_creation_config: AutoBranchCreationConfig | None = core.arg(default=None)

        auto_branch_creation_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        basic_auth_credentials: str | core.StringOut | None = core.arg(default=None)

        build_spec: str | core.StringOut | None = core.arg(default=None)

        custom_rule: list[CustomRule] | core.ArrayOut[CustomRule] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        enable_auto_branch_creation: bool | core.BoolOut | None = core.arg(default=None)

        enable_basic_auth: bool | core.BoolOut | None = core.arg(default=None)

        enable_branch_auto_build: bool | core.BoolOut | None = core.arg(default=None)

        enable_branch_auto_deletion: bool | core.BoolOut | None = core.arg(default=None)

        environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        iam_service_role_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        oauth_token: str | core.StringOut | None = core.arg(default=None)

        platform: str | core.StringOut | None = core.arg(default=None)

        repository: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
