import terrascript.core as core


@core.schema
class LogConfig(core.Schema):

    cloudwatch_logs_role_arn: str | core.StringOut = core.attr(str)

    exclude_verbose_content: bool | core.BoolOut | None = core.attr(bool, default=None)

    field_log_level: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cloudwatch_logs_role_arn: str | core.StringOut,
        field_log_level: str | core.StringOut,
        exclude_verbose_content: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=LogConfig.Args(
                cloudwatch_logs_role_arn=cloudwatch_logs_role_arn,
                field_log_level=field_log_level,
                exclude_verbose_content=exclude_verbose_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs_role_arn: str | core.StringOut = core.arg()

        exclude_verbose_content: bool | core.BoolOut | None = core.arg(default=None)

        field_log_level: str | core.StringOut = core.arg()


@core.schema
class UserPoolConfig(core.Schema):

    app_id_client_regex: str | core.StringOut | None = core.attr(str, default=None)

    aws_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    default_action: str | core.StringOut = core.attr(str)

    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        default_action: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        app_id_client_regex: str | core.StringOut | None = None,
        aws_region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=UserPoolConfig.Args(
                default_action=default_action,
                user_pool_id=user_pool_id,
                app_id_client_regex=app_id_client_regex,
                aws_region=aws_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        app_id_client_regex: str | core.StringOut | None = core.arg(default=None)

        aws_region: str | core.StringOut | None = core.arg(default=None)

        default_action: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()


@core.schema
class OpenidConnectConfig(core.Schema):

    auth_ttl: int | core.IntOut | None = core.attr(int, default=None)

    client_id: str | core.StringOut | None = core.attr(str, default=None)

    iat_ttl: int | core.IntOut | None = core.attr(int, default=None)

    issuer: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        issuer: str | core.StringOut,
        auth_ttl: int | core.IntOut | None = None,
        client_id: str | core.StringOut | None = None,
        iat_ttl: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=OpenidConnectConfig.Args(
                issuer=issuer,
                auth_ttl=auth_ttl,
                client_id=client_id,
                iat_ttl=iat_ttl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_ttl: int | core.IntOut | None = core.arg(default=None)

        client_id: str | core.StringOut | None = core.arg(default=None)

        iat_ttl: int | core.IntOut | None = core.arg(default=None)

        issuer: str | core.StringOut = core.arg()


@core.schema
class LambdaAuthorizerConfig(core.Schema):

    authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    authorizer_uri: str | core.StringOut = core.attr(str)

    identity_validation_expression: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        authorizer_uri: str | core.StringOut,
        authorizer_result_ttl_in_seconds: int | core.IntOut | None = None,
        identity_validation_expression: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LambdaAuthorizerConfig.Args(
                authorizer_uri=authorizer_uri,
                authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
                identity_validation_expression=identity_validation_expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorizer_result_ttl_in_seconds: int | core.IntOut | None = core.arg(default=None)

        authorizer_uri: str | core.StringOut = core.arg()

        identity_validation_expression: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AdditionalAuthenticationProviderUserPoolConfig(core.Schema):

    app_id_client_regex: str | core.StringOut | None = core.attr(str, default=None)

    aws_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_pool_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        user_pool_id: str | core.StringOut,
        app_id_client_regex: str | core.StringOut | None = None,
        aws_region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AdditionalAuthenticationProviderUserPoolConfig.Args(
                user_pool_id=user_pool_id,
                app_id_client_regex=app_id_client_regex,
                aws_region=aws_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        app_id_client_regex: str | core.StringOut | None = core.arg(default=None)

        aws_region: str | core.StringOut | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()


@core.schema
class AdditionalAuthenticationProvider(core.Schema):

    authentication_type: str | core.StringOut = core.attr(str)

    lambda_authorizer_config: LambdaAuthorizerConfig | None = core.attr(
        LambdaAuthorizerConfig, default=None
    )

    openid_connect_config: OpenidConnectConfig | None = core.attr(OpenidConnectConfig, default=None)

    user_pool_config: AdditionalAuthenticationProviderUserPoolConfig | None = core.attr(
        AdditionalAuthenticationProviderUserPoolConfig, default=None
    )

    def __init__(
        self,
        *,
        authentication_type: str | core.StringOut,
        lambda_authorizer_config: LambdaAuthorizerConfig | None = None,
        openid_connect_config: OpenidConnectConfig | None = None,
        user_pool_config: AdditionalAuthenticationProviderUserPoolConfig | None = None,
    ):
        super().__init__(
            args=AdditionalAuthenticationProvider.Args(
                authentication_type=authentication_type,
                lambda_authorizer_config=lambda_authorizer_config,
                openid_connect_config=openid_connect_config,
                user_pool_config=user_pool_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_type: str | core.StringOut = core.arg()

        lambda_authorizer_config: LambdaAuthorizerConfig | None = core.arg(default=None)

        openid_connect_config: OpenidConnectConfig | None = core.arg(default=None)

        user_pool_config: AdditionalAuthenticationProviderUserPoolConfig | None = core.arg(
            default=None
        )


@core.resource(type="aws_appsync_graphql_api", namespace="appsync")
class GraphqlApi(core.Resource):
    """
    (Optional) One or more additional authentication providers for the GraphqlApi. Defined below.
    """

    additional_authentication_provider: list[AdditionalAuthenticationProvider] | core.ArrayOut[
        AdditionalAuthenticationProvider
    ] | None = core.attr(AdditionalAuthenticationProvider, default=None, kind=core.Kind.array)

    """
    The ARN
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`,
    OPENID_CONNECT`, `AWS_LAMBDA`
    """
    authentication_type: str | core.StringOut = core.attr(str)

    """
    API ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Nested argument containing Lambda authorizer configuration. Defined below.
    """
    lambda_authorizer_config: LambdaAuthorizerConfig | None = core.attr(
        LambdaAuthorizerConfig, default=None
    )

    """
    (Optional) Nested argument containing logging configuration. Defined below.
    """
    log_config: LogConfig | None = core.attr(LogConfig, default=None)

    """
    (Required) A user-supplied name for the GraphqlApi.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Nested argument containing OpenID Connect configuration. Defined below.
    """
    openid_connect_config: OpenidConnectConfig | None = core.attr(OpenidConnectConfig, default=None)

    """
    (Optional) The schema definition, in GraphQL schema language format. Terraform cannot perform drift
    detection of this configuration.
    """
    schema: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    Map of URIs associated with the APIE.g., `uris["GRAPHQL"] = https://ID.appsync-api.REGION.amazonaws.
    com/graphql`
    """
    uris: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    (Optional) The Amazon Cognito User Pool configuration. Defined below.
    """
    user_pool_config: UserPoolConfig | None = core.attr(UserPoolConfig, default=None)

    """
    (Optional) Whether tracing with X-ray is enabled. Defaults to false.
    """
    xray_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_type: str | core.StringOut,
        name: str | core.StringOut,
        additional_authentication_provider: list[AdditionalAuthenticationProvider]
        | core.ArrayOut[AdditionalAuthenticationProvider]
        | None = None,
        lambda_authorizer_config: LambdaAuthorizerConfig | None = None,
        log_config: LogConfig | None = None,
        openid_connect_config: OpenidConnectConfig | None = None,
        schema: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_pool_config: UserPoolConfig | None = None,
        xray_enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GraphqlApi.Args(
                authentication_type=authentication_type,
                name=name,
                additional_authentication_provider=additional_authentication_provider,
                lambda_authorizer_config=lambda_authorizer_config,
                log_config=log_config,
                openid_connect_config=openid_connect_config,
                schema=schema,
                tags=tags,
                tags_all=tags_all,
                user_pool_config=user_pool_config,
                xray_enabled=xray_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        additional_authentication_provider: list[AdditionalAuthenticationProvider] | core.ArrayOut[
            AdditionalAuthenticationProvider
        ] | None = core.arg(default=None)

        authentication_type: str | core.StringOut = core.arg()

        lambda_authorizer_config: LambdaAuthorizerConfig | None = core.arg(default=None)

        log_config: LogConfig | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        openid_connect_config: OpenidConnectConfig | None = core.arg(default=None)

        schema: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_pool_config: UserPoolConfig | None = core.arg(default=None)

        xray_enabled: bool | core.BoolOut | None = core.arg(default=None)
