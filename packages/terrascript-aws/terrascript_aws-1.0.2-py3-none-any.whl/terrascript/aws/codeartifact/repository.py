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


@core.resource(type="aws_codeartifact_repository", namespace="aws_codeartifact")
class Repository(core.Resource):

    administrator_account: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    domain: str | core.StringOut = core.attr(str)

    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    external_connections: ExternalConnections | None = core.attr(ExternalConnections, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    repository: str | core.StringOut = core.attr(str)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
