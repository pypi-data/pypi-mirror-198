import terrascript.core as core


@core.resource(type="aws_api_gateway_deployment", namespace="aws_api_gateway")
class Deployment(core.Resource):

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    invoke_url: str | core.StringOut = core.attr(str, computed=True)

    rest_api_id: str | core.StringOut = core.attr(str)

    stage_description: str | core.StringOut | None = core.attr(str, default=None)

    stage_name: str | core.StringOut | None = core.attr(str, default=None)

    triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        rest_api_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        stage_description: str | core.StringOut | None = None,
        stage_name: str | core.StringOut | None = None,
        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        variables: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                rest_api_id=rest_api_id,
                description=description,
                stage_description=stage_description,
                stage_name=stage_name,
                triggers=triggers,
                variables=variables,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        stage_description: str | core.StringOut | None = core.arg(default=None)

        stage_name: str | core.StringOut | None = core.arg(default=None)

        triggers: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        variables: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
