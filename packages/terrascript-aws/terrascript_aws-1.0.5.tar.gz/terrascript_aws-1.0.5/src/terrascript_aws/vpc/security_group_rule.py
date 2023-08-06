import terrascript.core as core


@core.resource(type="aws_security_group_rule", namespace="vpc")
class SecurityGroupRule(core.Resource):
    """
    (Optional) List of CIDR blocks. Cannot be specified with `source_security_group_id` or `self`.
    """

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Description of the rule.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Start port (or ICMP type number if protocol is "icmp" or "icmpv6").
    """
    from_port: int | core.IntOut = core.attr(int)

    """
    ID of the security group rule.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of IPv6 CIDR blocks. Cannot be specified with `source_security_group_id` or `self`.
    """
    ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) List of Prefix List IDs.
    """
    prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) Protocol. If not icmp, icmpv6, tcp, udp, or all use the [protocol number](https://www.ian
    a.org/assignments/protocol-numbers/protocol-numbers.xhtml)
    """
    protocol: str | core.StringOut = core.attr(str)

    """
    (Required) Security group to apply this rule to.
    """
    security_group_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether the security group itself will be added as a source to this ingress rule. Cannot
    be specified with `cidr_blocks`, `ipv6_cidr_blocks`, or `source_security_group_id`.
    """
    self_: bool | core.BoolOut | None = core.attr(bool, default=None, alias="self")

    """
    (Optional) Security group id to allow access to/from, depending on the `type`. Cannot be specified w
    ith `cidr_blocks`, `ipv6_cidr_blocks`, or `self`.
    """
    source_security_group_id: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) End port (or ICMP code if protocol is "icmp").
    """
    to_port: int | core.IntOut = core.attr(int)

    """
    (Required) Type of rule being created. Valid options are `ingress` (inbound)
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        from_port: int | core.IntOut,
        protocol: str | core.StringOut,
        security_group_id: str | core.StringOut,
        to_port: int | core.IntOut,
        type: str | core.StringOut,
        cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_: bool | core.BoolOut | None = None,
        source_security_group_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecurityGroupRule.Args(
                from_port=from_port,
                protocol=protocol,
                security_group_id=security_group_id,
                to_port=to_port,
                type=type,
                cidr_blocks=cidr_blocks,
                description=description,
                ipv6_cidr_blocks=ipv6_cidr_blocks,
                prefix_list_ids=prefix_list_ids,
                self_=self_,
                source_security_group_id=source_security_group_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        from_port: int | core.IntOut = core.arg()

        ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        security_group_id: str | core.StringOut = core.arg()

        self_: bool | core.BoolOut | None = core.arg(default=None)

        source_security_group_id: str | core.StringOut | None = core.arg(default=None)

        to_port: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()
