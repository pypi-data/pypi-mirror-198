import terrascript.core as core


@core.resource(type="aws_codeartifact_repository_permissions_policy", namespace="aws_codeartifact")
class RepositoryPermissionsPolicy(core.Resource):

    domain: str | core.StringOut = core.attr(str)

    domain_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    policy_document: str | core.StringOut = core.attr(str)

    policy_revision: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    repository: str | core.StringOut = core.attr(str)

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain: str | core.StringOut,
        policy_document: str | core.StringOut,
        repository: str | core.StringOut,
        domain_owner: str | core.StringOut | None = None,
        policy_revision: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RepositoryPermissionsPolicy.Args(
                domain=domain,
                policy_document=policy_document,
                repository=repository,
                domain_owner=domain_owner,
                policy_revision=policy_revision,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain: str | core.StringOut = core.arg()

        domain_owner: str | core.StringOut | None = core.arg(default=None)

        policy_document: str | core.StringOut = core.arg()

        policy_revision: str | core.StringOut | None = core.arg(default=None)

        repository: str | core.StringOut = core.arg()
