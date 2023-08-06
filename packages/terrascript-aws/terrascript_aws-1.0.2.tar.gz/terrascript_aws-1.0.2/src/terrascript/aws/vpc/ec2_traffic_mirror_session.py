import terrascript.core as core


@core.resource(type="aws_ec2_traffic_mirror_session", namespace="aws_vpc")
class Ec2TrafficMirrorSession(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    network_interface_id: str | core.StringOut = core.attr(str)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    packet_length: int | core.IntOut | None = core.attr(int, default=None)

    session_number: int | core.IntOut = core.attr(int)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    traffic_mirror_filter_id: str | core.StringOut = core.attr(str)

    traffic_mirror_target_id: str | core.StringOut = core.attr(str)

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
