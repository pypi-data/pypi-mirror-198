import terrascript.core as core


@core.data(type="aws_codeartifact_repository_endpoint", namespace="aws_codeartifact")
class DsRepositoryEndpoint(core.Data):

    domain: str | core.StringOut = core.attr(str)

    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    format: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    repository: str | core.StringOut = core.attr(str)

    repository_endpoint: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        domain: str | core.StringOut,
        format: str | core.StringOut,
        repository: str | core.StringOut,
        domain_owner: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRepositoryEndpoint.Args(
                domain=domain,
                format=format,
                repository=repository,
                domain_owner=domain_owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: str | core.StringOut = core.arg()

        domain_owner: str | core.StringOut | None = core.arg(default=None)

        format: str | core.StringOut = core.arg()

        repository: str | core.StringOut = core.arg()
