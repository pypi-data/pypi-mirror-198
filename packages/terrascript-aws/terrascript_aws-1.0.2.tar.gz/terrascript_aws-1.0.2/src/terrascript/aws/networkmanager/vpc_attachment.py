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


@core.resource(type="aws_networkmanager_vpc_attachment", namespace="aws_networkmanager")
class VpcAttachment(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attachment_policy_rule_number: int | core.IntOut = core.attr(int, computed=True)

    attachment_type: str | core.StringOut = core.attr(str, computed=True)

    core_network_arn: str | core.StringOut = core.attr(str, computed=True)

    core_network_id: str | core.StringOut = core.attr(str)

    edge_location: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    options: Options | None = core.attr(Options, default=None)

    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    segment_name: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    subnet_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
