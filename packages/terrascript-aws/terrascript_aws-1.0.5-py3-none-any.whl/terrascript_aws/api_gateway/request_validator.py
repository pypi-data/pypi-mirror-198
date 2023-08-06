import terrascript.core as core


@core.resource(type="aws_api_gateway_request_validator", namespace="api_gateway")
class RequestValidator(core.Resource):
    """
    The unique ID of the request validator
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the request validator
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the associated Rest API
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Boolean whether to validate request body. Defaults to `false`.
    """
    validate_request_body: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Boolean whether to validate request parameters. Defaults to `false`.
    """
    validate_request_parameters: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        rest_api_id: str | core.StringOut,
        validate_request_body: bool | core.BoolOut | None = None,
        validate_request_parameters: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=RequestValidator.Args(
                name=name,
                rest_api_id=rest_api_id,
                validate_request_body=validate_request_body,
                validate_request_parameters=validate_request_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        rest_api_id: str | core.StringOut = core.arg()

        validate_request_body: bool | core.BoolOut | None = core.arg(default=None)

        validate_request_parameters: bool | core.BoolOut | None = core.arg(default=None)
