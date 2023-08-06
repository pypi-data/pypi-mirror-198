import terrascript.core as core


@core.schema
class Cors(core.Schema):

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
            args=Cors.Args(
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


@core.data(type="aws_lambda_function_url", namespace="lambda_")
class DsFunctionUrl(core.Data):
    """
    The type of authentication that the function URL uses.
    """

    authorization_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) s
    ettings for the function URL. See the [`aws_lambda_function_url` resource](/docs/providers/aws/r/lam
    bda_function_url.html) documentation for more details.
    """
    cors: list[Cors] | core.ArrayOut[Cors] = core.attr(Cors, computed=True, kind=core.Kind.array)

    """
    When the function URL was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime).
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) of the function.
    """
    function_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) he name (or ARN) of the Lambda function.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    The HTTP URL endpoint for the function in the format `https://<url_id>.lambda-url.<region>.on.aws`.
    """
    function_url: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    When the function URL configuration was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOT
    E-datetime).
    """
    last_modified_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The alias name or `"$LATEST"`.
    """
    qualifier: str | core.StringOut | None = core.attr(str, default=None)

    """
    A generated ID for the endpoint.
    """
    url_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        function_name: str | core.StringOut,
        qualifier: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFunctionUrl.Args(
                function_name=function_name,
                qualifier=qualifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: str | core.StringOut = core.arg()

        qualifier: str | core.StringOut | None = core.arg(default=None)
