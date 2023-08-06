import terrascript.core as core


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


@core.resource(type="aws_amplify_app", namespace="aws_amplify")
class App(core.Resource):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    auto_branch_creation_config: AutoBranchCreationConfig | None = core.attr(
        AutoBranchCreationConfig, default=None, computed=True
    )

    auto_branch_creation_patterns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    basic_auth_credentials: str | core.StringOut | None = core.attr(str, default=None)

    build_spec: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    custom_rule: list[CustomRule] | core.ArrayOut[CustomRule] | None = core.attr(
        CustomRule, default=None, kind=core.Kind.array
    )

    default_domain: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    enable_auto_branch_creation: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_basic_auth: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_branch_auto_build: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_branch_auto_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    iam_service_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    oauth_token: str | core.StringOut | None = core.attr(str, default=None)

    platform: str | core.StringOut | None = core.attr(str, default=None)

    production_branch: list[ProductionBranch] | core.ArrayOut[ProductionBranch] = core.attr(
        ProductionBranch, computed=True, kind=core.Kind.array
    )

    repository: str | core.StringOut | None = core.attr(str, default=None)

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
