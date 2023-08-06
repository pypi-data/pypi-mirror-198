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


@core.resource(type="aws_sagemaker_code_repository", namespace="sagemaker")
class CodeRepository(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Code Repository.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Code Repository (must be unique).
    """
    code_repository_name: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies details about the repository. see [Git Config](#git-config) details below.
    """
    git_config: GitConfig = core.attr(GitConfig)

    """
    The name of the Code Repository.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

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
