import terrascript.core as core


@core.resource(type="aws_api_gateway_base_path_mapping", namespace="aws_api_gateway")
class BasePathMapping(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    base_path: str | core.StringOut | None = core.attr(str, default=None)

    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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
