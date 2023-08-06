import terrascript.core as core


@core.resource(type="aws_ec2_traffic_mirror_session", namespace="vpc")
class Ec2TrafficMirrorSession(core.Resource):
    """
    The ARN of the traffic mirror session.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the traffic mirror session.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the session.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new) ID of the source network interface. Not all network interfaces are eligible a
    s mirror sources. On EC2 instances only nitro based instances support mirroring.
    """
    network_interface_id: str | core.StringOut = core.attr(str)

    """
    The AWS account ID of the session owner.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of bytes in each packet to mirror. These are bytes after the VXLAN header. Do
    not specify this parameter when you want to mirror the entire packet. To mirror a subset of the pack
    et, set this to the length (in bytes) that you want to mirror.
    """
    packet_length: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) - The session number determines the order in which sessions are evaluated when an interfa
    ce is used by multiple sessions. The first session with a matching filter is the one that mirrors th
    e packets.
    """
    session_number: int | core.IntOut = core.attr(int)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    traffic_mirror_filter_id: str | core.StringOut = core.attr(str)

    """
    (Required) ID of the traffic mirror target to be used
    """
    traffic_mirror_target_id: str | core.StringOut = core.attr(str)

    """
    (Optional) - The VXLAN ID for the Traffic Mirror session. For more information about the VXLAN proto
    col, see RFC 7348. If you do not specify a VirtualNetworkId, an account-wide unique id is chosen at
    random.
    """
    virtual_network_id: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        network_interface_id: str | core.StringOut,
        session_number: int | core.IntOut,
        traffic_mirror_filter_id: str | core.StringOut,
        traffic_mirror_target_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        packet_length: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        virtual_network_id: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TrafficMirrorSession.Args(
                network_interface_id=network_interface_id,
                session_number=session_number,
                traffic_mirror_filter_id=traffic_mirror_filter_id,
                traffic_mirror_target_id=traffic_mirror_target_id,
                description=description,
                packet_length=packet_length,
                tags=tags,
                tags_all=tags_all,
                virtual_network_id=virtual_network_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        network_interface_id: str | core.StringOut = core.arg()

        packet_length: int | core.IntOut | None = core.arg(default=None)

        session_number: int | core.IntOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        traffic_mirror_filter_id: str | core.StringOut = core.arg()

        traffic_mirror_target_id: str | core.StringOut = core.arg()

        virtual_network_id: int | core.IntOut | None = core.arg(default=None)
