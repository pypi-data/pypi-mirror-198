import terrascript.core as core


@core.resource(type="aws_dx_connection", namespace="direct_connect")
class DxConnection(core.Resource):
    """
    The ARN of the connection.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The Direct Connect endpoint on which the physical connection terminates.
    """
    aws_device: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The bandwidth of the connection. Valid values for dedicated connections: 1Gbps, 10Gbps. V
    alid values for hosted connections: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbp
    s, 5Gbps, 10Gbps and 100Gbps. Case sensitive.
    """
    bandwidth: str | core.StringOut = core.attr(str)

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
    (Required) The AWS Direct Connect location where the connection is located. See [DescribeLocations](
    https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the li
    st of AWS Direct Connect locations. Use `locationCode`.
    """
    location: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the connection.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The ID of the AWS account that owns the connection.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the service provider associated with the connection.
    """
    provider_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: str | core.StringOut,
        location: str | core.StringOut,
        name: str | core.StringOut,
        provider_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxConnection.Args(
                bandwidth=bandwidth,
                location=location,
                name=name,
                provider_name=provider_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: str | core.StringOut = core.arg()

        location: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
