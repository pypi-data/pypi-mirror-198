import terrascript.core as core


@core.resource(type="aws_amplify_branch", namespace="aws_amplify")
class Branch(core.Resource):

    app_id: str | core.StringOut = core.attr(str)

    arn: str | core.StringOut = core.attr(str, computed=True)

    associated_resources: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    backend_environment_arn: str | core.StringOut | None = core.attr(str, default=None)

    basic_auth_credentials: str | core.StringOut | None = core.attr(str, default=None)

    branch_name: str | core.StringOut = core.attr(str)

    custom_domains: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    destination_branch: str | core.StringOut = core.attr(str, computed=True)

    display_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enable_auto_build: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_basic_auth: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_notification: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_performance_mode: bool | core.BoolOut | None = core.attr(bool, default=None)

    enable_pull_request_preview: bool | core.BoolOut | None = core.attr(bool, default=None)

    environment_variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    framework: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    pull_request_environment_name: str | core.StringOut | None = core.attr(str, default=None)

    source_branch: str | core.StringOut = core.attr(str, computed=True)

    stage: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
