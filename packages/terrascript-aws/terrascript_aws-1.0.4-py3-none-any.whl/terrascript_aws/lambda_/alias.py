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


@core.resource(type="aws_lambda_alias", namespace="lambda_")
class Alias(core.Resource):
    """
    The Amazon Resource Name (ARN) identifying your Lambda function alias.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the alias.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Lambda Function name or ARN.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    (Required) Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)
    .
    """
    function_version: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_i
    ntegration`](/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
    """
    invoke_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The Lambda alias' route configuration settings. Fields documented below
    """
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
