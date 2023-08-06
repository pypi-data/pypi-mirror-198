import terrascript.core as core


@core.schema
class GitConfig(core.Schema):

    branch: str | core.StringOut | None = core.attr(str, default=None)

    repository_url: str | core.StringOut = core.attr(str)

    secret_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        repository_url: str | core.StringOut,
        branch: str | core.StringOut | None = None,
        secret_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=GitConfig.Args(
                repository_url=repository_url,
                branch=branch,
                secret_arn=secret_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        branch: str | core.StringOut | None = core.arg(default=None)

        repository_url: str | core.StringOut = core.arg()

        secret_arn: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_sagemaker_code_repository", namespace="aws_sagemaker")
class CodeRepository(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    code_repository_name: str | core.StringOut = core.attr(str)

    git_config: GitConfig = core.attr(GitConfig)

    id: str | core.StringOut = core.attr(str, computed=True)

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
        code_repository_name: str | core.StringOut,
        git_config: GitConfig,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CodeRepository.Args(
                code_repository_name=code_repository_name,
                git_config=git_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        code_repository_name: str | core.StringOut = core.arg()

        git_config: GitConfig = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
