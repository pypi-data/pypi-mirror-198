import terrascript.core as core


@core.schema
class TlsConfig(core.Schema):

    insecure_skip_verification: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        insecure_skip_verification: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=TlsConfig.Args(
                insecure_skip_verification=insecure_skip_verification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insecure_skip_verification: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_api_gateway_integration", namespace="api_gateway")
class Integration(core.Resource):
    """
    (Optional) A list of cache key parameters for the integration.
    """

    cache_key_parameters: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The integration's cache namespace.
    """
    cache_namespace: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The id of the VpcLink used for the integration. **Required** if `connection_type` is `VPC
    _LINK`
    """
    connection_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The integration input's [connectionType](https://docs.aws.amazon.com/apigateway/api-refer
    ence/resource/integration/#connectionType). Valid values are `INTERNET` (default for connections thr
    ough the public routable internet), and `VPC_LINK` (for private connections between API Gateway and
    a network load balancer in a VPC).
    """
    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Specifies how to handle request payload content type conversions. Supported values are `C
    ONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will b
    e passed through from the method request to integration request without modification, provided that
    the passthroughBehaviors is configured to support payload pass-through.
    """
    content_handling: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The credentials required for the integration. For `AWS` integrations, 2 options are avail
    able. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that t
    he caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*
    .
    """
    credentials: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
    """
    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The integration HTTP method
    """
    integration_http_method: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **
    Required** if `request_templates` is used.
    """
    passthrough_behavior: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of request query string parameters and headers that should be passed to the backend
    responder.
    """
    request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A map of the integration's request templates.
    """
    request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The API resource ID.
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the associated REST API.
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 millisecon
    ds.
    """
    timeout_milliseconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Configuration block specifying the TLS configuration for an integration. Defined below.
    """
    tls_config: TlsConfig | None = core.attr(TlsConfig, default=None)

    """
    (Required) The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resou
    rce/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend
    ), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP p
    roxy integration). An `HTTP` or `HTTP_PROXY` integration with a `connection_type` of `VPC_LINK` is r
    eferred to as a private integration and uses a VpcLink to connect API Gateway to a network load bala
    ncer of a VPC.
    """
    type: str | core.StringOut = core.attr(str)

    """
    (Optional) The input's URI. **Required** if `type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`.
    """
    uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        http_method: str | core.StringOut,
        resource_id: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        type: str | core.StringOut,
        cache_key_parameters: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cache_namespace: str | core.StringOut | None = None,
        connection_id: str | core.StringOut | None = None,
        connection_type: str | core.StringOut | None = None,
        content_handling: str | core.StringOut | None = None,
        credentials: str | core.StringOut | None = None,
        integration_http_method: str | core.StringOut | None = None,
        passthrough_behavior: str | core.StringOut | None = None,
        request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout_milliseconds: int | core.IntOut | None = None,
        tls_config: TlsConfig | None = None,
        uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Integration.Args(
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                type=type,
                cache_key_parameters=cache_key_parameters,
                cache_namespace=cache_namespace,
                connection_id=connection_id,
                connection_type=connection_type,
                content_handling=content_handling,
                credentials=credentials,
                integration_http_method=integration_http_method,
                passthrough_behavior=passthrough_behavior,
                request_parameters=request_parameters,
                request_templates=request_templates,
                timeout_milliseconds=timeout_milliseconds,
                tls_config=tls_config,
                uri=uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cache_key_parameters: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        cache_namespace: str | core.StringOut | None = core.arg(default=None)

        connection_id: str | core.StringOut | None = core.arg(default=None)

        connection_type: str | core.StringOut | None = core.arg(default=None)

        content_handling: str | core.StringOut | None = core.arg(default=None)

        credentials: str | core.StringOut | None = core.arg(default=None)

        http_method: str | core.StringOut = core.arg()

        integration_http_method: str | core.StringOut | None = core.arg(default=None)

        passthrough_behavior: str | core.StringOut | None = core.arg(default=None)

        request_parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        request_templates: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        resource_id: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()

        timeout_milliseconds: int | core.IntOut | None = core.arg(default=None)

        tls_config: TlsConfig | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        uri: str | core.StringOut | None = core.arg(default=None)
