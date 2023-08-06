import terrascript.core as core


@core.resource(type="aws_api_gateway_authorizer", namespace="api_gateway")
class Authorizer(core.Resource):
    """
    Amazon Resource Name (ARN) of the API Gateway Authorizer
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The credentials required for the authorizer. To specify an IAM Role for API Gateway to as
    sume, use the IAM Role ARN.
    """
    authorizer_credentials: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The TTL of cached authorizer results in seconds. Defaults to `300`.
    """
    authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, required for type `TOKEN`/`REQUEST`) The authorizer's Uniform Resource Identifier (URI).
    This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:pa
    th/{service_api}`,
    """
    authorizer_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Authorizer identifier.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The source of the identity in an incoming request. Defaults to `method.request.header.Aut
    horization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, qu
    ery string parameters and stage variables - e.g., `"method.request.header.SomeHeaderName,method.requ
    est.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`
    """
    identity_source: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A validation expression for the incoming identity. For `TOKEN` type, this value should be
    a regular expression. The incoming token from the client is matched against this expression, and wi
    ll proceed if the token matches. If the token doesn't match, the client receives a 401 Unauthorized
    response.
    """
    identity_validation_expression: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the authorizer
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional, required for type `COGNITO_USER_POOLS`) A list of the Amazon Cognito user pool ARNs. Each
    element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
    """
    provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The ID of the associated REST API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a sin
    gle authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming
    request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool. Defaults to `TOK
    EN`.
    """
    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        authorizer_credentials: str | core.StringOut | None = None,
        authorizer_result_ttl_in_seconds: int | core.IntOut | None = None,
        authorizer_uri: str | core.StringOut | None = None,
        identity_source: str | core.StringOut | None = None,
        identity_validation_expression: str | core.StringOut | None = None,
        provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Authorizer.Args(
                name=name,
                rest_api_id=rest_api_id,
                authorizer_credentials=authorizer_credentials,
                authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
                authorizer_uri=authorizer_uri,
                identity_source=identity_source,
                identity_validation_expression=identity_validation_expression,
                provider_arns=provider_arns,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authorizer_credentials: str | core.StringOut | None = core.arg(default=None)

        authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.arg(default=None)

        authorizer_uri: str | core.StringOut | None = core.arg(default=None)

        identity_source: str | core.StringOut | None = core.arg(default=None)

        identity_validation_expression: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)
