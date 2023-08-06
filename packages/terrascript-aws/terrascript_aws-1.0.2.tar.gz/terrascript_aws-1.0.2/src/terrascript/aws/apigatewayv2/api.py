import terrascript.core as core


@core.schema
class CorsConfiguration(core.Schema):

    allow_credentials: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_age: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allow_credentials: bool | core.BoolOut | None = None,
        allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = None,
        allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = None,
        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        max_age: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CorsConfiguration.Args(
                allow_credentials=allow_credentials,
                allow_headers=allow_headers,
                allow_methods=allow_methods,
                allow_origins=allow_origins,
                expose_headers=expose_headers,
                max_age=max_age,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_credentials: bool | core.BoolOut | None = core.arg(default=None)

        allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_age: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_api", namespace="aws_apigatewayv2")
class Api(core.Resource):

    api_endpoint: str | core.StringOut = core.attr(str, computed=True)

    api_key_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    body: str | core.StringOut | None = core.attr(str, default=None)

    cors_configuration: CorsConfiguration | None = core.attr(CorsConfiguration, default=None)

    credentials_arn: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    disable_execute_api_endpoint: bool | core.BoolOut | None = core.attr(bool, default=None)

    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    fail_on_warnings: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    protocol_type: str | core.StringOut = core.attr(str)

    route_key: str | core.StringOut | None = core.attr(str, default=None)

    route_selection_expression: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target: str | core.StringOut | None = core.attr(str, default=None)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        protocol_type: str | core.StringOut,
        api_key_selection_expression: str | core.StringOut | None = None,
        body: str | core.StringOut | None = None,
        cors_configuration: CorsConfiguration | None = None,
        credentials_arn: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        disable_execute_api_endpoint: bool | core.BoolOut | None = None,
        fail_on_warnings: bool | core.BoolOut | None = None,
        route_key: str | core.StringOut | None = None,
        route_selection_expression: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Api.Args(
                name=name,
                protocol_type=protocol_type,
                api_key_selection_expression=api_key_selection_expression,
                body=body,
                cors_configuration=cors_configuration,
                credentials_arn=credentials_arn,
                description=description,
                disable_execute_api_endpoint=disable_execute_api_endpoint,
                fail_on_warnings=fail_on_warnings,
                route_key=route_key,
                route_selection_expression=route_selection_expression,
                tags=tags,
                tags_all=tags_all,
                target=target,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_selection_expression: str | core.StringOut | None = core.arg(default=None)

        body: str | core.StringOut | None = core.arg(default=None)

        cors_configuration: CorsConfiguration | None = core.arg(default=None)

        credentials_arn: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        disable_execute_api_endpoint: bool | core.BoolOut | None = core.arg(default=None)

        fail_on_warnings: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        protocol_type: str | core.StringOut = core.arg()

        route_key: str | core.StringOut | None = core.arg(default=None)

        route_selection_expression: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)
