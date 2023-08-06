import terrascript.core as core


@core.schema
class AnalyticsConfiguration(core.Schema):

    application_arn: str | core.StringOut | None = core.attr(str, default=None)

    application_id: str | core.StringOut | None = core.attr(str, default=None)

    external_id: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    user_data_shared: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        application_arn: str | core.StringOut | None = None,
        application_id: str | core.StringOut | None = None,
        external_id: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        user_data_shared: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=AnalyticsConfiguration.Args(
                application_arn=application_arn,
                application_id=application_id,
                external_id=external_id,
                role_arn=role_arn,
                user_data_shared=user_data_shared,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_arn: str | core.StringOut | None = core.arg(default=None)

        application_id: str | core.StringOut | None = core.arg(default=None)

        external_id: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        user_data_shared: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class TokenValidityUnits(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    id_token: str | core.StringOut | None = core.attr(str, default=None)

    refresh_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: str | core.StringOut | None = None,
        id_token: str | core.StringOut | None = None,
        refresh_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TokenValidityUnits.Args(
                access_token=access_token,
                id_token=id_token,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        id_token: str | core.StringOut | None = core.arg(default=None)

        refresh_token: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_cognito_user_pool_client", namespace="cognito")
class UserPoolClient(core.Resource):

    access_token_validity: int | core.IntOut | None = core.attr(int, default=None)

    allowed_oauth_flows: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allowed_oauth_flows_user_pool_client: bool | core.BoolOut | None = core.attr(bool, default=None)

    allowed_oauth_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    analytics_configuration: AnalyticsConfiguration | None = core.attr(
        AnalyticsConfiguration, default=None
    )

    callback_urls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    client_secret: str | core.StringOut = core.attr(str, computed=True)

    default_redirect_uri: str | core.StringOut | None = core.attr(str, default=None)

    enable_propagate_additional_user_context_data: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    enable_token_revocation: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    explicit_auth_flows: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    generate_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    id_token_validity: int | core.IntOut | None = core.attr(int, default=None)

    logout_urls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    prevent_user_existence_errors: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    read_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    refresh_token_validity: int | core.IntOut | None = core.attr(int, default=None)

    supported_identity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    token_validity_units: TokenValidityUnits | None = core.attr(TokenValidityUnits, default=None)

    user_pool_id: str | core.StringOut = core.attr(str)

    write_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        user_pool_id: str | core.StringOut,
        access_token_validity: int | core.IntOut | None = None,
        allowed_oauth_flows: list[str] | core.ArrayOut[core.StringOut] | None = None,
        allowed_oauth_flows_user_pool_client: bool | core.BoolOut | None = None,
        allowed_oauth_scopes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        analytics_configuration: AnalyticsConfiguration | None = None,
        callback_urls: list[str] | core.ArrayOut[core.StringOut] | None = None,
        default_redirect_uri: str | core.StringOut | None = None,
        enable_propagate_additional_user_context_data: bool | core.BoolOut | None = None,
        enable_token_revocation: bool | core.BoolOut | None = None,
        explicit_auth_flows: list[str] | core.ArrayOut[core.StringOut] | None = None,
        generate_secret: bool | core.BoolOut | None = None,
        id_token_validity: int | core.IntOut | None = None,
        logout_urls: list[str] | core.ArrayOut[core.StringOut] | None = None,
        prevent_user_existence_errors: str | core.StringOut | None = None,
        read_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        refresh_token_validity: int | core.IntOut | None = None,
        supported_identity_providers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        token_validity_units: TokenValidityUnits | None = None,
        write_attributes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPoolClient.Args(
                name=name,
                user_pool_id=user_pool_id,
                access_token_validity=access_token_validity,
                allowed_oauth_flows=allowed_oauth_flows,
                allowed_oauth_flows_user_pool_client=allowed_oauth_flows_user_pool_client,
                allowed_oauth_scopes=allowed_oauth_scopes,
                analytics_configuration=analytics_configuration,
                callback_urls=callback_urls,
                default_redirect_uri=default_redirect_uri,
                enable_propagate_additional_user_context_data=enable_propagate_additional_user_context_data,
                enable_token_revocation=enable_token_revocation,
                explicit_auth_flows=explicit_auth_flows,
                generate_secret=generate_secret,
                id_token_validity=id_token_validity,
                logout_urls=logout_urls,
                prevent_user_existence_errors=prevent_user_existence_errors,
                read_attributes=read_attributes,
                refresh_token_validity=refresh_token_validity,
                supported_identity_providers=supported_identity_providers,
                token_validity_units=token_validity_units,
                write_attributes=write_attributes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_token_validity: int | core.IntOut | None = core.arg(default=None)

        allowed_oauth_flows: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        allowed_oauth_flows_user_pool_client: bool | core.BoolOut | None = core.arg(default=None)

        allowed_oauth_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        analytics_configuration: AnalyticsConfiguration | None = core.arg(default=None)

        callback_urls: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        default_redirect_uri: str | core.StringOut | None = core.arg(default=None)

        enable_propagate_additional_user_context_data: bool | core.BoolOut | None = core.arg(
            default=None
        )

        enable_token_revocation: bool | core.BoolOut | None = core.arg(default=None)

        explicit_auth_flows: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        generate_secret: bool | core.BoolOut | None = core.arg(default=None)

        id_token_validity: int | core.IntOut | None = core.arg(default=None)

        logout_urls: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        prevent_user_existence_errors: str | core.StringOut | None = core.arg(default=None)

        read_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        refresh_token_validity: int | core.IntOut | None = core.arg(default=None)

        supported_identity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        token_validity_units: TokenValidityUnits | None = core.arg(default=None)

        user_pool_id: str | core.StringOut = core.arg()

        write_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
