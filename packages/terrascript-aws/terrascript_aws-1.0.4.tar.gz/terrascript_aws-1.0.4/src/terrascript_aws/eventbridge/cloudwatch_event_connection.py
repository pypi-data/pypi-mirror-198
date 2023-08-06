import terrascript.core as core


@core.schema
class Basic(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=Basic.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class QueryString(core.Schema):

    is_value_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    key: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        is_value_secret: bool | core.BoolOut | None = None,
        key: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=QueryString.Args(
                is_value_secret=is_value_secret,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        is_value_secret: bool | core.BoolOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Body(core.Schema):

    is_value_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    key: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        is_value_secret: bool | core.BoolOut | None = None,
        key: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Body.Args(
                is_value_secret=is_value_secret,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        is_value_secret: bool | core.BoolOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Header(core.Schema):

    is_value_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    key: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        is_value_secret: bool | core.BoolOut | None = None,
        key: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Header.Args(
                is_value_secret=is_value_secret,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        is_value_secret: bool | core.BoolOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class OauthHttpParameters(core.Schema):

    body: list[Body] | core.ArrayOut[Body] | None = core.attr(
        Body, default=None, kind=core.Kind.array
    )

    header: list[Header] | core.ArrayOut[Header] | None = core.attr(
        Header, default=None, kind=core.Kind.array
    )

    query_string: list[QueryString] | core.ArrayOut[QueryString] | None = core.attr(
        QueryString, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        body: list[Body] | core.ArrayOut[Body] | None = None,
        header: list[Header] | core.ArrayOut[Header] | None = None,
        query_string: list[QueryString] | core.ArrayOut[QueryString] | None = None,
    ):
        super().__init__(
            args=OauthHttpParameters.Args(
                body=body,
                header=header,
                query_string=query_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        body: list[Body] | core.ArrayOut[Body] | None = core.arg(default=None)

        header: list[Header] | core.ArrayOut[Header] | None = core.arg(default=None)

        query_string: list[QueryString] | core.ArrayOut[QueryString] | None = core.arg(default=None)


@core.schema
class ClientParameters(core.Schema):

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
    ):
        super().__init__(
            args=ClientParameters.Args(
                client_id=client_id,
                client_secret=client_secret,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()


@core.schema
class Oauth(core.Schema):

    authorization_endpoint: str | core.StringOut = core.attr(str)

    client_parameters: ClientParameters | None = core.attr(ClientParameters, default=None)

    http_method: str | core.StringOut = core.attr(str)

    oauth_http_parameters: OauthHttpParameters = core.attr(OauthHttpParameters)

    def __init__(
        self,
        *,
        authorization_endpoint: str | core.StringOut,
        http_method: str | core.StringOut,
        oauth_http_parameters: OauthHttpParameters,
        client_parameters: ClientParameters | None = None,
    ):
        super().__init__(
            args=Oauth.Args(
                authorization_endpoint=authorization_endpoint,
                http_method=http_method,
                oauth_http_parameters=oauth_http_parameters,
                client_parameters=client_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_endpoint: str | core.StringOut = core.arg()

        client_parameters: ClientParameters | None = core.arg(default=None)

        http_method: str | core.StringOut = core.arg()

        oauth_http_parameters: OauthHttpParameters = core.arg()


@core.schema
class InvocationHttpParameters(core.Schema):

    body: list[Body] | core.ArrayOut[Body] | None = core.attr(
        Body, default=None, kind=core.Kind.array
    )

    header: list[Header] | core.ArrayOut[Header] | None = core.attr(
        Header, default=None, kind=core.Kind.array
    )

    query_string: list[QueryString] | core.ArrayOut[QueryString] | None = core.attr(
        QueryString, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        body: list[Body] | core.ArrayOut[Body] | None = None,
        header: list[Header] | core.ArrayOut[Header] | None = None,
        query_string: list[QueryString] | core.ArrayOut[QueryString] | None = None,
    ):
        super().__init__(
            args=InvocationHttpParameters.Args(
                body=body,
                header=header,
                query_string=query_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        body: list[Body] | core.ArrayOut[Body] | None = core.arg(default=None)

        header: list[Header] | core.ArrayOut[Header] | None = core.arg(default=None)

        query_string: list[QueryString] | core.ArrayOut[QueryString] | None = core.arg(default=None)


@core.schema
class ApiKey(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ApiKey.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class AuthParameters(core.Schema):

    api_key: ApiKey | None = core.attr(ApiKey, default=None)

    basic: Basic | None = core.attr(Basic, default=None)

    invocation_http_parameters: InvocationHttpParameters | None = core.attr(
        InvocationHttpParameters, default=None
    )

    oauth: Oauth | None = core.attr(Oauth, default=None)

    def __init__(
        self,
        *,
        api_key: ApiKey | None = None,
        basic: Basic | None = None,
        invocation_http_parameters: InvocationHttpParameters | None = None,
        oauth: Oauth | None = None,
    ):
        super().__init__(
            args=AuthParameters.Args(
                api_key=api_key,
                basic=basic,
                invocation_http_parameters=invocation_http_parameters,
                oauth=oauth,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: ApiKey | None = core.arg(default=None)

        basic: Basic | None = core.arg(default=None)

        invocation_http_parameters: InvocationHttpParameters | None = core.arg(default=None)

        oauth: Oauth | None = core.arg(default=None)


@core.resource(type="aws_cloudwatch_event_connection", namespace="eventbridge")
class CloudwatchEventConnection(core.Resource):
    """
    The Amazon Resource Name (ARN) of the connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Parameters used for authorization. A maximum of 1 are allowed. Documented below.
    """
    auth_parameters: AuthParameters = core.attr(AuthParameters)

    """
    (Required) Choose the type of authorization to use for the connection. One of `API_KEY`,`BASIC`,`OAU
    TH_CLIENT_CREDENTIALS`.
    """
    authorization_type: str | core.StringOut = core.attr(str)

    """
    (Optional) Enter a description for the connection. Maximum of 512 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the new connection. Maximum of 64 characters consisting of numbers, lower/upp
    er case letters, .,-,_.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the secret created from the authorization parameters specified for
    the connection.
    """
    secret_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_parameters: AuthParameters,
        authorization_type: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventConnection.Args(
                auth_parameters=auth_parameters,
                authorization_type=authorization_type,
                name=name,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_parameters: AuthParameters = core.arg()

        authorization_type: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
