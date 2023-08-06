import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_endpoint_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: list[str] | core.ArrayOut[core.StringOut],
        vpc_endpoint_ids: list[str] | core.ArrayOut[core.StringOut],
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

        vpc_endpoint_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.data(type="aws_api_gateway_rest_api", namespace="api_gateway")
class DsRestApi(core.Data):
    """
    The source of the API key for requests.
    """

    api_key_source: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the REST API.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The list of binary media types supported by the REST API.
    """
    binary_media_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The description of the REST API.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The endpoint configuration of this RestApi showing the endpoint types of the API.
    """
    endpoint_configuration: list[EndpointConfiguration] | core.ArrayOut[
        EndpointConfiguration
    ] = core.attr(EndpointConfiguration, computed=True, kind=core.Kind.array)

    """
    The execution ARN part to be used in [`lambda_permission`](/docs/providers/aws/r/lambda_permission.h
    tml)'s `source_arn` when allowing API Gateway to invoke a Lambda function, e.g., `arn:aws:execute-ap
    i:eu-west-2:123456789012:z4675bid1j`, which can be concatenated with allowed stage, method and resou
    rce path.
    """
    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the ID of the found REST API.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Minimum response size to compress for the REST API.
    """
    minimum_compression_size: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The name of the REST API to look up. If no REST API is found with this name, an error wil
    l be returned. If multiple REST APIs are found with this name, an error will be returned.
    """
    name: str | core.StringOut = core.attr(str)

    """
    JSON formatted policy document that controls access to the API Gateway.
    """
    policy: str | core.StringOut = core.attr(str, computed=True)

    """
    Set to the ID of the API Gateway Resource on the found REST API where the route matches '/'.
    """
    root_resource_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Key-value map of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRestApi.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
