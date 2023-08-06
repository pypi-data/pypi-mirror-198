import terrascript.core as core


@core.resource(type="aws_dx_hosted_connection", namespace="direct_connect")
class DxHostedConnection(core.Resource):
    """
    The Direct Connect endpoint on which the physical connection terminates.
    """

    aws_device: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The bandwidth of the connection. Valid values for dedicated connections: 1Gbps, 10Gbps. V
    alid values for hosted connections: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbp
    s, 5Gbps and 10Gbps. Case sensitive.
    """
    bandwidth: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the interconnect or LAG.
    """
    connection_id: str | core.StringOut = core.attr(str)

    """
    Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6
    ).
    """
    has_logical_redundancy: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the connection.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Boolean value representing if jumbo frames have been enabled for this connection.
    """
    jumbo_frame_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The ID of the LAG.
    """
    lag_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The time of the most recent call to [DescribeLoa](https://docs.aws.amazon.com/directconnect/latest/A
    PIReference/API_DescribeLoa.html) for this connection.
    """
    loa_issue_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The location of the connection.
    """
    location: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the connection.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the AWS account of the customer for the connection.
    """
    owner_account_id: str | core.StringOut = core.attr(str)

    """
    The name of the AWS Direct Connect service provider associated with the connection.
    """
    partner_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the service provider associated with the connection.
    """
    provider_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS Region where the connection is located.
    """
    region: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the connection. Possible values include: ordering, requested, pending, available, down,
    deleting, deleted, rejected, unknown. See [AllocateHostedConnection](https://docs.aws.amazon.com/di
    rectconnect/latest/APIReference/API_AllocateHostedConnection.html) for a description of each connect
    ion state.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The dedicated VLAN provisioned to the hosted connection.
    """
    vlan: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: str | core.StringOut,
        connection_id: str | core.StringOut,
        name: str | core.StringOut,
        owner_account_id: str | core.StringOut,
        vlan: int | core.IntOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedConnection.Args(
                bandwidth=bandwidth,
                connection_id=connection_id,
                name=name,
                owner_account_id=owner_account_id,
                vlan=vlan,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: str | core.StringOut = core.arg()

        connection_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        owner_account_id: str | core.StringOut = core.arg()

        vlan: int | core.IntOut = core.arg()
