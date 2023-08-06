import terrascript.core as core


@core.schema
class Ingress(core.Schema):

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    from_port: int | core.IntOut = core.attr(int)

    ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    protocol: str | core.StringOut = core.attr(str)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_: bool | core.BoolOut | None = core.attr(bool, default=None, alias="self")

    to_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut,
        protocol: str | core.StringOut,
        to_port: int | core.IntOut,
        cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Ingress.Args(
                from_port=from_port,
                protocol=protocol,
                to_port=to_port,
                cidr_blocks=cidr_blocks,
                description=description,
                ipv6_cidr_blocks=ipv6_cidr_blocks,
                prefix_list_ids=prefix_list_ids,
                security_groups=security_groups,
                self_=self_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        from_port: int | core.IntOut = core.arg()

        ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        self_: bool | core.BoolOut | None = core.arg(default=None)

        to_port: int | core.IntOut = core.arg()


@core.schema
class Egress(core.Schema):

    cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    from_port: int | core.IntOut = core.attr(int)

    ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    protocol: str | core.StringOut = core.attr(str)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_: bool | core.BoolOut | None = core.attr(bool, default=None, alias="self")

    to_port: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        from_port: int | core.IntOut,
        protocol: str | core.StringOut,
        to_port: int | core.IntOut,
        cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        self_: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Egress.Args(
                from_port=from_port,
                protocol=protocol,
                to_port=to_port,
                cidr_blocks=cidr_blocks,
                description=description,
                ipv6_cidr_blocks=ipv6_cidr_blocks,
                prefix_list_ids=prefix_list_ids,
                security_groups=security_groups,
                self_=self_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        from_port: int | core.IntOut = core.arg()

        ipv6_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        prefix_list_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        self_: bool | core.BoolOut | None = core.arg(default=None)

        to_port: int | core.IntOut = core.arg()


@core.resource(type="aws_default_security_group", namespace="vpc")
class DefaultSecurityGroup(core.Resource):
    """
    ARN of the security group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of this rule.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, VPC only) Configuration block. Detailed below.
    """
    egress: list[Egress] | core.ArrayOut[Egress] | None = core.attr(
        Egress, default=None, computed=True, kind=core.Kind.array
    )

    """
    ID of the security group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block. Detailed below.
    """
    ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.attr(
        Ingress, default=None, computed=True, kind=core.Kind.array
    )

    """
    Name of the security group.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    name_prefix: str | core.StringOut = core.attr(str, computed=True)

    """
    Owner ID.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    revoke_rules_on_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

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
    (Optional, Forces new resource) VPC ID. **Note that changing the `vpc_id` will _not_ restore any def
    ault security group rules that were modified, added, or removed.** It will be left in its current st
    ate.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        egress: list[Egress] | core.ArrayOut[Egress] | None = None,
        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = None,
        revoke_rules_on_delete: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultSecurityGroup.Args(
                egress=egress,
                ingress=ingress,
                revoke_rules_on_delete=revoke_rules_on_delete,
                tags=tags,
                tags_all=tags_all,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        egress: list[Egress] | core.ArrayOut[Egress] | None = core.arg(default=None)

        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.arg(default=None)

        revoke_rules_on_delete: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
