import terrascript.core as core


@core.resource(type="aws_api_gateway_base_path_mapping", namespace="api_gateway")
class BasePathMapping(core.Resource):
    """
    (Required) The id of the API to connect.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Path segment that must be prepended to the path when accessing the API via this mapping.
    If omitted, the API is exposed at the root of the given domain.
    """
    base_path: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The already-registered domain name to connect the API to.
    """
    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of a specific deployment stage to expose at the given path. If omitted, callers
    may select any stage by including its name as a path element after the base path.
    """
    stage_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        domain_name: str | core.StringOut,
        base_path: str | core.StringOut | None = None,
        stage_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BasePathMapping.Args(
                api_id=api_id,
                domain_name=domain_name,
                base_path=base_path,
                stage_name=stage_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        base_path: str | core.StringOut | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()

        stage_name: str | core.StringOut | None = core.arg(default=None)
