import terrascript.core as core


@core.schema
class ExternalConnections(core.Schema):

    external_connection_name: str | core.StringOut = core.attr(str)

    package_format: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        external_connection_name: str | core.StringOut,
        package_format: str | core.StringOut,
        status: str | core.StringOut,
    ):
        super().__init__(
            args=ExternalConnections.Args(
                external_connection_name=external_connection_name,
                package_format=package_format,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        external_connection_name: str | core.StringOut = core.arg()

        package_format: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()


@core.schema
class Upstream(core.Schema):

    repository_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        repository_name: str | core.StringOut,
    ):
        super().__init__(
            args=Upstream.Args(
                repository_name=repository_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: str | core.StringOut = core.arg()


@core.resource(type="aws_codeartifact_repository", namespace="codeartifact")
class Repository(core.Resource):
    """
    The account number of the AWS account that manages the repository.
    """

    administrator_account: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the repository.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the repository.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The domain that contains the created repository.
    """
    domain: str | core.StringOut = core.attr(str)

    """
    (Optional) The account number of the AWS account that owns the domain.
    """
    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    An array of external connections associated with the repository. Only one external connection can be
    set per repository. see [External Connections](#external-connections).
    """
    external_connections: ExternalConnections | None = core.attr(ExternalConnections, default=None)

    """
    The ARN of the repository.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the repository to create.
    """
    repository: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    (Optional) A list of upstream repositories to associate with the repository. The order of the upstre
    am repositories in the list determines their priority order when AWS CodeArtifact looks for a reques
    ted package version. see [Upstream](#upstream)
    """
    upstream: list[Upstream] | core.ArrayOut[Upstream] | None = core.attr(
        Upstream, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        repository: str | core.StringOut,
        description: str | core.StringOut | None = None,
        domain_owner: str | core.StringOut | None = None,
        external_connections: ExternalConnections | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        upstream: list[Upstream] | core.ArrayOut[Upstream] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Repository.Args(
                domain=domain,
                repository=repository,
                description=description,
                domain_owner=domain_owner,
                external_connections=external_connections,
                tags=tags,
                tags_all=tags_all,
                upstream=upstream,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        domain: str | core.StringOut = core.arg()

        domain_owner: str | core.StringOut | None = core.arg(default=None)

        external_connections: ExternalConnections | None = core.arg(default=None)

        repository: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        upstream: list[Upstream] | core.ArrayOut[Upstream] | None = core.arg(default=None)
