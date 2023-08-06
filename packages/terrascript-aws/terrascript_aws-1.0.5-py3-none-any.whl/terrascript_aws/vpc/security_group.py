import terrascript.core as core


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


@core.resource(type="aws_security_group", namespace="vpc")
class SecurityGroup(core.Resource):
    """
    ARN of the security group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) Security group description. Defaults to `Managed by Terraform`. Cann
    ot be `""`. __NOTE__: This field maps to the AWS `GroupDescription` attribute, for which there is no
    Update API. If you'd like to classify your security groups in a way that can be updated, use `tags`
    .
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, VPC only) Configuration block for egress rules. Can be specified multiple times for each
    egress rule. Each egress block supports fields documented below. This argument is processed in [attr
    ibute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
    """
    egress: list[Egress] | core.ArrayOut[Egress] | None = core.attr(
        Egress, default=None, computed=True, kind=core.Kind.array
    )

    """
    ID of the security group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Configuration block for ingress rules. Can be specified multiple times for each ingress r
    ule. Each ingress block supports fields documented below. This argument is processed in [attribute-a
    s-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
    """
    ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.attr(
        Ingress, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional, Forces new resource) Name of the security group. If omitted, Terraform will assign a rand
    om, unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Owner ID.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Instruct Terraform to revoke all of the Security Groups attached ingress and egress rules
    before deleting the rule itself. This is normally not needed, however certain AWS services such as
    Elastic Map Reduce may automatically add required rules to security groups used with the service, an
    d those rules may contain a cyclic dependency that prevent the security groups from being destroyed
    without removing the dependency first. Default `false`.
    """
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
    (Optional, Forces new resource) VPC ID.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut | None = None,
        egress: list[Egress] | core.ArrayOut[Egress] | None = None,
        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
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
            args=SecurityGroup.Args(
                description=description,
                egress=egress,
                ingress=ingress,
                name=name,
                name_prefix=name_prefix,
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
        description: str | core.StringOut | None = core.arg(default=None)

        egress: list[Egress] | core.ArrayOut[Egress] | None = core.arg(default=None)

        ingress: list[Ingress] | core.ArrayOut[Ingress] | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        revoke_rules_on_delete: bool | core.BoolOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
