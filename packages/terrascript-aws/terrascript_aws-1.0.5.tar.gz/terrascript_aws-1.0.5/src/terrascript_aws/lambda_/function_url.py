import terrascript.core as core


@core.schema
class Cors(core.Schema):

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
        allow_credentials: bool | core.BoolOut | None = core.arg(default=None)

        allow_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allow_methods: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        allow_origins: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        expose_headers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        max_age: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_lambda_function_url", namespace="lambda_")
class FunctionUrl(core.Resource):
    """
    (Required) The type of authentication that the function URL uses. Set to `"AWS_IAM"` to restrict acc
    ess to authenticated IAM users only. Set to `"NONE"` to bypass IAM authentication and create a publi
    c endpoint. See the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html)
    for more details.
    """

    authorization_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/H
    TTP/CORS) settings for the function URL. Documented below.
    """
    cors: Cors | None = core.attr(Cors, default=None)

    """
    The Amazon Resource Name (ARN) of the function.
    """
    function_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name (or ARN) of the Lambda function.
    """
    function_name: str | core.StringOut = core.attr(str)

    """
    The HTTP URL endpoint for the function in the format `https://<url_id>.lambda-url.<region>.on.aws`.
    """
    function_url: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

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
        resource_name: str,
        *,
        authorization_type: str | core.StringOut,
        function_name: str | core.StringOut,
        cors: Cors | None = None,
        qualifier: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FunctionUrl.Args(
                authorization_type=authorization_type,
                function_name=function_name,
                cors=cors,
                qualifier=qualifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authorization_type: str | core.StringOut = core.arg()

        cors: Cors | None = core.arg(default=None)

        function_name: str | core.StringOut = core.arg()

        qualifier: str | core.StringOut | None = core.arg(default=None)
