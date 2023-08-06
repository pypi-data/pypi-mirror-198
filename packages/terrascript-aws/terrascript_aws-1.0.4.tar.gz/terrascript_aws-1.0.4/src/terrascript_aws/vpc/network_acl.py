import terrascript.core as core


@core.schema
class Egress(core.Schema):

    action: str | core.StringOut = core.attr(str)

    cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    from_port: int | core.IntOut = core.attr(int)

    icmp_code: int | core.IntOut | None = core.attr(int, default=None)

    icmp_type: int | core.IntOut | None = core.attr(int, default=None)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    protocol: str | core.StringOut = core.attr(str)

    rule_no: int | core.IntOut = core.attr(int)

    to_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        action: str | core.StringOut,
        from_port: int | core.IntOut,
        protocol: str | core.StringOut,
        rule_no: int | core.IntOut,
        to_port: int | core.IntOut,
        cidr_block: str | core.StringOut | None = None,
        icmp_code: int | core.IntOut | None = None,
        icmp_type: int | core.IntOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Egress.Args(
                action=action,
                from_port=from_port,
                protocol=protocol,
                rule_no=rule_no,
                to_port=to_port,
                cidr_block=cidr_block,
                icmp_code=icmp_code,
                icmp_type=icmp_type,
                ipv6_cidr_block=ipv6_cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        from_port: int | core.IntOut = core.arg()

        icmp_code: int | core.IntOut | None = core.arg(default=None)

        icmp_type: int | core.IntOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        rule_no: int | core.IntOut = core.arg()

        to_port: int | core.IntOut = core.arg()


@core.schema
class Ingress(core.Schema):

    action: str | core.StringOut = core.attr(str)

    cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    from_port: int | core.IntOut = core.attr(int)

    icmp_code: int | core.IntOut | None = core.attr(int, default=None)

    icmp_type: int | core.IntOut | None = core.attr(int, default=None)

    ipv6_cidr_block: str | core.StringOut | None = core.attr(str, default=None)

    protocol: str | core.StringOut = core.attr(str)

    rule_no: int | core.IntOut = core.attr(int)

    to_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        action: str | core.StringOut,
        from_port: int | core.IntOut,
        protocol: str | core.StringOut,
        rule_no: int | core.IntOut,
        to_port: int | core.IntOut,
        cidr_block: str | core.StringOut | None = None,
        icmp_code: int | core.IntOut | None = None,
        icmp_type: int | core.IntOut | None = None,
        ipv6_cidr_block: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Ingress.Args(
                action=action,
                from_port=from_port,
                protocol=protocol,
                rule_no=rule_no,
                to_port=to_port,
                cidr_block=cidr_block,
                icmp_code=icmp_code,
                icmp_type=icmp_type,
                ipv6_cidr_block=ipv6_cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()

        cidr_block: str | core.StringOut | None = core.arg(default=None)

        from_port: int | core.IntOut = core.arg()

        icmp_code: int | core.IntOut | None = core.arg(default=None)

        icmp_type: int | core.IntOut | None = core.arg(default=None)

        ipv6_cidr_block: str | core.StringOut | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        rule_no: int | core.IntOut = core.arg()

        to_port: int | core.IntOut = core.arg()


@core.resource(type="aws_network_acl", namespace="vpc")
class NetworkAcl(core.Resource):
    """
    The ARN of the network ACL
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies an egress rule. Parameters defined below.
    """
    egress: list[Egress] | core.ArrayOut[Egress] | None = core.attr(
        Egress, default=None, computed=True, kind=core.Kind.array
    )

    """
    The ID of the network ACL
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies an ingress rule. Parameters defined below.
    """
    ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.attr(
        Ingress, default=None, computed=True, kind=core.Kind.array
    )

    """
    The ID of the AWS account that owns the network ACL.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of Subnet IDs to apply the ACL to
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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

    """
    (Required) The ID of the associated VPC.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: str | core.StringOut,
        egress: list[Egress] | core.ArrayOut[Egress] | None = None,
        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkAcl.Args(
                vpc_id=vpc_id,
                egress=egress,
                ingress=ingress,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        egress: list[Egress] | core.ArrayOut[Egress] | None = core.arg(default=None)

        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
