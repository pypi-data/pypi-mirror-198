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


@core.resource(type="aws_lambda_function_url", namespace="aws_lambda_")
class FunctionUrl(core.Resource):

    authorization_type: str | core.StringOut = core.attr(str)

    cors: Cors | None = core.attr(Cors, default=None)

    function_arn: str | core.StringOut = core.attr(str, computed=True)

    function_name: str | core.StringOut = core.attr(str)

    function_url: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    qualifier: str | core.StringOut | None = core.attr(str, default=None)

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
