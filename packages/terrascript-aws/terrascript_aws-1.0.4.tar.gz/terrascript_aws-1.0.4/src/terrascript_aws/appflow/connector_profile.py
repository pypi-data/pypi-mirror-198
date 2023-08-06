import terrascript.core as core


@core.schema
class ConnectorProfileCredentialsDynatrace(core.Schema):

    api_token: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        api_token: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsDynatrace.Args(
                api_token=api_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_token: str | core.StringOut = core.arg()


@core.schema
class OauthRequest(core.Schema):

    auth_code: str | core.StringOut | None = core.attr(str, default=None)

    redirect_uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auth_code: str | core.StringOut | None = None,
        redirect_uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OauthRequest.Args(
                auth_code=auth_code,
                redirect_uri=redirect_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_code: str | core.StringOut | None = core.arg(default=None)

        redirect_uri: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsGoogleAnalytics(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    refresh_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        access_token: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
        refresh_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsGoogleAnalytics.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        oauth_request: OauthRequest | None = core.arg(default=None)

        refresh_token: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsSingular(core.Schema):

    api_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        api_key: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSingular.Args(
                api_key=api_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsSnowflake(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSnowflake.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsMarketo(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        access_token: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsMarketo.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        oauth_request: OauthRequest | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsZendesk(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        access_token: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsZendesk.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        oauth_request: OauthRequest | None = core.arg(default=None)


@core.schema
class BasicAuthCredentials(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=BasicAuthCredentials.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class OauthCredentials(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    refresh_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        access_token: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
        refresh_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OauthCredentials.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        oauth_request: OauthRequest | None = core.arg(default=None)

        refresh_token: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsSapoData(core.Schema):

    basic_auth_credentials: BasicAuthCredentials | None = core.attr(
        BasicAuthCredentials, default=None
    )

    oauth_credentials: OauthCredentials | None = core.attr(OauthCredentials, default=None)

    def __init__(
        self,
        *,
        basic_auth_credentials: BasicAuthCredentials | None = None,
        oauth_credentials: OauthCredentials | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSapoData.Args(
                basic_auth_credentials=basic_auth_credentials,
                oauth_credentials=oauth_credentials,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        basic_auth_credentials: BasicAuthCredentials | None = core.arg(default=None)

        oauth_credentials: OauthCredentials | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsRedshift(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsRedshift.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsInforNexus(core.Schema):

    access_key_id: str | core.StringOut = core.attr(str)

    datakey: str | core.StringOut = core.attr(str)

    secret_access_key: str | core.StringOut = core.attr(str)

    user_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        access_key_id: str | core.StringOut,
        datakey: str | core.StringOut,
        secret_access_key: str | core.StringOut,
        user_id: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsInforNexus.Args(
                access_key_id=access_key_id,
                datakey=datakey,
                secret_access_key=secret_access_key,
                user_id=user_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_key_id: str | core.StringOut = core.arg()

        datakey: str | core.StringOut = core.arg()

        secret_access_key: str | core.StringOut = core.arg()

        user_id: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsTrendmicro(core.Schema):

    api_secret_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        api_secret_key: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsTrendmicro.Args(
                api_secret_key=api_secret_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_secret_key: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsDatadog(core.Schema):

    api_key: str | core.StringOut = core.attr(str)

    application_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        api_key: str | core.StringOut,
        application_key: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsDatadog.Args(
                api_key=api_key,
                application_key=application_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: str | core.StringOut = core.arg()

        application_key: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsVeeva(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsVeeva.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsAmplitude(core.Schema):

    api_key: str | core.StringOut = core.attr(str)

    secret_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        api_key: str | core.StringOut,
        secret_key: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsAmplitude.Args(
                api_key=api_key,
                secret_key=secret_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: str | core.StringOut = core.arg()

        secret_key: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsServiceNow(core.Schema):

    password: str | core.StringOut = core.attr(str)

    username: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        password: str | core.StringOut,
        username: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsServiceNow.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut = core.arg()

        username: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfileCredentialsSlack(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut,
        client_secret: str | core.StringOut,
        access_token: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSlack.Args(
                client_id=client_id,
                client_secret=client_secret,
                access_token=access_token,
                oauth_request=oauth_request,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_id: str | core.StringOut = core.arg()

        client_secret: str | core.StringOut = core.arg()

        oauth_request: OauthRequest | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsHoneycode(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    refresh_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
        refresh_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsHoneycode.Args(
                access_token=access_token,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        oauth_request: OauthRequest | None = core.arg(default=None)

        refresh_token: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentialsSalesforce(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_credentials_arn: str | core.StringOut | None = core.attr(str, default=None)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    refresh_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: str | core.StringOut | None = None,
        client_credentials_arn: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
        refresh_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsSalesforce.Args(
                access_token=access_token,
                client_credentials_arn=client_credentials_arn,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_credentials_arn: str | core.StringOut | None = core.arg(default=None)

        oauth_request: OauthRequest | None = core.arg(default=None)

        refresh_token: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Custom(core.Schema):

    credentials_map: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    custom_authentication_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        custom_authentication_type: str | core.StringOut,
        credentials_map: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Custom.Args(
                custom_authentication_type=custom_authentication_type,
                credentials_map=credentials_map,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials_map: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        custom_authentication_type: str | core.StringOut = core.arg()


@core.schema
class Oauth2(core.Schema):

    access_token: str | core.StringOut | None = core.attr(str, default=None)

    client_id: str | core.StringOut | None = core.attr(str, default=None)

    client_secret: str | core.StringOut | None = core.attr(str, default=None)

    oauth_request: OauthRequest | None = core.attr(OauthRequest, default=None)

    refresh_token: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_token: str | core.StringOut | None = None,
        client_id: str | core.StringOut | None = None,
        client_secret: str | core.StringOut | None = None,
        oauth_request: OauthRequest | None = None,
        refresh_token: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Oauth2.Args(
                access_token=access_token,
                client_id=client_id,
                client_secret=client_secret,
                oauth_request=oauth_request,
                refresh_token=refresh_token,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_token: str | core.StringOut | None = core.arg(default=None)

        client_id: str | core.StringOut | None = core.arg(default=None)

        client_secret: str | core.StringOut | None = core.arg(default=None)

        oauth_request: OauthRequest | None = core.arg(default=None)

        refresh_token: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ApiKey(core.Schema):

    api_key: str | core.StringOut = core.attr(str)

    api_secret_key: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        api_key: str | core.StringOut,
        api_secret_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ApiKey.Args(
                api_key=api_key,
                api_secret_key=api_secret_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: str | core.StringOut = core.arg()

        api_secret_key: str | core.StringOut | None = core.arg(default=None)


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
class ConnectorProfileCredentialsCustomConnector(core.Schema):

    api_key: ApiKey | None = core.attr(ApiKey, default=None)

    authentication_type: str | core.StringOut = core.attr(str)

    basic: Basic | None = core.attr(Basic, default=None)

    custom: Custom | None = core.attr(Custom, default=None)

    oauth2: Oauth2 | None = core.attr(Oauth2, default=None)

    def __init__(
        self,
        *,
        authentication_type: str | core.StringOut,
        api_key: ApiKey | None = None,
        basic: Basic | None = None,
        custom: Custom | None = None,
        oauth2: Oauth2 | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentialsCustomConnector.Args(
                authentication_type=authentication_type,
                api_key=api_key,
                basic=basic,
                custom=custom,
                oauth2=oauth2,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        api_key: ApiKey | None = core.arg(default=None)

        authentication_type: str | core.StringOut = core.arg()

        basic: Basic | None = core.arg(default=None)

        custom: Custom | None = core.arg(default=None)

        oauth2: Oauth2 | None = core.arg(default=None)


@core.schema
class ConnectorProfileCredentials(core.Schema):

    amplitude: ConnectorProfileCredentialsAmplitude | None = core.attr(
        ConnectorProfileCredentialsAmplitude, default=None
    )

    custom_connector: ConnectorProfileCredentialsCustomConnector | None = core.attr(
        ConnectorProfileCredentialsCustomConnector, default=None
    )

    datadog: ConnectorProfileCredentialsDatadog | None = core.attr(
        ConnectorProfileCredentialsDatadog, default=None
    )

    dynatrace: ConnectorProfileCredentialsDynatrace | None = core.attr(
        ConnectorProfileCredentialsDynatrace, default=None
    )

    google_analytics: ConnectorProfileCredentialsGoogleAnalytics | None = core.attr(
        ConnectorProfileCredentialsGoogleAnalytics, default=None
    )

    honeycode: ConnectorProfileCredentialsHoneycode | None = core.attr(
        ConnectorProfileCredentialsHoneycode, default=None
    )

    infor_nexus: ConnectorProfileCredentialsInforNexus | None = core.attr(
        ConnectorProfileCredentialsInforNexus, default=None
    )

    marketo: ConnectorProfileCredentialsMarketo | None = core.attr(
        ConnectorProfileCredentialsMarketo, default=None
    )

    redshift: ConnectorProfileCredentialsRedshift | None = core.attr(
        ConnectorProfileCredentialsRedshift, default=None
    )

    salesforce: ConnectorProfileCredentialsSalesforce | None = core.attr(
        ConnectorProfileCredentialsSalesforce, default=None
    )

    sapo_data: ConnectorProfileCredentialsSapoData | None = core.attr(
        ConnectorProfileCredentialsSapoData, default=None
    )

    service_now: ConnectorProfileCredentialsServiceNow | None = core.attr(
        ConnectorProfileCredentialsServiceNow, default=None
    )

    singular: ConnectorProfileCredentialsSingular | None = core.attr(
        ConnectorProfileCredentialsSingular, default=None
    )

    slack: ConnectorProfileCredentialsSlack | None = core.attr(
        ConnectorProfileCredentialsSlack, default=None
    )

    snowflake: ConnectorProfileCredentialsSnowflake | None = core.attr(
        ConnectorProfileCredentialsSnowflake, default=None
    )

    trendmicro: ConnectorProfileCredentialsTrendmicro | None = core.attr(
        ConnectorProfileCredentialsTrendmicro, default=None
    )

    veeva: ConnectorProfileCredentialsVeeva | None = core.attr(
        ConnectorProfileCredentialsVeeva, default=None
    )

    zendesk: ConnectorProfileCredentialsZendesk | None = core.attr(
        ConnectorProfileCredentialsZendesk, default=None
    )

    def __init__(
        self,
        *,
        amplitude: ConnectorProfileCredentialsAmplitude | None = None,
        custom_connector: ConnectorProfileCredentialsCustomConnector | None = None,
        datadog: ConnectorProfileCredentialsDatadog | None = None,
        dynatrace: ConnectorProfileCredentialsDynatrace | None = None,
        google_analytics: ConnectorProfileCredentialsGoogleAnalytics | None = None,
        honeycode: ConnectorProfileCredentialsHoneycode | None = None,
        infor_nexus: ConnectorProfileCredentialsInforNexus | None = None,
        marketo: ConnectorProfileCredentialsMarketo | None = None,
        redshift: ConnectorProfileCredentialsRedshift | None = None,
        salesforce: ConnectorProfileCredentialsSalesforce | None = None,
        sapo_data: ConnectorProfileCredentialsSapoData | None = None,
        service_now: ConnectorProfileCredentialsServiceNow | None = None,
        singular: ConnectorProfileCredentialsSingular | None = None,
        slack: ConnectorProfileCredentialsSlack | None = None,
        snowflake: ConnectorProfileCredentialsSnowflake | None = None,
        trendmicro: ConnectorProfileCredentialsTrendmicro | None = None,
        veeva: ConnectorProfileCredentialsVeeva | None = None,
        zendesk: ConnectorProfileCredentialsZendesk | None = None,
    ):
        super().__init__(
            args=ConnectorProfileCredentials.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                honeycode=honeycode,
                infor_nexus=infor_nexus,
                marketo=marketo,
                redshift=redshift,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                snowflake=snowflake,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: ConnectorProfileCredentialsAmplitude | None = core.arg(default=None)

        custom_connector: ConnectorProfileCredentialsCustomConnector | None = core.arg(default=None)

        datadog: ConnectorProfileCredentialsDatadog | None = core.arg(default=None)

        dynatrace: ConnectorProfileCredentialsDynatrace | None = core.arg(default=None)

        google_analytics: ConnectorProfileCredentialsGoogleAnalytics | None = core.arg(default=None)

        honeycode: ConnectorProfileCredentialsHoneycode | None = core.arg(default=None)

        infor_nexus: ConnectorProfileCredentialsInforNexus | None = core.arg(default=None)

        marketo: ConnectorProfileCredentialsMarketo | None = core.arg(default=None)

        redshift: ConnectorProfileCredentialsRedshift | None = core.arg(default=None)

        salesforce: ConnectorProfileCredentialsSalesforce | None = core.arg(default=None)

        sapo_data: ConnectorProfileCredentialsSapoData | None = core.arg(default=None)

        service_now: ConnectorProfileCredentialsServiceNow | None = core.arg(default=None)

        singular: ConnectorProfileCredentialsSingular | None = core.arg(default=None)

        slack: ConnectorProfileCredentialsSlack | None = core.arg(default=None)

        snowflake: ConnectorProfileCredentialsSnowflake | None = core.arg(default=None)

        trendmicro: ConnectorProfileCredentialsTrendmicro | None = core.arg(default=None)

        veeva: ConnectorProfileCredentialsVeeva | None = core.arg(default=None)

        zendesk: ConnectorProfileCredentialsZendesk | None = core.arg(default=None)


@core.schema
class ConnectorProfilePropertiesHoneycode(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfilePropertiesVeeva(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesVeeva.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesZendesk(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesZendesk.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesSingular(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfilePropertiesMarketo(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesMarketo.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesTrendmicro(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfilePropertiesDatadog(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesDatadog.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesSalesforce(core.Schema):

    instance_url: str | core.StringOut | None = core.attr(str, default=None)

    is_sandbox_environment: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut | None = None,
        is_sandbox_environment: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSalesforce.Args(
                instance_url=instance_url,
                is_sandbox_environment=is_sandbox_environment,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut | None = core.arg(default=None)

        is_sandbox_environment: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Oauth2Properties(core.Schema):

    oauth2_grant_type: str | core.StringOut = core.attr(str)

    token_url: str | core.StringOut = core.attr(str)

    token_url_custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        oauth2_grant_type: str | core.StringOut,
        token_url: str | core.StringOut,
        token_url_custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Oauth2Properties.Args(
                oauth2_grant_type=oauth2_grant_type,
                token_url=token_url,
                token_url_custom_properties=token_url_custom_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        oauth2_grant_type: str | core.StringOut = core.arg()

        token_url: str | core.StringOut = core.arg()

        token_url_custom_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class ConnectorProfilePropertiesCustomConnector(core.Schema):

    oauth2_properties: Oauth2Properties | None = core.attr(Oauth2Properties, default=None)

    profile_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        oauth2_properties: Oauth2Properties | None = None,
        profile_properties: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesCustomConnector.Args(
                oauth2_properties=oauth2_properties,
                profile_properties=profile_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        oauth2_properties: Oauth2Properties | None = core.arg(default=None)

        profile_properties: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.schema
class ConnectorProfilePropertiesRedshift(core.Schema):

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    database_url: str | core.StringOut | None = core.attr(str, default=None)

    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        role_arn: str | core.StringOut,
        bucket_prefix: str | core.StringOut | None = None,
        database_url: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesRedshift.Args(
                bucket_name=bucket_name,
                role_arn=role_arn,
                bucket_prefix=bucket_prefix,
                database_url=database_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        database_url: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesDynatrace(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesDynatrace.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesAmplitude(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class OauthProperties(core.Schema):

    auth_code_url: str | core.StringOut = core.attr(str)

    oauth_scopes: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    token_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        auth_code_url: str | core.StringOut,
        oauth_scopes: list[str] | core.ArrayOut[core.StringOut],
        token_url: str | core.StringOut,
    ):
        super().__init__(
            args=OauthProperties.Args(
                auth_code_url=auth_code_url,
                oauth_scopes=oauth_scopes,
                token_url=token_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_code_url: str | core.StringOut = core.arg()

        oauth_scopes: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        token_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesSapoData(core.Schema):

    application_host_url: str | core.StringOut = core.attr(str)

    application_service_path: str | core.StringOut = core.attr(str)

    client_number: str | core.StringOut = core.attr(str)

    logon_language: str | core.StringOut | None = core.attr(str, default=None)

    oauth_properties: OauthProperties | None = core.attr(OauthProperties, default=None)

    port_number: int | core.IntOut = core.attr(int)

    private_link_service_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        application_host_url: str | core.StringOut,
        application_service_path: str | core.StringOut,
        client_number: str | core.StringOut,
        port_number: int | core.IntOut,
        logon_language: str | core.StringOut | None = None,
        oauth_properties: OauthProperties | None = None,
        private_link_service_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSapoData.Args(
                application_host_url=application_host_url,
                application_service_path=application_service_path,
                client_number=client_number,
                port_number=port_number,
                logon_language=logon_language,
                oauth_properties=oauth_properties,
                private_link_service_name=private_link_service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_host_url: str | core.StringOut = core.arg()

        application_service_path: str | core.StringOut = core.arg()

        client_number: str | core.StringOut = core.arg()

        logon_language: str | core.StringOut | None = core.arg(default=None)

        oauth_properties: OauthProperties | None = core.arg(default=None)

        port_number: int | core.IntOut = core.arg()

        private_link_service_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ConnectorProfilePropertiesInforNexus(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesInforNexus.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesServiceNow(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesServiceNow.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesSlack(core.Schema):

    instance_url: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        instance_url: str | core.StringOut,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSlack.Args(
                instance_url=instance_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_url: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesSnowflake(core.Schema):

    account_name: str | core.StringOut | None = core.attr(str, default=None)

    bucket_name: str | core.StringOut = core.attr(str)

    bucket_prefix: str | core.StringOut | None = core.attr(str, default=None)

    private_link_service_name: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None)

    stage: str | core.StringOut = core.attr(str)

    warehouse: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: str | core.StringOut,
        stage: str | core.StringOut,
        warehouse: str | core.StringOut,
        account_name: str | core.StringOut | None = None,
        bucket_prefix: str | core.StringOut | None = None,
        private_link_service_name: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectorProfilePropertiesSnowflake.Args(
                bucket_name=bucket_name,
                stage=stage,
                warehouse=warehouse,
                account_name=account_name,
                bucket_prefix=bucket_prefix,
                private_link_service_name=private_link_service_name,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_name: str | core.StringOut | None = core.arg(default=None)

        bucket_name: str | core.StringOut = core.arg()

        bucket_prefix: str | core.StringOut | None = core.arg(default=None)

        private_link_service_name: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        stage: str | core.StringOut = core.arg()

        warehouse: str | core.StringOut = core.arg()


@core.schema
class ConnectorProfilePropertiesGoogleAnalytics(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class ConnectorProfileProperties(core.Schema):

    amplitude: ConnectorProfilePropertiesAmplitude | None = core.attr(
        ConnectorProfilePropertiesAmplitude, default=None
    )

    custom_connector: ConnectorProfilePropertiesCustomConnector | None = core.attr(
        ConnectorProfilePropertiesCustomConnector, default=None
    )

    datadog: ConnectorProfilePropertiesDatadog | None = core.attr(
        ConnectorProfilePropertiesDatadog, default=None
    )

    dynatrace: ConnectorProfilePropertiesDynatrace | None = core.attr(
        ConnectorProfilePropertiesDynatrace, default=None
    )

    google_analytics: ConnectorProfilePropertiesGoogleAnalytics | None = core.attr(
        ConnectorProfilePropertiesGoogleAnalytics, default=None
    )

    honeycode: ConnectorProfilePropertiesHoneycode | None = core.attr(
        ConnectorProfilePropertiesHoneycode, default=None
    )

    infor_nexus: ConnectorProfilePropertiesInforNexus | None = core.attr(
        ConnectorProfilePropertiesInforNexus, default=None
    )

    marketo: ConnectorProfilePropertiesMarketo | None = core.attr(
        ConnectorProfilePropertiesMarketo, default=None
    )

    redshift: ConnectorProfilePropertiesRedshift | None = core.attr(
        ConnectorProfilePropertiesRedshift, default=None
    )

    salesforce: ConnectorProfilePropertiesSalesforce | None = core.attr(
        ConnectorProfilePropertiesSalesforce, default=None
    )

    sapo_data: ConnectorProfilePropertiesSapoData | None = core.attr(
        ConnectorProfilePropertiesSapoData, default=None
    )

    service_now: ConnectorProfilePropertiesServiceNow | None = core.attr(
        ConnectorProfilePropertiesServiceNow, default=None
    )

    singular: ConnectorProfilePropertiesSingular | None = core.attr(
        ConnectorProfilePropertiesSingular, default=None
    )

    slack: ConnectorProfilePropertiesSlack | None = core.attr(
        ConnectorProfilePropertiesSlack, default=None
    )

    snowflake: ConnectorProfilePropertiesSnowflake | None = core.attr(
        ConnectorProfilePropertiesSnowflake, default=None
    )

    trendmicro: ConnectorProfilePropertiesTrendmicro | None = core.attr(
        ConnectorProfilePropertiesTrendmicro, default=None
    )

    veeva: ConnectorProfilePropertiesVeeva | None = core.attr(
        ConnectorProfilePropertiesVeeva, default=None
    )

    zendesk: ConnectorProfilePropertiesZendesk | None = core.attr(
        ConnectorProfilePropertiesZendesk, default=None
    )

    def __init__(
        self,
        *,
        amplitude: ConnectorProfilePropertiesAmplitude | None = None,
        custom_connector: ConnectorProfilePropertiesCustomConnector | None = None,
        datadog: ConnectorProfilePropertiesDatadog | None = None,
        dynatrace: ConnectorProfilePropertiesDynatrace | None = None,
        google_analytics: ConnectorProfilePropertiesGoogleAnalytics | None = None,
        honeycode: ConnectorProfilePropertiesHoneycode | None = None,
        infor_nexus: ConnectorProfilePropertiesInforNexus | None = None,
        marketo: ConnectorProfilePropertiesMarketo | None = None,
        redshift: ConnectorProfilePropertiesRedshift | None = None,
        salesforce: ConnectorProfilePropertiesSalesforce | None = None,
        sapo_data: ConnectorProfilePropertiesSapoData | None = None,
        service_now: ConnectorProfilePropertiesServiceNow | None = None,
        singular: ConnectorProfilePropertiesSingular | None = None,
        slack: ConnectorProfilePropertiesSlack | None = None,
        snowflake: ConnectorProfilePropertiesSnowflake | None = None,
        trendmicro: ConnectorProfilePropertiesTrendmicro | None = None,
        veeva: ConnectorProfilePropertiesVeeva | None = None,
        zendesk: ConnectorProfilePropertiesZendesk | None = None,
    ):
        super().__init__(
            args=ConnectorProfileProperties.Args(
                amplitude=amplitude,
                custom_connector=custom_connector,
                datadog=datadog,
                dynatrace=dynatrace,
                google_analytics=google_analytics,
                honeycode=honeycode,
                infor_nexus=infor_nexus,
                marketo=marketo,
                redshift=redshift,
                salesforce=salesforce,
                sapo_data=sapo_data,
                service_now=service_now,
                singular=singular,
                slack=slack,
                snowflake=snowflake,
                trendmicro=trendmicro,
                veeva=veeva,
                zendesk=zendesk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amplitude: ConnectorProfilePropertiesAmplitude | None = core.arg(default=None)

        custom_connector: ConnectorProfilePropertiesCustomConnector | None = core.arg(default=None)

        datadog: ConnectorProfilePropertiesDatadog | None = core.arg(default=None)

        dynatrace: ConnectorProfilePropertiesDynatrace | None = core.arg(default=None)

        google_analytics: ConnectorProfilePropertiesGoogleAnalytics | None = core.arg(default=None)

        honeycode: ConnectorProfilePropertiesHoneycode | None = core.arg(default=None)

        infor_nexus: ConnectorProfilePropertiesInforNexus | None = core.arg(default=None)

        marketo: ConnectorProfilePropertiesMarketo | None = core.arg(default=None)

        redshift: ConnectorProfilePropertiesRedshift | None = core.arg(default=None)

        salesforce: ConnectorProfilePropertiesSalesforce | None = core.arg(default=None)

        sapo_data: ConnectorProfilePropertiesSapoData | None = core.arg(default=None)

        service_now: ConnectorProfilePropertiesServiceNow | None = core.arg(default=None)

        singular: ConnectorProfilePropertiesSingular | None = core.arg(default=None)

        slack: ConnectorProfilePropertiesSlack | None = core.arg(default=None)

        snowflake: ConnectorProfilePropertiesSnowflake | None = core.arg(default=None)

        trendmicro: ConnectorProfilePropertiesTrendmicro | None = core.arg(default=None)

        veeva: ConnectorProfilePropertiesVeeva | None = core.arg(default=None)

        zendesk: ConnectorProfilePropertiesZendesk | None = core.arg(default=None)


@core.schema
class ConnectorProfileConfig(core.Schema):

    connector_profile_credentials: ConnectorProfileCredentials = core.attr(
        ConnectorProfileCredentials
    )

    connector_profile_properties: ConnectorProfileProperties = core.attr(ConnectorProfileProperties)

    def __init__(
        self,
        *,
        connector_profile_credentials: ConnectorProfileCredentials,
        connector_profile_properties: ConnectorProfileProperties,
    ):
        super().__init__(
            args=ConnectorProfileConfig.Args(
                connector_profile_credentials=connector_profile_credentials,
                connector_profile_properties=connector_profile_properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connector_profile_credentials: ConnectorProfileCredentials = core.arg()

        connector_profile_properties: ConnectorProfileProperties = core.arg()


@core.resource(type="aws_appflow_connector_profile", namespace="appflow")
class ConnectorProfile(core.Resource):
    """
    The Amazon Resource Name (ARN) of the connector profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    connection_mode: str | core.StringOut = core.attr(str)

    connector_label: str | core.StringOut | None = core.attr(str, default=None)

    connector_profile_config: ConnectorProfileConfig = core.attr(ConnectorProfileConfig)

    connector_type: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the connector profile credentials.
    """
    credentials_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_mode: str | core.StringOut,
        connector_profile_config: ConnectorProfileConfig,
        connector_type: str | core.StringOut,
        name: str | core.StringOut,
        connector_label: str | core.StringOut | None = None,
        kms_arn: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConnectorProfile.Args(
                connection_mode=connection_mode,
                connector_profile_config=connector_profile_config,
                connector_type=connector_type,
                name=name,
                connector_label=connector_label,
                kms_arn=kms_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_mode: str | core.StringOut = core.arg()

        connector_label: str | core.StringOut | None = core.arg(default=None)

        connector_profile_config: ConnectorProfileConfig = core.arg()

        connector_type: str | core.StringOut = core.arg()

        kms_arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()
