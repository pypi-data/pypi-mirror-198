import terrascript.core as core


@core.resource(type="aws_apigatewayv2_api_mapping", namespace="aws_apigatewayv2")
class ApiMapping(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    api_mapping_key: str | core.StringOut | None = core.attr(str, default=None)

    domain_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    stage: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        domain_name: str | core.StringOut,
        stage: str | core.StringOut,
        api_mapping_key: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApiMapping.Args(
                api_id=api_id,
                domain_name=domain_name,
                stage=stage,
                api_mapping_key=api_mapping_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        api_mapping_key: str | core.StringOut | None = core.arg(default=None)

        domain_name: str | core.StringOut = core.arg()

        stage: str | core.StringOut = core.arg()
