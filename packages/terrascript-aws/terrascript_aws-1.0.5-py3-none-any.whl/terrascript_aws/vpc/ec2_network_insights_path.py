import terrascript.core as core


@core.resource(type="aws_ec2_network_insights_path", namespace="vpc")
class Ec2NetworkInsightsPath(core.Resource):
    """
    ARN of the Network Insights Path.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ID of the resource which is the source of the path. Can be an Instance, Internet Gateway,
    Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
    """
    destination: str | core.StringOut = core.attr(str)

    """
    (Optional) IP address of the destination resource.
    """
    destination_ip: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Destination port to analyze access to.
    """
    destination_port: int | core.IntOut | None = core.attr(int, default=None)

    """
    ID of the Network Insights Path.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Protocol to use for analysis. Valid options are `tcp` or `udp`.
    """
    protocol: str | core.StringOut = core.attr(str)

    """
    (Required) ID of the resource which is the source of the path. Can be an Instance, Internet Gateway,
    Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
    """
    source: str | core.StringOut = core.attr(str)

    """
    (Optional) IP address of the source resource.
    """
    source_ip: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        destination: str | core.StringOut,
        protocol: str | core.StringOut,
        source: str | core.StringOut,
        destination_ip: str | core.StringOut | None = None,
        destination_port: int | core.IntOut | None = None,
        source_ip: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2NetworkInsightsPath.Args(
                destination=destination,
                protocol=protocol,
                source=source,
                destination_ip=destination_ip,
                destination_port=destination_port,
                source_ip=source_ip,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: str | core.StringOut = core.arg()

        destination_ip: str | core.StringOut | None = core.arg(default=None)

        destination_port: int | core.IntOut | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        source: str | core.StringOut = core.arg()

        source_ip: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
