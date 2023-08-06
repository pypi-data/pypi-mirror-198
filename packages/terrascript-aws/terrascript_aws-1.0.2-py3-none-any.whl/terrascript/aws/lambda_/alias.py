import terrascript.core as core


@core.schema
class RoutingConfig(core.Schema):

    additional_version_weights: dict[str, float] | core.MapOut[core.FloatOut] | None = core.attr(
        float, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        additional_version_weights: dict[str, float] | core.MapOut[core.FloatOut] | None = None,
    ):
        super().__init__(
            args=RoutingConfig.Args(
                additional_version_weights=additional_version_weights,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_version_weights: dict[str, float] | core.MapOut[core.FloatOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_lambda_alias", namespace="aws_lambda_")
class Alias(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    function_name: str | core.StringOut = core.attr(str)

    function_version: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    routing_config: RoutingConfig | None = core.attr(RoutingConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: str | core.StringOut,
        function_version: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        routing_config: RoutingConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Alias.Args(
                function_name=function_name,
                function_version=function_version,
                name=name,
                description=description,
                routing_config=routing_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        function_name: str | core.StringOut = core.arg()

        function_version: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        routing_config: RoutingConfig | None = core.arg(default=None)
