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


@core.data(type="aws_cognito_user_pool_client", namespace="cognito")
class DsUserPoolClient(core.Data):

    access_token_validity: int | core.IntOut = core.attr(int, computed=True)

    allowed_oauth_flows: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    allowed_oauth_flows_user_pool_client: bool | core.BoolOut = core.attr(bool, computed=True)

    allowed_oauth_scopes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    analytics_configuration: list[AnalyticsConfiguration] | core.ArrayOut[
        AnalyticsConfiguration
    ] = core.attr(AnalyticsConfiguration, computed=True, kind=core.Kind.array)

    callback_urls: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    client_id: str | core.StringOut = core.attr(str)

    client_secret: str | core.StringOut = core.attr(str, computed=True)

    default_redirect_uri: str | core.StringOut = core.attr(str, computed=True)

    enable_propagate_additional_user_context_data: bool | core.BoolOut = core.attr(
        bool, computed=True
    )

    enable_token_revocation: bool | core.BoolOut = core.attr(bool, computed=True)

    explicit_auth_flows: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    generate_secret: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    id_token_validity: int | core.IntOut = core.attr(int, computed=True)

    logout_urls: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str, computed=True)

    prevent_user_existence_errors: str | core.StringOut = core.attr(str, computed=True)

    read_attributes: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    refresh_token_validity: int | core.IntOut = core.attr(int, computed=True)

    supported_identity_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    token_validity_units: list[TokenValidityUnits] | core.ArrayOut[TokenValidityUnits] = core.attr(
        TokenValidityUnits, computed=True, kind=core.Kind.array
    )

    user_pool_id: str | core.StringOut = core.attr(str)

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
