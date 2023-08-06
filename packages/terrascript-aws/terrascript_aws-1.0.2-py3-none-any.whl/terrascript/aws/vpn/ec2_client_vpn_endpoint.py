import terrascript.core as core


@core.schema
class ConnectionLogOptions(core.Schema):

    cloudwatch_log_group: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatch_log_stream: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        cloudwatch_log_group: str | core.StringOut | None = None,
        cloudwatch_log_stream: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ConnectionLogOptions.Args(
                enabled=enabled,
                cloudwatch_log_group=cloudwatch_log_group,
                cloudwatch_log_stream=cloudwatch_log_stream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group: str | core.StringOut | None = core.arg(default=None)

        cloudwatch_log_stream: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut = core.arg()


@core.schema
class ClientConnectOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    lambda_function_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        lambda_function_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ClientConnectOptions.Args(
                enabled=enabled,
                lambda_function_arn=lambda_function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        lambda_function_arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ClientLoginBannerOptions(core.Schema):

    banner_text: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        banner_text: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=ClientLoginBannerOptions.Args(
                banner_text=banner_text,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        banner_text: str | core.StringOut | None = core.arg(default=None)

        enabled: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class AuthenticationOptions(core.Schema):

    active_directory_id: str | core.StringOut | None = core.attr(str, default=None)

    root_certificate_chain_arn: str | core.StringOut | None = core.attr(str, default=None)

    saml_provider_arn: str | core.StringOut | None = core.attr(str, default=None)

    self_service_saml_provider_arn: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        active_directory_id: str | core.StringOut | None = None,
        root_certificate_chain_arn: str | core.StringOut | None = None,
        saml_provider_arn: str | core.StringOut | None = None,
        self_service_saml_provider_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AuthenticationOptions.Args(
                type=type,
                active_directory_id=active_directory_id,
                root_certificate_chain_arn=root_certificate_chain_arn,
                saml_provider_arn=saml_provider_arn,
                self_service_saml_provider_arn=self_service_saml_provider_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_directory_id: str | core.StringOut | None = core.arg(default=None)

        root_certificate_chain_arn: str | core.StringOut | None = core.arg(default=None)

        saml_provider_arn: str | core.StringOut | None = core.arg(default=None)

        self_service_saml_provider_arn: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_ec2_client_vpn_endpoint", namespace="aws_vpn")
class Ec2ClientVpnEndpoint(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    authentication_options: list[AuthenticationOptions] | core.ArrayOut[
        AuthenticationOptions
    ] = core.attr(AuthenticationOptions, kind=core.Kind.array)

    client_cidr_block: str | core.StringOut = core.attr(str)

    client_connect_options: ClientConnectOptions | None = core.attr(
        ClientConnectOptions, default=None, computed=True
    )

    client_login_banner_options: ClientLoginBannerOptions | None = core.attr(
        ClientLoginBannerOptions, default=None, computed=True
    )

    connection_log_options: ConnectionLogOptions = core.attr(ConnectionLogOptions)

    description: str | core.StringOut | None = core.attr(str, default=None)

    dns_name: str | core.StringOut = core.attr(str, computed=True)

    dns_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    self_service_portal: str | core.StringOut | None = core.attr(str, default=None)

    server_certificate_arn: str | core.StringOut = core.attr(str)

    session_timeout_hours: int | core.IntOut | None = core.attr(int, default=None)

    split_tunnel: bool | core.BoolOut | None = core.attr(bool, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transport_protocol: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    vpn_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_options: list[AuthenticationOptions] | core.ArrayOut[AuthenticationOptions],
        client_cidr_block: str | core.StringOut,
        connection_log_options: ConnectionLogOptions,
        server_certificate_arn: str | core.StringOut,
        client_connect_options: ClientConnectOptions | None = None,
        client_login_banner_options: ClientLoginBannerOptions | None = None,
        description: str | core.StringOut | None = None,
        dns_servers: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_service_portal: str | core.StringOut | None = None,
        session_timeout_hours: int | core.IntOut | None = None,
        split_tunnel: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transport_protocol: str | core.StringOut | None = None,
        vpc_id: str | core.StringOut | None = None,
        vpn_port: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnEndpoint.Args(
                authentication_options=authentication_options,
                client_cidr_block=client_cidr_block,
                connection_log_options=connection_log_options,
                server_certificate_arn=server_certificate_arn,
                client_connect_options=client_connect_options,
                client_login_banner_options=client_login_banner_options,
                description=description,
                dns_servers=dns_servers,
                security_group_ids=security_group_ids,
                self_service_portal=self_service_portal,
                session_timeout_hours=session_timeout_hours,
                split_tunnel=split_tunnel,
                tags=tags,
                tags_all=tags_all,
                transport_protocol=transport_protocol,
                vpc_id=vpc_id,
                vpn_port=vpn_port,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_options: list[AuthenticationOptions] | core.ArrayOut[
            AuthenticationOptions
        ] = core.arg()

        client_cidr_block: str | core.StringOut = core.arg()

        client_connect_options: ClientConnectOptions | None = core.arg(default=None)

        client_login_banner_options: ClientLoginBannerOptions | None = core.arg(default=None)

        connection_log_options: ConnectionLogOptions = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        dns_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        self_service_portal: str | core.StringOut | None = core.arg(default=None)

        server_certificate_arn: str | core.StringOut = core.arg()

        session_timeout_hours: int | core.IntOut | None = core.arg(default=None)

        split_tunnel: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transport_protocol: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)

        vpn_port: int | core.IntOut | None = core.arg(default=None)
