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


@core.data(type="aws_vpn_gateway", namespace="vpn")
class DsGateway(core.Data):
    """
    (Optional) The Autonomous System Number (ASN) for the Amazon side of the specific VPN Gateway to ret
    rieve.
    """

    amazon_side_asn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of a VPC attached to the specific VPN Gateway to retrieve.
    """
    attached_vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Availability Zone of the specific VPN Gateway to retrieve.
    """
    availability_zone: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Custom filter block as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The ID of the specific VPN Gateway to retrieve.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The state of the specific VPN Gateway to retrieve.
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
        amazon_side_asn: str | core.StringOut | None = None,
        attached_vpc_id: str | core.StringOut | None = None,
        availability_zone: str | core.StringOut | None = None,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsGateway.Args(
                amazon_side_asn=amazon_side_asn,
                attached_vpc_id=attached_vpc_id,
                availability_zone=availability_zone,
                filter=filter,
                id=id,
                state=state,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amazon_side_asn: str | core.StringOut | None = core.arg(default=None)

        attached_vpc_id: str | core.StringOut | None = core.arg(default=None)

        availability_zone: str | core.StringOut | None = core.arg(default=None)

        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
