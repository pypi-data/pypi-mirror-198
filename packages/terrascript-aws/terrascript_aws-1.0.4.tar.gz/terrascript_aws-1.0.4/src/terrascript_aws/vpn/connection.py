import terrascript.core as core


@core.schema
class VgwTelemetry(core.Schema):

    accepted_route_count: int | core.IntOut = core.attr(int, computed=True)

    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    last_status_change: str | core.StringOut = core.attr(str, computed=True)

    outside_ip_address: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    status_message: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        accepted_route_count: int | core.IntOut,
        certificate_arn: str | core.StringOut,
        last_status_change: str | core.StringOut,
        outside_ip_address: str | core.StringOut,
        status: str | core.StringOut,
        status_message: str | core.StringOut,
    ):
        super().__init__(
            args=VgwTelemetry.Args(
                accepted_route_count=accepted_route_count,
                certificate_arn=certificate_arn,
                last_status_change=last_status_change,
                outside_ip_address=outside_ip_address,
                status=status,
                status_message=status_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accepted_route_count: int | core.IntOut = core.arg()

        certificate_arn: str | core.StringOut = core.arg()

        last_status_change: str | core.StringOut = core.arg()

        outside_ip_address: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

        status_message: str | core.StringOut = core.arg()


@core.schema
class Routes(core.Schema):

    destination_cidr_block: str | core.StringOut = core.attr(str, computed=True)

    source: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination_cidr_block: str | core.StringOut,
        source: str | core.StringOut,
        state: str | core.StringOut,
    ):
        super().__init__(
            args=Routes.Args(
                destination_cidr_block=destination_cidr_block,
                source=source,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_cidr_block: str | core.StringOut = core.arg()

        source: str | core.StringOut = core.arg()

        state: str | core.StringOut = core.arg()


@core.resource(type="aws_vpn_connection", namespace="vpn")
class Connection(core.Resource):
    """
    Amazon Resource Name (ARN) of the VPN Connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the core network.
    """
    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the core network attachment.
    """
    core_network_attachment_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The configuration information for the VPN connection's customer gateway (in the native XML format).
    """
    customer_gateway_configuration: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the customer gateway.
    """
    customer_gateway_id: str | core.StringOut = core.attr(str)

    """
    (Optional, Default `false`) Indicate whether to enable acceleration for the VPN connection. Supports
    only EC2 Transit Gateway.
    """
    enable_acceleration: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    The amazon-assigned ID of the VPN connection.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Default `0.0.0.0/0`) The IPv4 CIDR on the customer gateway (on-premises) side of the VPN
    connection.
    """
    local_ipv4_network_cidr: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Default `::/0`) The IPv6 CIDR on the customer gateway (on-premises) side of the VPN conne
    ction.
    """
    local_ipv6_network_cidr: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Default `PublicIpv4`) Indicates if a Public S2S VPN or Private S2S VPN over AWS Direct Co
    nnect. Valid values are `PublicIpv4 | PrivateIpv4`
    """
    outside_ip_address_type: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Default `0.0.0.0/0`) The IPv4 CIDR on the AWS side of the VPN connection.
    """
    remote_ipv4_network_cidr: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional, Default `::/0`) The IPv6 CIDR on the customer gateway (on-premises) side of the VPN conne
    ction.
    """
    remote_ipv6_network_cidr: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The static routes associated with the VPN connection. Detailed below.
    """
    routes: list[Routes] | core.ArrayOut[Routes] = core.attr(
        Routes, computed=True, kind=core.Kind.array
    )

    """
    (Optional, Default `false`) Whether the VPN connection uses static routes exclusively. Static routes
    must be used for devices that don't support BGP.
    """
    static_routes_only: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) Tags to apply to the connection. If configured with a provider [`default_tags` configurat
    ion block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurat
    ion-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
    When associated with an EC2 Transit Gateway (`transit_gateway_id` argument), the attachment ID. See
    also the [`aws_ec2_tag` resource](/docs/providers/aws/r/ec2_tag.html) for tagging the EC2 Transit Ga
    teway VPN Attachment.
    """
    transit_gateway_attachment_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the EC2 Transit Gateway.
    """
    transit_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required when outside_ip_address_type is set to `PrivateIpv4`). The attachment ID of the Transit Ga
    teway attachment to Direct Connect Gateway. The ID is obtained through a data source only.
    """
    transport_transit_gateway_attachment_id: str | core.StringOut | None = core.attr(
        str, default=None
    )

    """
    The public IP address of the first VPN tunnel.
    """
    tunnel1_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The bgp asn number of the first VPN tunnel.
    """
    tunnel1_bgp_asn: str | core.StringOut = core.attr(str, computed=True)

    """
    The bgp holdtime of the first VPN tunnel.
    """
    tunnel1_bgp_holdtime: int | core.IntOut = core.attr(int, computed=True)

    """
    The RFC 6890 link-local address of the first VPN tunnel (Customer Gateway Side).
    """
    tunnel1_cgw_inside_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Default `clear`) The action to take after DPD timeout occurs for the first VPN tunnel. Sp
    ecify restart to restart the IKE initiation. Specify clear to end the IKE session. Valid values are
    clear | none | restart`.
    """
    tunnel1_dpd_timeout_action: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Default `30`) The number of seconds after which a DPD timeout occurs for the first VPN tu
    nnel. Valid value is equal or higher than `30`.
    """
    tunnel1_dpd_timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The IKE versions that are permitted for the first VPN tunnel. Valid values are `ikev1 | i
    kev2`.
    """
    tunnel1_ike_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The CIDR block of the inside IP addresses for the first VPN tunnel. Valid value is a size
    /30 CIDR block from the 169.254.0.0/16 range.
    """
    tunnel1_inside_cidr: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The range of inside IPv6 addresses for the first VPN tunnel. Supports only EC2 Transit Ga
    teway. Valid value is a size /126 CIDR block from the local fd00::/8 range.
    """
    tunnel1_inside_ipv6_cidr: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) List of one or more Diffie-Hellman group numbers that are permitted for the first VPN tun
    nel for phase 1 IKE negotiations. Valid values are ` 2 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22
    | 23 | 24`.
    """
    tunnel1_phase1_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of one or more encryption algorithms that are permitted for the first VPN tunnel for
    phase 1 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.
    """
    tunnel1_phase1_encryption_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional) One or more integrity algorithms that are permitted for the first VPN tunnel for phase 1
    IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.
    """
    tunnel1_phase1_integrity_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional, Default `28800`) The lifetime for phase 1 of the IKE negotiation for the first VPN tunnel
    , in seconds. Valid value is between `900` and `28800`.
    """
    tunnel1_phase1_lifetime_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) List of one or more Diffie-Hellman group numbers that are permitted for the first VPN tun
    nel for phase 2 IKE negotiations. Valid values are `2 | 5 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
    22 | 23 | 24`.
    """
    tunnel1_phase2_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of one or more encryption algorithms that are permitted for the first VPN tunnel for
    phase 2 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.
    """
    tunnel1_phase2_encryption_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional) List of one or more integrity algorithms that are permitted for the first VPN tunnel for
    phase 2 IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.
    """
    tunnel1_phase2_integrity_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional, Default `3600`) The lifetime for phase 2 of the IKE negotiation for the first VPN tunnel,
    in seconds. Valid value is between `900` and `3600`.
    """
    tunnel1_phase2_lifetime_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The preshared key of the first VPN tunnel. The preshared key must be between 8 and 64 cha
    racters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, per
    iods(.) and underscores(_).
    """
    tunnel1_preshared_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Default `100`) The percentage of the rekey window for the first VPN tunnel (determined by
    tunnel1_rekey_margin_time_seconds`) during which the rekey time is randomly selected. Valid value
    is between `0` and `100`.
    """
    tunnel1_rekey_fuzz_percentage: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Default `540`) The margin time, in seconds, before the phase 2 lifetime expires, during w
    hich the AWS side of the first VPN connection performs an IKE rekey. The exact time of the rekey is
    randomly selected based on the value for `tunnel1_rekey_fuzz_percentage`. Valid value is between `60
    and half of `tunnel1_phase2_lifetime_seconds`.
    """
    tunnel1_rekey_margin_time_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Default `1024`) The number of packets in an IKE replay window for the first VPN tunnel. V
    alid value is between `64` and `2048`.
    """
    tunnel1_replay_window_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Default `add`) The action to take when the establishing the tunnel for the first VPN conn
    ection. By default, your customer gateway device must initiate the IKE negotiation and bring up the
    tunnel. Specify start for AWS to initiate the IKE negotiation. Valid values are `add | start`.
    """
    tunnel1_startup_action: str | core.StringOut | None = core.attr(str, default=None)

    """
    The RFC 6890 link-local address of the first VPN tunnel (VPN Gateway Side).
    """
    tunnel1_vgw_inside_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The public IP address of the second VPN tunnel.
    """
    tunnel2_address: str | core.StringOut = core.attr(str, computed=True)

    """
    The bgp asn number of the second VPN tunnel.
    """
    tunnel2_bgp_asn: str | core.StringOut = core.attr(str, computed=True)

    """
    The bgp holdtime of the second VPN tunnel.
    """
    tunnel2_bgp_holdtime: int | core.IntOut = core.attr(int, computed=True)

    """
    The RFC 6890 link-local address of the second VPN tunnel (Customer Gateway Side).
    """
    tunnel2_cgw_inside_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Default `clear`) The action to take after DPD timeout occurs for the second VPN tunnel. S
    pecify restart to restart the IKE initiation. Specify clear to end the IKE session. Valid values are
    clear | none | restart`.
    """
    tunnel2_dpd_timeout_action: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Default `30`) The number of seconds after which a DPD timeout occurs for the second VPN t
    unnel. Valid value is equal or higher than `30`.
    """
    tunnel2_dpd_timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The IKE versions that are permitted for the second VPN tunnel. Valid values are `ikev1 |
    ikev2`.
    """
    tunnel2_ike_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The CIDR block of the inside IP addresses for the second VPN tunnel. Valid value is a siz
    e /30 CIDR block from the 169.254.0.0/16 range.
    """
    tunnel2_inside_cidr: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The range of inside IPv6 addresses for the second VPN tunnel. Supports only EC2 Transit G
    ateway. Valid value is a size /126 CIDR block from the local fd00::/8 range.
    """
    tunnel2_inside_ipv6_cidr: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) List of one or more Diffie-Hellman group numbers that are permitted for the second VPN tu
    nnel for phase 1 IKE negotiations. Valid values are ` 2 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22
    | 23 | 24`.
    """
    tunnel2_phase1_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of one or more encryption algorithms that are permitted for the second VPN tunnel fo
    r phase 1 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.
    """
    tunnel2_phase1_encryption_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional) One or more integrity algorithms that are permitted for the second VPN tunnel for phase 1
    IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.
    """
    tunnel2_phase1_integrity_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional, Default `28800`) The lifetime for phase 1 of the IKE negotiation for the second VPN tunne
    l, in seconds. Valid value is between `900` and `28800`.
    """
    tunnel2_phase1_lifetime_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) List of one or more Diffie-Hellman group numbers that are permitted for the second VPN tu
    nnel for phase 2 IKE negotiations. Valid values are `2 | 5 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
    22 | 23 | 24`.
    """
    tunnel2_phase2_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of one or more encryption algorithms that are permitted for the second VPN tunnel fo
    r phase 2 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.
    """
    tunnel2_phase2_encryption_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional) List of one or more integrity algorithms that are permitted for the second VPN tunnel for
    phase 2 IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.
    """
    tunnel2_phase2_integrity_algorithms: list[str] | core.ArrayOut[
        core.StringOut
    ] | None = core.attr(str, default=None, kind=core.Kind.array)

    """
    (Optional, Default `3600`) The lifetime for phase 2 of the IKE negotiation for the second VPN tunnel
    , in seconds. Valid value is between `900` and `3600`.
    """
    tunnel2_phase2_lifetime_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The preshared key of the second VPN tunnel. The preshared key must be between 8 and 64 ch
    aracters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, pe
    riods(.) and underscores(_).
    """
    tunnel2_preshared_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Default `100`) The percentage of the rekey window for the second VPN tunnel (determined b
    y `tunnel2_rekey_margin_time_seconds`) during which the rekey time is randomly selected. Valid value
    is between `0` and `100`.
    """
    tunnel2_rekey_fuzz_percentage: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Default `540`) The margin time, in seconds, before the phase 2 lifetime expires, during w
    hich the AWS side of the second VPN connection performs an IKE rekey. The exact time of the rekey is
    randomly selected based on the value for `tunnel2_rekey_fuzz_percentage`. Valid value is between `6
    0` and half of `tunnel2_phase2_lifetime_seconds`.
    """
    tunnel2_rekey_margin_time_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Default `1024`) The number of packets in an IKE replay window for the second VPN tunnel.
    Valid value is between `64` and `2048`.
    """
    tunnel2_replay_window_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Default `add`) The action to take when the establishing the tunnel for the second VPN con
    nection. By default, your customer gateway device must initiate the IKE negotiation and bring up the
    tunnel. Specify start for AWS to initiate the IKE negotiation. Valid values are `add | start`.
    """
    tunnel2_startup_action: str | core.StringOut | None = core.attr(str, default=None)

    """
    The RFC 6890 link-local address of the second VPN tunnel (VPN Gateway Side).
    """
    tunnel2_vgw_inside_address: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Default `ipv4`) Indicate whether the VPN tunnels process IPv4 or IPv6 traffic. Valid valu
    es are `ipv4 | ipv6`. `ipv6` Supports only EC2 Transit Gateway.
    """
    tunnel_inside_ip_version: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) The type of VPN connection. The only type AWS supports at this time is "ipsec.1".
    """
    type: str | core.StringOut = core.attr(str)

    """
    Telemetry for the VPN tunnels. Detailed below.
    """
    vgw_telemetry: list[VgwTelemetry] | core.ArrayOut[VgwTelemetry] = core.attr(
        VgwTelemetry, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The ID of the Virtual Private Gateway.
    """
    vpn_gateway_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        customer_gateway_id: str | core.StringOut,
        type: str | core.StringOut,
        enable_acceleration: bool | core.BoolOut | None = None,
        local_ipv4_network_cidr: str | core.StringOut | None = None,
        local_ipv6_network_cidr: str | core.StringOut | None = None,
        outside_ip_address_type: str | core.StringOut | None = None,
        remote_ipv4_network_cidr: str | core.StringOut | None = None,
        remote_ipv6_network_cidr: str | core.StringOut | None = None,
        static_routes_only: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transit_gateway_id: str | core.StringOut | None = None,
        transport_transit_gateway_attachment_id: str | core.StringOut | None = None,
        tunnel1_dpd_timeout_action: str | core.StringOut | None = None,
        tunnel1_dpd_timeout_seconds: int | core.IntOut | None = None,
        tunnel1_ike_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tunnel1_inside_cidr: str | core.StringOut | None = None,
        tunnel1_inside_ipv6_cidr: str | core.StringOut | None = None,
        tunnel1_phase1_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = None,
        tunnel1_phase1_encryption_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel1_phase1_integrity_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel1_phase1_lifetime_seconds: int | core.IntOut | None = None,
        tunnel1_phase2_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = None,
        tunnel1_phase2_encryption_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel1_phase2_integrity_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel1_phase2_lifetime_seconds: int | core.IntOut | None = None,
        tunnel1_preshared_key: str | core.StringOut | None = None,
        tunnel1_rekey_fuzz_percentage: int | core.IntOut | None = None,
        tunnel1_rekey_margin_time_seconds: int | core.IntOut | None = None,
        tunnel1_replay_window_size: int | core.IntOut | None = None,
        tunnel1_startup_action: str | core.StringOut | None = None,
        tunnel2_dpd_timeout_action: str | core.StringOut | None = None,
        tunnel2_dpd_timeout_seconds: int | core.IntOut | None = None,
        tunnel2_ike_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tunnel2_inside_cidr: str | core.StringOut | None = None,
        tunnel2_inside_ipv6_cidr: str | core.StringOut | None = None,
        tunnel2_phase1_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = None,
        tunnel2_phase1_encryption_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel2_phase1_integrity_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel2_phase1_lifetime_seconds: int | core.IntOut | None = None,
        tunnel2_phase2_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = None,
        tunnel2_phase2_encryption_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel2_phase2_integrity_algorithms: list[str]
        | core.ArrayOut[core.StringOut]
        | None = None,
        tunnel2_phase2_lifetime_seconds: int | core.IntOut | None = None,
        tunnel2_preshared_key: str | core.StringOut | None = None,
        tunnel2_rekey_fuzz_percentage: int | core.IntOut | None = None,
        tunnel2_rekey_margin_time_seconds: int | core.IntOut | None = None,
        tunnel2_replay_window_size: int | core.IntOut | None = None,
        tunnel2_startup_action: str | core.StringOut | None = None,
        tunnel_inside_ip_version: str | core.StringOut | None = None,
        vpn_gateway_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                customer_gateway_id=customer_gateway_id,
                type=type,
                enable_acceleration=enable_acceleration,
                local_ipv4_network_cidr=local_ipv4_network_cidr,
                local_ipv6_network_cidr=local_ipv6_network_cidr,
                outside_ip_address_type=outside_ip_address_type,
                remote_ipv4_network_cidr=remote_ipv4_network_cidr,
                remote_ipv6_network_cidr=remote_ipv6_network_cidr,
                static_routes_only=static_routes_only,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_id=transit_gateway_id,
                transport_transit_gateway_attachment_id=transport_transit_gateway_attachment_id,
                tunnel1_dpd_timeout_action=tunnel1_dpd_timeout_action,
                tunnel1_dpd_timeout_seconds=tunnel1_dpd_timeout_seconds,
                tunnel1_ike_versions=tunnel1_ike_versions,
                tunnel1_inside_cidr=tunnel1_inside_cidr,
                tunnel1_inside_ipv6_cidr=tunnel1_inside_ipv6_cidr,
                tunnel1_phase1_dh_group_numbers=tunnel1_phase1_dh_group_numbers,
                tunnel1_phase1_encryption_algorithms=tunnel1_phase1_encryption_algorithms,
                tunnel1_phase1_integrity_algorithms=tunnel1_phase1_integrity_algorithms,
                tunnel1_phase1_lifetime_seconds=tunnel1_phase1_lifetime_seconds,
                tunnel1_phase2_dh_group_numbers=tunnel1_phase2_dh_group_numbers,
                tunnel1_phase2_encryption_algorithms=tunnel1_phase2_encryption_algorithms,
                tunnel1_phase2_integrity_algorithms=tunnel1_phase2_integrity_algorithms,
                tunnel1_phase2_lifetime_seconds=tunnel1_phase2_lifetime_seconds,
                tunnel1_preshared_key=tunnel1_preshared_key,
                tunnel1_rekey_fuzz_percentage=tunnel1_rekey_fuzz_percentage,
                tunnel1_rekey_margin_time_seconds=tunnel1_rekey_margin_time_seconds,
                tunnel1_replay_window_size=tunnel1_replay_window_size,
                tunnel1_startup_action=tunnel1_startup_action,
                tunnel2_dpd_timeout_action=tunnel2_dpd_timeout_action,
                tunnel2_dpd_timeout_seconds=tunnel2_dpd_timeout_seconds,
                tunnel2_ike_versions=tunnel2_ike_versions,
                tunnel2_inside_cidr=tunnel2_inside_cidr,
                tunnel2_inside_ipv6_cidr=tunnel2_inside_ipv6_cidr,
                tunnel2_phase1_dh_group_numbers=tunnel2_phase1_dh_group_numbers,
                tunnel2_phase1_encryption_algorithms=tunnel2_phase1_encryption_algorithms,
                tunnel2_phase1_integrity_algorithms=tunnel2_phase1_integrity_algorithms,
                tunnel2_phase1_lifetime_seconds=tunnel2_phase1_lifetime_seconds,
                tunnel2_phase2_dh_group_numbers=tunnel2_phase2_dh_group_numbers,
                tunnel2_phase2_encryption_algorithms=tunnel2_phase2_encryption_algorithms,
                tunnel2_phase2_integrity_algorithms=tunnel2_phase2_integrity_algorithms,
                tunnel2_phase2_lifetime_seconds=tunnel2_phase2_lifetime_seconds,
                tunnel2_preshared_key=tunnel2_preshared_key,
                tunnel2_rekey_fuzz_percentage=tunnel2_rekey_fuzz_percentage,
                tunnel2_rekey_margin_time_seconds=tunnel2_rekey_margin_time_seconds,
                tunnel2_replay_window_size=tunnel2_replay_window_size,
                tunnel2_startup_action=tunnel2_startup_action,
                tunnel_inside_ip_version=tunnel_inside_ip_version,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        customer_gateway_id: str | core.StringOut = core.arg()

        enable_acceleration: bool | core.BoolOut | None = core.arg(default=None)

        local_ipv4_network_cidr: str | core.StringOut | None = core.arg(default=None)

        local_ipv6_network_cidr: str | core.StringOut | None = core.arg(default=None)

        outside_ip_address_type: str | core.StringOut | None = core.arg(default=None)

        remote_ipv4_network_cidr: str | core.StringOut | None = core.arg(default=None)

        remote_ipv6_network_cidr: str | core.StringOut | None = core.arg(default=None)

        static_routes_only: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transit_gateway_id: str | core.StringOut | None = core.arg(default=None)

        transport_transit_gateway_attachment_id: str | core.StringOut | None = core.arg(
            default=None
        )

        tunnel1_dpd_timeout_action: str | core.StringOut | None = core.arg(default=None)

        tunnel1_dpd_timeout_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel1_ike_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tunnel1_inside_cidr: str | core.StringOut | None = core.arg(default=None)

        tunnel1_inside_ipv6_cidr: str | core.StringOut | None = core.arg(default=None)

        tunnel1_phase1_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(
            default=None
        )

        tunnel1_phase1_encryption_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel1_phase1_integrity_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel1_phase1_lifetime_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel1_phase2_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(
            default=None
        )

        tunnel1_phase2_encryption_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel1_phase2_integrity_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel1_phase2_lifetime_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel1_preshared_key: str | core.StringOut | None = core.arg(default=None)

        tunnel1_rekey_fuzz_percentage: int | core.IntOut | None = core.arg(default=None)

        tunnel1_rekey_margin_time_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel1_replay_window_size: int | core.IntOut | None = core.arg(default=None)

        tunnel1_startup_action: str | core.StringOut | None = core.arg(default=None)

        tunnel2_dpd_timeout_action: str | core.StringOut | None = core.arg(default=None)

        tunnel2_dpd_timeout_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel2_ike_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tunnel2_inside_cidr: str | core.StringOut | None = core.arg(default=None)

        tunnel2_inside_ipv6_cidr: str | core.StringOut | None = core.arg(default=None)

        tunnel2_phase1_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(
            default=None
        )

        tunnel2_phase1_encryption_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel2_phase1_integrity_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel2_phase1_lifetime_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel2_phase2_dh_group_numbers: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(
            default=None
        )

        tunnel2_phase2_encryption_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel2_phase2_integrity_algorithms: list[str] | core.ArrayOut[
            core.StringOut
        ] | None = core.arg(default=None)

        tunnel2_phase2_lifetime_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel2_preshared_key: str | core.StringOut | None = core.arg(default=None)

        tunnel2_rekey_fuzz_percentage: int | core.IntOut | None = core.arg(default=None)

        tunnel2_rekey_margin_time_seconds: int | core.IntOut | None = core.arg(default=None)

        tunnel2_replay_window_size: int | core.IntOut | None = core.arg(default=None)

        tunnel2_startup_action: str | core.StringOut | None = core.arg(default=None)

        tunnel_inside_ip_version: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        vpn_gateway_id: str | core.StringOut | None = core.arg(default=None)
