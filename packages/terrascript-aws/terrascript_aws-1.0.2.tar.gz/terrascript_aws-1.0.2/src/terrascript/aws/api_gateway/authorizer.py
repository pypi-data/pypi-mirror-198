import terrascript.core as core


@core.resource(type="aws_api_gateway_authorizer", namespace="aws_api_gateway")
class Authorizer(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authorizer_credentials: str | core.StringOut | None = core.attr(str, default=None)

    authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    authorizer_uri: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_source: str | core.StringOut | None = core.attr(str, default=None)

    identity_validation_expression: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    rest_api_id: str | core.StringOut = core.attr(str)

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
