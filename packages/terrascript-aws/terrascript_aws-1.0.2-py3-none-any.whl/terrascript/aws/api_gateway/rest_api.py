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


@core.resource(type="aws_api_gateway_rest_api", namespace="aws_api_gateway")
class RestApi(core.Resource):

    api_key_source: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    binary_media_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    body: str | core.StringOut | None = core.attr(str, default=None)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    disable_execute_api_endpoint: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    endpoint_configuration: EndpointConfiguration | None = core.attr(
        EndpointConfiguration, default=None, computed=True
    )

    execution_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    minimum_compression_size: int | core.IntOut | None = core.attr(int, default=None)

    name: str | core.StringOut = core.attr(str)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    put_rest_api_mode: str | core.StringOut | None = core.attr(str, default=None)

    root_resource_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
