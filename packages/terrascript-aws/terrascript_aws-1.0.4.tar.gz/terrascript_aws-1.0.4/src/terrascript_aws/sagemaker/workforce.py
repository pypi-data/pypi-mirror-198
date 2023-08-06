import terrascript.core as core


@core.schema
class CognitoConfig(core.Schema):

    client_id: str | core.StringOut = core.attr(str)

    user_pool: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        user_pool: str | core.StringOut,
    ):
        super().__init__(
            args=CognitoConfig.Args(
                client_id=client_id,
                user_pool=user_pool,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: str | core.StringOut = core.arg()

        user_pool: str | core.StringOut = core.arg()


@core.schema
class OidcConfig(core.Schema):

    authorization_endpoint: str | core.StringOut = core.attr(str)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    issuer: str | core.StringOut = core.attr(str)

    jwks_uri: str | core.StringOut = core.attr(str)

    logout_endpoint: str | core.StringOut = core.attr(str)

    token_endpoint: str | core.StringOut = core.attr(str)

    user_info_endpoint: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        authorization_endpoint: str | core.StringOut,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        issuer: str | core.StringOut,
        jwks_uri: str | core.StringOut,
        logout_endpoint: str | core.StringOut,
        token_endpoint: str | core.StringOut,
        user_info_endpoint: str | core.StringOut,
    ):
        super().__init__(
            args=OidcConfig.Args(
                authorization_endpoint=authorization_endpoint,
                client_id=client_id,
                client_secret=client_secret,
                issuer=issuer,
                jwks_uri=jwks_uri,
                logout_endpoint=logout_endpoint,
                token_endpoint=token_endpoint,
                user_info_endpoint=user_info_endpoint,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_endpoint: str | core.StringOut = core.arg()

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        issuer: str | core.StringOut = core.arg()

        jwks_uri: str | core.StringOut = core.arg()

        logout_endpoint: str | core.StringOut = core.arg()

        token_endpoint: str | core.StringOut = core.arg()

        user_info_endpoint: str | core.StringOut = core.arg()


@core.schema
class SourceIpConfig(core.Schema):

    cidrs: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        cidrs: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=SourceIpConfig.Args(
                cidrs=cidrs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidrs: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_sagemaker_workforce", namespace="sagemaker")
class Workforce(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this Workforce.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Use this parameter to configure an Amazon Cognito private workforce. A single Cognito wor
    kforce is created using and corresponds to a single Amazon Cognito user pool. Conflicts with `oidc_c
    onfig`. see [Cognito Config](#cognito-config) details below.
    """
    cognito_config: CognitoConfig | None = core.attr(CognitoConfig, default=None)

    """
    The name of the Workforce.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Use this parameter to configure a private workforce using your own OIDC Identity Provider
    . Conflicts with `cognito_config`. see [OIDC Config](#oidc-config) details below.
    """
    oidc_config: OidcConfig | None = core.attr(OidcConfig, default=None)

    """
    (Required) A list of IP address ranges Used to create an allow list of IP addresses for a private wo
    rkforce. By default, a workforce isn't restricted to specific IP addresses. see [Source Ip Config](#
    source-ip-config) details below.
    """
    source_ip_config: SourceIpConfig | None = core.attr(SourceIpConfig, default=None, computed=True)

    """
    The subdomain for your OIDC Identity Provider.
    """
    subdomain: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Workforce (must be unique).
    """
    workforce_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        workforce_name: str | core.StringOut,
        cognito_config: CognitoConfig | None = None,
        oidc_config: OidcConfig | None = None,
        source_ip_config: SourceIpConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workforce.Args(
                workforce_name=workforce_name,
                cognito_config=cognito_config,
                oidc_config=oidc_config,
                source_ip_config=source_ip_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cognito_config: CognitoConfig | None = core.arg(default=None)

        oidc_config: OidcConfig | None = core.arg(default=None)

        source_ip_config: SourceIpConfig | None = core.arg(default=None)

        workforce_name: str | core.StringOut = core.arg()
