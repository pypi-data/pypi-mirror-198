import terrascript.core as core


@core.schema
class TokenValidityUnits(core.Schema):

    access_token: str | core.StringOut = core.attr(str, computed=True)

    id_token: str | core.StringOut = core.attr(str, computed=True)

    refresh_token: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        access_token: str | core.StringOut,
        id_token: str | core.StringOut,
        refresh_token: str | core.StringOut,
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
        access_token: str | core.StringOut = core.arg()

        id_token: str | core.StringOut = core.arg()

        refresh_token: str | core.StringOut = core.arg()


@core.schema
class AnalyticsConfiguration(core.Schema):

    application_arn: str | core.StringOut = core.attr(str, computed=True)

    application_id: str | core.StringOut = core.attr(str, computed=True)

    external_id: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    user_data_shared: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        application_arn: str | core.StringOut,
        application_id: str | core.StringOut,
        external_id: str | core.StringOut,
        role_arn: str | core.StringOut,
        user_data_shared: bool | core.BoolOut,
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
        application_arn: str | core.StringOut = core.arg()

        application_id: str | core.StringOut = core.arg()

        external_id: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        user_data_shared: bool | core.BoolOut = core.arg()


@core.data(type="aws_cognito_user_pool_client", namespace="aws_cognito")
class DsUserPoolClient(core.Data):
    """
    (Optional) Time limit, between 5 minutes and 1 day, after which the access token is no longer valid
    and cannot be used. This value will be overridden if you have entered a value in `token_validity_uni
    ts`.
    """

    access_token_validity: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) List of allowed OAuth flows (code, implicit, client_credentials).
    """
    allowed_oauth_flows: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Whether the client is allowed to follow the OAuth protocol when interacting with Cognito
    user pools.
    """
    allowed_oauth_flows_user_pool_client: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.
    admin).
    """
    allowed_oauth_scopes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for Amazon Pinpoint analytics for collecting metrics for this user po
    ol. [Detailed below](#analytics_configuration).
    """
    analytics_configuration: list[AnalyticsConfiguration] | core.ArrayOut[
        AnalyticsConfiguration
    ] = core.attr(AnalyticsConfiguration, computed=True, kind=core.Kind.array)

    """
    (Optional) List of allowed callback URLs for the identity providers.
    """
    callback_urls: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) Client Id of the user pool.
    """
    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Default redirect URI. Must be in the list of callback URLs.
    """
    default_redirect_uri: str | core.StringOut = core.attr(str, computed=True)

    enable_propagate_additional_user_context_data: bool | core.BoolOut = core.attr(
        bool, computed=True
    )

    """
    (Optional) Enables or disables token revocation.
    """
    enable_token_revocation: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUT
    H, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH,
    ALLOW_REFRESH_TOKEN_AUTH).
    """
    explicit_auth_flows: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Should an application secret be generated.
    """
    generate_secret: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Time limit, between 5 minutes and 1 day, after which the ID token is no longer valid and
    cannot be used. This value will be overridden if you have entered a value in `token_validity_units`.
    """
    id_token_validity: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) List of allowed logout URLs for the identity providers.
    """
    logout_urls: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Choose which errors and responses are returned by Cognito APIs during authentication, acc
    ount confirmation, and password recovery when the user does not exist in the user pool. When set to
    ENABLED` and the user does not exist, authentication returns an error indicating either the usernam
    e or password was incorrect, and account confirmation and password recovery return a response indica
    ting a code was sent to a simulated destination. When set to `LEGACY`, those APIs will return a `Use
    rNotFoundException` exception if the user does not exist in the user pool.
    """
    prevent_user_existence_errors: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of user pool attributes the application client can read from.
    """
    read_attributes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Time limit in days refresh tokens are valid for.
    """
    refresh_token_validity: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) List of provider names for the identity providers that are supported on this client. Uses
    the `provider_name` attribute of `aws_cognito_identity_provider` resource(s), or the equivalent str
    ing(s).
    """
    supported_identity_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Configuration block for units in which the validity times are represented in. [Detailed b
    elow](#token_validity_units).
    """
    token_validity_units: list[TokenValidityUnits] | core.ArrayOut[TokenValidityUnits] = core.attr(
        TokenValidityUnits, computed=True, kind=core.Kind.array
    )

    """
    (Required) User pool the client belongs to.
    """
    user_pool_id: str | core.StringOut = core.attr(str)

    """
    (Optional) List of user pool attributes the application client can write to.
    """
    write_attributes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        client_id: str | core.StringOut,
        user_pool_id: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsUserPoolClient.Args(
                client_id=client_id,
                user_pool_id=user_pool_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: str | core.StringOut = core.arg()

        user_pool_id: str | core.StringOut = core.arg()
