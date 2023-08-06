import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_endpoint_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: list[str] | core.ArrayOut[core.StringOut],
        vpc_endpoint_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                types=types,
                vpc_endpoint_ids=vpc_endpoint_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        types: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_endpoint_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_api_gateway_rest_api", namespace="api_gateway")
class RestApi(core.Resource):
    """
    (Optional) Source of the API key for requests. Valid values are `HEADER` (default) and `AUTHORIZER`.
    If importing an OpenAPI specification via the `body` argument, this corresponds to the [`x-amazon-a
    pigateway-api-key-source` extension](https://docs.aws.amazon.com/apigateway/latest/developerguide/ap
    i-gateway-swagger-extensions-api-key-source.html). If the argument value is provided and is differen
    t than the OpenAPI value, the argument value will override the OpenAPI value.
    """

    api_key_source: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN)
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of binary media types supported by the REST API. By default, the REST API supports o
    nly UTF-8-encoded text payloads. If importing an OpenAPI specification via the `body` argument, this
    corresponds to the [`x-amazon-apigateway-binary-media-types` extension](https://docs.aws.amazon.com
    /apigateway/latest/developerguide/api-gateway-swagger-extensions-binary-media-types.html). If the ar
    gument value is provided and is different than the OpenAPI value, the argument value will override t
    he OpenAPI value.
    """
    binary_media_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) OpenAPI specification that defines the set of routes and integrations to create as part o
    f the REST API. This configuration, and any updates to it, will replace all REST API configuration e
    xcept values overridden in this resource configuration and other resource updates applied after this
    resource but before any `aws_api_gateway_deployment` creation. More information about REST API Open
    API support can be found in the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway
    /latest/developerguide/api-gateway-import-api.html).
    """
    body: str | core.StringOut | None = core.attr(str, default=None)

    """
    The creation date of the REST API
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the REST API. If importing an OpenAPI specification via the `body` argumen
    t, this corresponds to the `info.description` field. If the argument value is provided and is differ
    ent than the OpenAPI value, the argument value will override the OpenAPI value.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies whether clients can invoke your API by using the default execute-api endpoint.
    By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazo
    naws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the
    default endpoint. Defaults to `false`. If importing an OpenAPI specification via the `body` argument
    , this corresponds to the [`x-amazon-apigateway-endpoint-configuration` extension `disableExecuteApi
    Endpoint` property](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger
    extensions-endpoint-configuration.html). If the argument value is `true` and is different than the
    OpenAPI value, the argument value will override the OpenAPI value.
    """
    disable_execute_api_endpoint: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Configuration block defining API endpoint configuration including endpoint type. Defined
    below.
    """
    endpoint_configuration: EndpointConfiguration | None = core.attr(
        EndpointConfiguration, default=None, computed=True
    )

    """
    The execution ARN part to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.h
    tml)'s `source_arn`
    """
    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the REST API
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Minimum response size to compress for the REST API. Integer between `-1` and `10485760` (
    10MB). Setting a value greater than `-1` will enable compression, `-1` disables compression (default
    ). If importing an OpenAPI specification via the `body` argument, this corresponds to the [`x-amazon
    apigateway-minimum-compression-size` extension](https://docs.aws.amazon.com/apigateway/latest/devel
    operguide/api-gateway-openapi-minimum-compression-size.html). If the argument value (_except_ `-1`)
    is provided and is different than the OpenAPI value, the argument value will override the OpenAPI va
    lue.
    """
    minimum_compression_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) Name of the REST API. If importing an OpenAPI specification via the `body` argument, this
    corresponds to the `info.title` field. If the argument value is different than the OpenAPI value, t
    he argument value will override the OpenAPI value.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of customizations for importing the specification in the `body` argument. For example
    , to exclude DocumentationParts from an imported API, set `ignore` equal to `documentation`. Additio
    nal documentation, including other parameters such as `basepath`, can be found in the [API Gateway D
    eveloper Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.
    html).
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) JSON formatted policy document that controls access to the API Gateway. For more informat
    ion about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](
    https://learn.hashicorp.com/terraform/aws/iam-policy). Terraform will only perform drift detection o
    f its value when present in a configuration. We recommend using the [`aws_api_gateway_rest_api_polic
    y` resource](/docs/providers/aws/r/api_gateway_rest_api_policy.html) instead. If importing an OpenAP
    I specification via the `body` argument, this corresponds to the [`x-amazon-apigateway-policy` exten
    sion](https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-policy.html).
    If the argument value is provided and is different than the OpenAPI value, the argument value will o
    verride the OpenAPI value.
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Specifies the mode of the PutRestApi operation when importing an OpenAPI specification vi
    a the `body` argument (create or update operation). Valid values are `merge` and `overwrite`. If uns
    pecificed, defaults to `overwrite` (for backwards compatibility). This corresponds to the [`x-amazon
    apigateway-put-integration-method` extension](https://docs.aws.amazon.com/apigateway/latest/develop
    erguide/api-gateway-swagger-extensions-put-integration-method.html). If the argument value is provid
    ed and is different than the OpenAPI value, the argument value will override the OpenAPI value.
    """
    put_rest_api_mode: str | core.StringOut | None = core.attr(str, default=None)

    """
    The resource ID of the REST API's root
    """
    root_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        api_key_source: str | core.StringOut | None = None,
        binary_media_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        body: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        disable_execute_api_endpoint: bool | core.BoolOut | None = None,
        endpoint_configuration: EndpointConfiguration | None = None,
        minimum_compression_size: int | core.IntOut | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        policy: str | core.StringOut | None = None,
        put_rest_api_mode: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RestApi.Args(
                name=name,
                api_key_source=api_key_source,
                binary_media_types=binary_media_types,
                body=body,
                description=description,
                disable_execute_api_endpoint=disable_execute_api_endpoint,
                endpoint_configuration=endpoint_configuration,
                minimum_compression_size=minimum_compression_size,
                parameters=parameters,
                policy=policy,
                put_rest_api_mode=put_rest_api_mode,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_source: str | core.StringOut | None = core.arg(default=None)

        binary_media_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        body: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disable_execute_api_endpoint: bool | core.BoolOut | None = core.arg(default=None)

        endpoint_configuration: EndpointConfiguration | None = core.arg(default=None)

        minimum_compression_size: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        put_rest_api_mode: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
