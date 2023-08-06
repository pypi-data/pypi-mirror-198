import terrascript.core as core


@core.resource(type="aws_dx_lag", namespace="direct_connect")
class DxLag(core.Resource):
    """
    The ARN of the LAG.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of an existing dedicated connection to migrate to the LAG.
    """
    connection_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The bandwidth of the individual physical connections bundled by the LAG. Valid values: 50
    Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, 10Gbps and 100Gbps. Case sen
    sitive.
    """
    connections_bandwidth: str | core.StringOut = core.attr(str)

    """
    (Optional, Default:false) A boolean that indicates all connections associated with the LAG should be
    deleted so that the LAG can be destroyed without error. These objects are *not* recoverable.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).
    """
    has_logical_redundancy: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the LAG.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    jumbo_frame_capable: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Required) The AWS Direct Connect location in which the LAG should be allocated. See [DescribeLocati
    ons](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for t
    he list of AWS Direct Connect locations. Use `locationCode`.
    """
    location: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the LAG.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The ID of the AWS account that owns the LAG.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the service provider associated with the LAG.
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
        connections_bandwidth: str | core.StringOut,
        location: str | core.StringOut,
        name: str | core.StringOut,
        connection_id: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        provider_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxLag.Args(
                connections_bandwidth=connections_bandwidth,
                location=location,
                name=name,
                connection_id=connection_id,
                force_destroy=force_destroy,
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
        connection_id: str | core.StringOut | None = core.arg(default=None)

        connections_bandwidth: str | core.StringOut = core.arg()

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        location: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        provider_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
