import terrascript.core as core


@core.resource(type="aws_api_gateway_method", namespace="aws_api_gateway")
class Method(core.Resource):

    api_key_required: bool | core.BoolOut | None = core.attr(bool, default=None)

    authorization: str | core.StringOut = core.attr(str)

    authorization_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    authorizer_id: str | core.StringOut | None = core.attr(str, default=None)

    http_method: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    operation_name: str | core.StringOut | None = core.attr(str, default=None)

    request_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_parameters: dict[str, bool] | core.MapOut[core.BoolOut] | None = core.attr(
        bool, default=None, kind=core.Kind.map
    )

    request_validator_id: str | core.StringOut | None = core.attr(str, default=None)

    resource_id: str | core.StringOut = core.attr(str)

    rest_api_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        authorization: str | core.StringOut,
        http_method: str | core.StringOut,
        resource_id: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        api_key_required: bool | core.BoolOut | None = None,
        authorization_scopes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        authorizer_id: str | core.StringOut | None = None,
        operation_name: str | core.StringOut | None = None,
        request_models: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        request_parameters: dict[str, bool] | core.MapOut[core.BoolOut] | None = None,
        request_validator_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Method.Args(
                authorization=authorization,
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                api_key_required=api_key_required,
                authorization_scopes=authorization_scopes,
                authorizer_id=authorizer_id,
                operation_name=operation_name,
                request_models=request_models,
                request_parameters=request_parameters,
                request_validator_id=request_validator_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_required: bool | core.BoolOut | None = core.arg(default=None)

        authorization: str | core.StringOut = core.arg()

        authorization_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        authorizer_id: str | core.StringOut | None = core.arg(default=None)

        http_method: str | core.StringOut = core.arg()

        operation_name: str | core.StringOut | None = core.arg(default=None)

        request_models: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        request_parameters: dict[str, bool] | core.MapOut[core.BoolOut] | None = core.arg(
            default=None
        )

        request_validator_id: str | core.StringOut | None = core.arg(default=None)

        resource_id: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()
