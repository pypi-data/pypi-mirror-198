import terrascript.core as core


@core.schema
class CorsConfiguration(core.Schema):

    allow_credentials: bool | core.BoolOut = core.attr(bool, computed=True)

    allow_headers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allow_methods: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allow_origins: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    expose_headers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_age: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        allow_credentials: bool | core.BoolOut,
        allow_headers: list[str] | core.ArrayOut[core.StringOut],
        allow_methods: list[str] | core.ArrayOut[core.StringOut],
        allow_origins: list[str] | core.ArrayOut[core.StringOut],
        expose_headers: list[str] | core.ArrayOut[core.StringOut],
        max_age: int | core.IntOut,
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
        allow_credentials: bool | core.BoolOut = core.arg()

        allow_headers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        allow_methods: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        allow_origins: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        expose_headers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        max_age: int | core.IntOut = core.arg()


@core.data(type="aws_apigatewayv2_api", namespace="aws_apigatewayv2")
class DsApi(core.Data):

    api_endpoint: str | core.StringOut = core.attr(str, computed=True)

    api_id: str | core.StringOut = core.attr(str)

    api_key_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cors_configuration: list[CorsConfiguration] | core.ArrayOut[CorsConfiguration] = core.attr(
        CorsConfiguration, computed=True, kind=core.Kind.array
    )

    description: str | core.StringOut = core.attr(str, computed=True)

    disable_execute_api_endpoint: bool | core.BoolOut = core.attr(bool, computed=True)

    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    protocol_type: str | core.StringOut = core.attr(str, computed=True)

    route_selection_expression: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        api_id: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApi.Args(
                api_id=api_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_id: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
