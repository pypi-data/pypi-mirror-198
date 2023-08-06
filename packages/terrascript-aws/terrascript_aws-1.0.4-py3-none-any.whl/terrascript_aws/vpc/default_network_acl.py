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


@core.resource(type="aws_default_network_acl", namespace="vpc")
class DefaultNetworkAcl(core.Resource):
    """
    ARN of the Default Network ACL
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Network ACL ID to manage. This attribute is exported from `aws_vpc`, or manually found vi
    a the AWS Console.
    """
    default_network_acl_id: str | core.StringOut = core.attr(str)

    """
    (Optional) Configuration block for an egress rule. Detailed below.
    """
    egress: list[Egress] | core.ArrayOut[Egress] | None = core.attr(
        Egress, default=None, kind=core.Kind.array
    )

    """
    ID of the Default Network ACL
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for an ingress rule. Detailed below.
    """
    ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.attr(
        Ingress, default=None, kind=core.Kind.array
    )

    """
    ID of the AWS account that owns the Default Network ACL
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of Subnet IDs to apply the ACL to. See the notes below on managing Subnets in the De
    fault Network ACL
    """
    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    ID of the associated VPC
    """
    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        default_network_acl_id: str | core.StringOut,
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
            args=DefaultNetworkAcl.Args(
                default_network_acl_id=default_network_acl_id,
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
        default_network_acl_id: str | core.StringOut = core.arg()

        egress: list[Egress] | core.ArrayOut[Egress] | None = core.arg(default=None)

        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
