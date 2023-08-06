import terrascript.core as core


@core.schema
class Options(core.Schema):

    ipv6_support: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        ipv6_support: bool | core.BoolOut,
    ):
        super().__init__(
            args=Options.Args(
                ipv6_support=ipv6_support,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ipv6_support: bool | core.BoolOut = core.arg()


@core.resource(type="aws_networkmanager_vpc_attachment", namespace="networkmanager")
class VpcAttachment(core.Resource):
    """
    The ARN of the attachment.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The policy rule number associated with the attachment.
    """
    attachment_policy_rule_number: int | core.IntOut = core.attr(int, computed=True)

    """
    The type of attachment.
    """
    attachment_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of a core network.
    """
    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of a core network for the VPC attachment.
    """
    core_network_id: str | core.StringOut = core.attr(str)

    """
    The Region where the edge is located.
    """
    edge_location: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the attachment.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Options for the VPC attachment.
    """
    options: Options | None = core.attr(Options, default=None)

    """
    The ID of the attachment account owner.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The attachment resource ARN.
    """
    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The name of the segment attachment.
    """
    segment_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The state of the attachment.
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The subnet ARN of the VPC attachment.
    """
    subnet_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) Key-value tags for the Global Network. If configured with a provider [`default_tags` conf
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
    (Required) The ARN of the VPC.
    """
    vpc_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        core_network_id: str | core.StringOut,
        subnet_arns: list[str] | core.ArrayOut[core.StringOut],
        vpc_arn: str | core.StringOut,
        options: Options | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VpcAttachment.Args(
                core_network_id=core_network_id,
                subnet_arns=subnet_arns,
                vpc_arn=vpc_arn,
                options=options,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        core_network_id: str | core.StringOut = core.arg()

        options: Options | None = core.arg(default=None)

        subnet_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_arn: str | core.StringOut = core.arg()
