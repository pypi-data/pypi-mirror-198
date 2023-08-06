import terrascript.core as core


@core.resource(type="aws_ecr_pull_through_cache_rule", namespace="ecr")
class PullThroughCacheRule(core.Resource):
    """
    (Required, Forces new resource) The repository name prefix to use when caching images from the sourc
    e registry.
    """

    ecr_repository_prefix: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The registry ID where the repository was created.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The registry URL of the upstream public registry to use as the sourc
    e.
    """
    upstream_registry_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ecr_repository_prefix: str | core.StringOut,
        upstream_registry_url: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PullThroughCacheRule.Args(
                ecr_repository_prefix=ecr_repository_prefix,
                upstream_registry_url=upstream_registry_url,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ecr_repository_prefix: str | core.StringOut = core.arg()

        upstream_registry_url: str | core.StringOut = core.arg()
