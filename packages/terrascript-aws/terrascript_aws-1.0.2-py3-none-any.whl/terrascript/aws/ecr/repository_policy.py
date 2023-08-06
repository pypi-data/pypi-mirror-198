import terrascript.core as core


@core.resource(type="aws_ecr_repository_policy", namespace="aws_ecr")
class RepositoryPolicy(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut = core.attr(str)

    registry_id: str | core.StringOut = core.attr(str, computed=True)

    repository: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: str | core.StringOut,
        repository: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RepositoryPolicy.Args(
                policy=policy,
                repository=repository,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: str | core.StringOut = core.arg()

        repository: str | core.StringOut = core.arg()
