import terrascript.core as core


@core.schema
class JwtConfiguration(core.Schema):

    audience: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    issuer: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        audience: list[str] | core.ArrayOut[core.StringOut] | None = None,
        issuer: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=JwtConfiguration.Args(
                audience=audience,
                issuer=issuer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audience: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        issuer: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_authorizer", namespace="aws_apigatewayv2")
class Authorizer(core.Resource):

    api_id: str | core.StringOut = core.attr(str)

    authorizer_credentials_arn: str | core.StringOut | None = core.attr(str, default=None)

    authorizer_payload_format_version: str | core.StringOut | None = core.attr(str, default=None)

    authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    authorizer_type: str | core.StringOut = core.attr(str)

    authorizer_uri: str | core.StringOut | None = core.attr(str, default=None)

    enable_simple_responses: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    jwt_configuration: JwtConfiguration | None = core.attr(JwtConfiguration, default=None)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: str | core.StringOut,
        authorizer_type: str | core.StringOut,
        name: str | core.StringOut,
        authorizer_credentials_arn: str | core.StringOut | None = None,
        authorizer_payload_format_version: str | core.StringOut | None = None,
        authorizer_result_ttl_in_seconds: int | core.IntOut | None = None,
        authorizer_uri: str | core.StringOut | None = None,
        enable_simple_responses: bool | core.BoolOut | None = None,
        identity_sources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        jwt_configuration: JwtConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Authorizer.Args(
                api_id=api_id,
                authorizer_type=authorizer_type,
                name=name,
                authorizer_credentials_arn=authorizer_credentials_arn,
                authorizer_payload_format_version=authorizer_payload_format_version,
                authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
                authorizer_uri=authorizer_uri,
                enable_simple_responses=enable_simple_responses,
                identity_sources=identity_sources,
                jwt_configuration=jwt_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: str | core.StringOut = core.arg()

        authorizer_credentials_arn: str | core.StringOut | None = core.arg(default=None)

        authorizer_payload_format_version: str | core.StringOut | None = core.arg(default=None)

        authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.arg(default=None)

        authorizer_type: str | core.StringOut = core.arg()

        authorizer_uri: str | core.StringOut | None = core.arg(default=None)

        enable_simple_responses: bool | core.BoolOut | None = core.arg(default=None)

        identity_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        jwt_configuration: JwtConfiguration | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
