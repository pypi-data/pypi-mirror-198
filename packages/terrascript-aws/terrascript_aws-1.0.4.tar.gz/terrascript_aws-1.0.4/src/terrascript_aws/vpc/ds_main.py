import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class CidrBlockAssociations(core.Schema):

    association_id: str | core.StringOut = core.attr(str, computed=True)

    cidr_block: str | core.StringOut = core.attr(str, computed=True)

    state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        association_id: str | core.StringOut,
        cidr_block: str | core.StringOut,
        state: str | core.StringOut,
    ):
        super().__init__(
            args=CidrBlockAssociations.Args(
                association_id=association_id,
                cidr_block=cidr_block,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        association_id: str | core.StringOut = core.arg()

        cidr_block: str | core.StringOut = core.arg()

        state: str | core.StringOut = core.arg()


@core.data(type="aws_vpc", namespace="vpc")
class DsMain(core.Data):
    """
    Amazon Resource Name (ARN) of VPC
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The cidr block of the desired VPC.
    """
    cidr_block: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cidr_block_associations: list[CidrBlockAssociations] | core.ArrayOut[
        CidrBlockAssociations
    ] = core.attr(CidrBlockAssociations, computed=True, kind=core.Kind.array)

    """
    (Optional) Boolean constraint on whether the desired VPC is
    """
    default: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    """
    (Optional) The DHCP options id of the desired VPC.
    """
    dhcp_options_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Whether or not the VPC has DNS hostname support
    """
    enable_dns_hostnames: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether or not the VPC has DNS support
    """
    enable_dns_support: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Custom filter block as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The id of the specific VPC to retrieve.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The allowed tenancy of instances launched into the
    """
    instance_tenancy: str | core.StringOut = core.attr(str, computed=True)

    """
    The association ID for the IPv6 CIDR block.
    """
    ipv6_association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IPv6 CIDR block.
    """
    ipv6_cidr_block: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the main route table associated with this VPC.
    """
    main_route_table_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the AWS account that owns the VPC.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The current state of the desired VPC.
    """
    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        cidr_block: str | core.StringOut | None = None,
        default: bool | core.BoolOut | None = None,
        dhcp_options_id: str | core.StringOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMain.Args(
                cidr_block=cidr_block,
                default=default,
                dhcp_options_id=dhcp_options_id,
                filter=filter,
                id=id,
                state=state,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: str | core.StringOut | None = core.arg(default=None)

        default: bool | core.BoolOut | None = core.arg(default=None)

        dhcp_options_id: str | core.StringOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
