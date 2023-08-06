import terrascript.core as core


@core.schema
class AuthenticationOptions(core.Schema):

    active_directory_id: str | core.StringOut = core.attr(str, computed=True)

    root_certificate_chain_arn: str | core.StringOut = core.attr(str, computed=True)

    saml_provider_arn: str | core.StringOut = core.attr(str, computed=True)

    self_service_saml_provider_arn: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        active_directory_id: str | core.StringOut,
        root_certificate_chain_arn: str | core.StringOut,
        saml_provider_arn: str | core.StringOut,
        self_service_saml_provider_arn: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=AuthenticationOptions.Args(
                active_directory_id=active_directory_id,
                root_certificate_chain_arn=root_certificate_chain_arn,
                saml_provider_arn=saml_provider_arn,
                self_service_saml_provider_arn=self_service_saml_provider_arn,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_directory_id: str | core.StringOut = core.arg()

        root_certificate_chain_arn: str | core.StringOut = core.arg()

        saml_provider_arn: str | core.StringOut = core.arg()

        self_service_saml_provider_arn: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class ConnectionLogOptions(core.Schema):

    cloudwatch_log_group: str | core.StringOut = core.attr(str, computed=True)

    cloudwatch_log_stream: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        cloudwatch_log_group: str | core.StringOut,
        cloudwatch_log_stream: str | core.StringOut,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=ConnectionLogOptions.Args(
                cloudwatch_log_group=cloudwatch_log_group,
                cloudwatch_log_stream=cloudwatch_log_stream,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group: str | core.StringOut = core.arg()

        cloudwatch_log_stream: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()


@core.schema
class ClientLoginBannerOptions(core.Schema):

    banner_text: str | core.StringOut = core.attr(str, computed=True)

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        banner_text: str | core.StringOut,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=ClientLoginBannerOptions.Args(
                banner_text=banner_text,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        banner_text: str | core.StringOut = core.arg()

        enabled: bool | core.BoolOut = core.arg()


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class ClientConnectOptions(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool, computed=True)

    lambda_function_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
        lambda_function_arn: str | core.StringOut,
    ):
        super().__init__(
            args=ClientConnectOptions.Args(
                enabled=enabled,
                lambda_function_arn=lambda_function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()

        lambda_function_arn: str | core.StringOut = core.arg()


@core.data(type="aws_ec2_client_vpn_endpoint", namespace="vpn")
class DsEc2ClientVpnEndpoint(core.Data):
    """
    The ARN of the Client VPN endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Information about the authentication method used by the Client VPN endpoint.
    """
    authentication_options: list[AuthenticationOptions] | core.ArrayOut[
        AuthenticationOptions
    ] = core.attr(AuthenticationOptions, computed=True, kind=core.Kind.array)

    """
    The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.
    """
    client_cidr_block: str | core.StringOut = core.attr(str, computed=True)

    """
    The options for managing connection authorization for new client connections.
    """
    client_connect_options: list[ClientConnectOptions] | core.ArrayOut[
        ClientConnectOptions
    ] = core.attr(ClientConnectOptions, computed=True, kind=core.Kind.array)

    """
    Options for enabling a customizable text banner that will be displayed on AWS provided clients when
    a VPN session is established.
    """
    client_login_banner_options: list[ClientLoginBannerOptions] | core.ArrayOut[
        ClientLoginBannerOptions
    ] = core.attr(ClientLoginBannerOptions, computed=True, kind=core.Kind.array)

    """
    (Optional) The ID of the Client VPN endpoint.
    """
    client_vpn_endpoint_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    Information about the client connection logging options for the Client VPN endpoint.
    """
    connection_log_options: list[ConnectionLogOptions] | core.ArrayOut[
        ConnectionLogOptions
    ] = core.attr(ConnectionLogOptions, computed=True, kind=core.Kind.array)

    """
    A brief description of the endpoint.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The DNS name to be used by clients when connecting to the Client VPN endpoint.
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    Information about the DNS servers to be used for DNS resolution.
    """
    dns_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) One or more configuration blocks containing name-values filters. Detailed below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IDs of the security groups for the target network associated with the Client VPN endpoint.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Indicates whether the self-service portal for the Client VPN endpoint is enabled.
    """
    self_service_portal: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the server certificate.
    """
    server_certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The maximum VPN session duration time in hours.
    """
    session_timeout_hours: int | core.IntOut = core.attr(int, computed=True)

    """
    Indicates whether split-tunnel is enabled in the AWS Client VPN endpoint.
    """
    split_tunnel: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Map of tags, each pair of which must exactly match a pair on the desired endpoint.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The transport protocol used by the Client VPN endpoint.
    """
    transport_protocol: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the VPC associated with the Client VPN endpoint.
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The port number for the Client VPN endpoint.
    """
    vpn_port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        client_vpn_endpoint_id: str | core.StringOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2ClientVpnEndpoint.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                filter=filter,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_vpn_endpoint_id: str | core.StringOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
