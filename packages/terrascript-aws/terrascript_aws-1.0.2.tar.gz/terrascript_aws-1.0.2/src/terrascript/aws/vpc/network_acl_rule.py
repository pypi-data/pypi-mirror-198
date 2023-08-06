import terrascript.core as core


@core.resource(type="aws_network_acl_rule", namespace="aws_vpc")
class NetworkAclRule(core.Resource):

    cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    egress: bool | core.BoolOut | None = core.attr(bool, default=None)

    from_port: int | core.IntOut | None = core.attr(int, default=None)

    icmp_code: int | core.IntOut | None = core.attr(int, default=None)

    icmp_type: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    network_acl_id: str | core.StringOut = core.attr(str)

    protocol: str | core.StringOut = core.attr(str)

    rule_action: str | core.StringOut = core.attr(str)

    rule_number: int | core.IntOut = core.attr(int)

    to_port: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        network_acl_id: str | core.StringOut,
        protocol: str | core.StringOut,
        rule_action: str | core.StringOut,
        rule_number: int | core.IntOut,
        cidr_block: str | core.StringOut | None = None,
        egress: bool | core.BoolOut | None = None,
        from_port: int | core.IntOut | None = None,
        icmp_code: int | core.IntOut | None = None,
        icmp_type: int | core.IntOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
        to_port: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkAclRule.Args(
                network_acl_id=network_acl_id,
                protocol=protocol,
                rule_action=rule_action,
                rule_number=rule_number,
                cidr_block=cidr_block,
                egress=egress,
                from_port=from_port,
                icmp_code=icmp_code,
                icmp_type=icmp_type,
                ipv6_cidr_block=ipv6_cidr_block,
                to_port=to_port,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr_block: str | core.StringOut | None = core.arg(default=None)

        egress: bool | core.BoolOut | None = core.arg(default=None)

        from_port: int | core.IntOut | None = core.arg(default=None)

        icmp_code: int | core.IntOut | None = core.arg(default=None)

        icmp_type: int | core.IntOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        network_acl_id: str | core.StringOut = core.arg()

        protocol: str | core.StringOut = core.arg()

        rule_action: str | core.StringOut = core.arg()

        rule_number: int | core.IntOut = core.arg()

        to_port: int | core.IntOut | None = core.arg(default=None)
