import terrascript.core as core


@core.schema
class DestinationPortRange(core.Schema):

    from_port: int | core.IntOut | None = core.attr(int, default=None)

    to_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut | None = None,
        to_port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=DestinationPortRange.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: int | core.IntOut | None = core.arg(default=None)

        to_port: int | core.IntOut | None = core.arg(default=None)


@core.schema
class SourcePortRange(core.Schema):

    from_port: int | core.IntOut | None = core.attr(int, default=None)

    to_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut | None = None,
        to_port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=SourcePortRange.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: int | core.IntOut | None = core.arg(default=None)

        to_port: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_ec2_traffic_mirror_filter_rule", namespace="aws_vpc")
class Ec2TrafficMirrorFilterRule(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    destination_cidr_block: str | core.StringOut = core.attr(str)

    destination_port_range: DestinationPortRange | None = core.attr(
        DestinationPortRange, default=None
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    protocol: int | core.IntOut | None = core.attr(int, default=None)

    rule_action: str | core.StringOut = core.attr(str)

    rule_number: int | core.IntOut = core.attr(int)

    source_cidr_block: str | core.StringOut = core.attr(str)

    source_port_range: SourcePortRange | None = core.attr(SourcePortRange, default=None)

    traffic_direction: str | core.StringOut = core.attr(str)

    traffic_mirror_filter_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: str | core.StringOut,
        rule_action: str | core.StringOut,
        rule_number: int | core.IntOut,
        source_cidr_block: str | core.StringOut,
        traffic_direction: str | core.StringOut,
        traffic_mirror_filter_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        destination_port_range: DestinationPortRange | None = None,
        protocol: int | core.IntOut | None = None,
        source_port_range: SourcePortRange | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TrafficMirrorFilterRule.Args(
                destination_cidr_block=destination_cidr_block,
                rule_action=rule_action,
                rule_number=rule_number,
                source_cidr_block=source_cidr_block,
                traffic_direction=traffic_direction,
                traffic_mirror_filter_id=traffic_mirror_filter_id,
                description=description,
                destination_port_range=destination_port_range,
                protocol=protocol,
                source_port_range=source_port_range,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        destination_cidr_block: str | core.StringOut = core.arg()

        destination_port_range: DestinationPortRange | None = core.arg(default=None)

        protocol: int | core.IntOut | None = core.arg(default=None)

        rule_action: str | core.StringOut = core.arg()

        rule_number: int | core.IntOut = core.arg()

        source_cidr_block: str | core.StringOut = core.arg()

        source_port_range: SourcePortRange | None = core.arg(default=None)

        traffic_direction: str | core.StringOut = core.arg()

        traffic_mirror_filter_id: str | core.StringOut = core.arg()
