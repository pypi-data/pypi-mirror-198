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


@core.resource(type="aws_cognito_user_pool_client", namespace="aws_cognito")
class UserPoolClient(core.Resource):
    """
    (Optional) Time limit, between 5 minutes and 1 day, after which the access token is no longer valid
    and cannot be used. This value will be overridden if you have entered a value in `token_validity_uni
    ts`.
    """

    access_token_validity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) List of allowed OAuth flows (code, implicit, client_credentials).
    """
    allowed_oauth_flows: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Whether the client is allowed to follow the OAuth protocol when interacting with Cognito
    user pools.
    """
    allowed_oauth_flows_user_pool_client: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.
    admin).
    """
    allowed_oauth_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for Amazon Pinpoint analytics for collecting metrics for this user po
    ol. [Detailed below](#analytics_configuration).
    """
    analytics_configuration: AnalyticsConfiguration | None = core.attr(
        AnalyticsConfiguration, default=None
    )

    """
    (Optional) List of allowed callback URLs for the identity providers.
    """
    callback_urls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    Client secret of the user pool client.
    """
    client_secret: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Default redirect URI. Must be in the list of callback URLs.
    """
    default_redirect_uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Activates the propagation of additional user context data.
    """
    enable_propagate_additional_user_context_data: bool | core.BoolOut | None = core.attr(
        bool, default=None
    )

    """
    (Optional) Enables or disables token revocation.
    """
    enable_token_revocation: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUT
    H, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH,
    ALLOW_REFRESH_TOKEN_AUTH).
    """
    explicit_auth_flows: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Should an application secret be generated.
    """
    generate_secret: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    ID of the user pool client.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Time limit, between 5 minutes and 1 day, after which the ID token is no longer valid and
    cannot be used. This value will be overridden if you have entered a value in `token_validity_units`.
    """
    id_token_validity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) List of allowed logout URLs for the identity providers.
    """
    logout_urls: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) Name of the application client.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Choose which errors and responses are returned by Cognito APIs during authentication, acc
    ount confirmation, and password recovery when the user does not exist in the user pool. When set to
    ENABLED` and the user does not exist, authentication returns an error indicating either the usernam
    e or password was incorrect, and account confirmation and password recovery return a response indica
    ting a code was sent to a simulated destination. When set to `LEGACY`, those APIs will return a `Use
    rNotFoundException` exception if the user does not exist in the user pool.
    """
    prevent_user_existence_errors: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) List of user pool attributes the application client can read from.
    """
    read_attributes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Time limit in days refresh tokens are valid for.
    """
    refresh_token_validity: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) List of provider names for the identity providers that are supported on this client. Uses
    the `provider_name` attribute of `aws_cognito_identity_provider` resource(s), or the equivalent str
    ing(s).
    """
    supported_identity_providers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for units in which the validity times are represented in. [Detailed b
    elow](#token_validity_units).
    """
    token_validity_units: TokenValidityUnits | None = core.attr(TokenValidityUnits, default=None)

    """
    (Required) User pool the client belongs to.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    """
    (Optional) List of user pool attributes the application client can write to.
    """
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
