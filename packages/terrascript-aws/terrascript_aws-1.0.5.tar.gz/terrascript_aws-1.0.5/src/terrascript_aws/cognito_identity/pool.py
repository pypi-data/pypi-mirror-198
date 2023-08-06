import terrascript.core as core


@core.schema
class CognitoIdentityProviders(core.Schema):

    client_id: str | core.StringOut | None = core.attr(str, default=None)

    provider_name: str | core.StringOut | None = core.attr(str, default=None)

    server_side_token_check: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        client_id: str | core.StringOut | None = None,
        provider_name: str | core.StringOut | None = None,
        server_side_token_check: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CognitoIdentityProviders.Args(
                client_id=client_id,
                provider_name=provider_name,
                server_side_token_check=server_side_token_check,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: str | core.StringOut | None = core.arg(default=None)

        provider_name: str | core.StringOut | None = core.arg(default=None)

        server_side_token_check: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_cognito_identity_pool", namespace="cognito_identity")
class Pool(core.Resource):

    allow_classic_flow: bool | core.BoolOut | None = core.attr(bool, default=None)

    allow_unauthenticated_identities: bool | core.BoolOut | None = core.attr(bool, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cognito_identity_providers: list[CognitoIdentityProviders] | core.ArrayOut[
        CognitoIdentityProviders
    ] | None = core.attr(CognitoIdentityProviders, default=None, kind=core.Kind.array)

    developer_provider_name: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_pool_name: str | core.StringOut = core.attr(str)

    openid_connect_provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    saml_provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    supported_login_providers: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        identity_pool_name: str | core.StringOut,
        allow_classic_flow: bool | core.BoolOut | None = None,
        allow_unauthenticated_identities: bool | core.BoolOut | None = None,
        cognito_identity_providers: list[CognitoIdentityProviders]
        | core.ArrayOut[CognitoIdentityProviders]
        | None = None,
        developer_provider_name: str | core.StringOut | None = None,
        openid_connect_provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        saml_provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        supported_login_providers: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Pool.Args(
                identity_pool_name=identity_pool_name,
                allow_classic_flow=allow_classic_flow,
                allow_unauthenticated_identities=allow_unauthenticated_identities,
                cognito_identity_providers=cognito_identity_providers,
                developer_provider_name=developer_provider_name,
                openid_connect_provider_arns=openid_connect_provider_arns,
                saml_provider_arns=saml_provider_arns,
                supported_login_providers=supported_login_providers,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_classic_flow: bool | core.BoolOut | None = core.arg(default=None)

        allow_unauthenticated_identities: bool | core.BoolOut | None = core.arg(default=None)

        cognito_identity_providers: list[CognitoIdentityProviders] | core.ArrayOut[
            CognitoIdentityProviders
        ] | None = core.arg(default=None)

        developer_provider_name: str | core.StringOut | None = core.arg(default=None)

        identity_pool_name: str | core.StringOut = core.arg()

        openid_connect_provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        saml_provider_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        supported_login_providers: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
