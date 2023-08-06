import terrascript.core as core


@core.resource(type="aws_apigatewayv2_api_mapping", namespace="apigatewayv2")
class ApiMapping(core.Resource):
    """
    (Required) The API identifier.
    """

    api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigat
    eway-websocket-api-mapping-template-reference.html).
    """
    api_mapping_key: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The domain name. Use the [`aws_apigatewayv2_domain_name`](/docs/providers/aws/r/apigatewa
    yv2_domain_name.html) resource to configure a domain name.
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    The API mapping identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The API stage. Use the [`aws_apigatewayv2_stage`](/docs/providers/aws/r/apigatewayv2_stag
    e.html) resource to configure an API stage.
    """
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
