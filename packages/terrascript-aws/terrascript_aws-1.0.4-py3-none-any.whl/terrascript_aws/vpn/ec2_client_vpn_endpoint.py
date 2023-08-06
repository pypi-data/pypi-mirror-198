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


@core.resource(type="aws_ec2_client_vpn_endpoint", namespace="vpn")
class Ec2ClientVpnEndpoint(core.Resource):
    """
    The ARN of the Client VPN endpoint.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Information about the authentication method to be used to authenticate clients.
    """
    authentication_options: list[AuthenticationOptions] | core.ArrayOut[
        AuthenticationOptions
    ] = core.attr(AuthenticationOptions, kind=core.Kind.array)

    """
    (Required) The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The a
    ddress range cannot overlap with the local CIDR of the VPC in which the associated subnet is located
    , or the routes that you add manually. The address range cannot be changed after the Client VPN endp
    oint has been created. The CIDR block should be /22 or greater.
    """
    client_cidr_block: str | core.StringOut = core.attr(str)

    """
    (Optional) The options for managing connection authorization for new client connections.
    """
    client_connect_options: ClientConnectOptions | None = core.attr(
        ClientConnectOptions, default=None, computed=True
    )

    """
    (Optional) Options for enabling a customizable text banner that will be displayed on AWS provided cl
    ients when a VPN session is established.
    """
    client_login_banner_options: ClientLoginBannerOptions | None = core.attr(
        ClientLoginBannerOptions, default=None, computed=True
    )

    """
    (Required) Information about the client connection logging options.
    """
    connection_log_options: ConnectionLogOptions = core.attr(ConnectionLogOptions)

    """
    (Optional) A brief description of the Client VPN endpoint.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The DNS name to be used by clients when establishing their VPN session.
    """
    dns_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint ca
    n have up to two DNS servers. If no DNS server is specified, the DNS address of the connecting devic
    e is used.
    """
    dns_servers: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the Client VPN endpoint.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The IDs of one or more security groups to apply to the target network. You must also spec
    ify the ID of the VPC that contains the security groups.
    """
    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Specify whether to enable the self-service portal for the Client VPN endpoint. Values can
    be `enabled` or `disabled`. Default value is `disabled`.
    """
    self_service_portal: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ARN of the ACM server certificate.
    """
    server_certificate_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) The maximum session duration is a trigger by which end-users are required to re-authentic
    ate prior to establishing a VPN session. Default value is `24` - Valid values: `8 | 10 | 12 | 24`
    """
    session_timeout_hours: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) Indicates whether split-tunnel is enabled on VPN endpoint. Default value is `false`.
    """
    split_tunnel: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    **Deprecated** The current state of the Client VPN endpoint.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A mapping of tags to assign to the resource. If configured with a provider [`default_tags
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tag
    s-configuration-block) present, tags with matching keys will overwrite those defined at the provider
    level.
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
    (Optional) The transport protocol to be used by the VPN session. Default value is `udp`.
    """
    transport_protocol: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are
    specified in the request, the default security group for the VPC is applied.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The port number for the Client VPN endpoint. Valid values are `443` and `1194`. Default v
    alue is `443`.
    """
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
