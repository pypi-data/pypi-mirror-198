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


@core.data(type="aws_nat_gateway", namespace="vpc")
class DsNatGateway(core.Data):
    """
    The Id of the EIP allocated to the selected Nat Gateway.
    """

    allocation_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The connectivity type of the NAT Gateway.
    """
    connectivity_type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Custom filter block as described below.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The id of the specific Nat Gateway to retrieve.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The Id of the ENI allocated to the selected Nat Gateway.
    """
    network_interface_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The private Ip address of the selected Nat Gateway.
    """
    private_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    The public Ip (EIP) address of the selected Nat Gateway.
    """
    public_ip: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The state of the NAT gateway (pending | failed | available | deleting | deleted ).
    """
    state: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The id of subnet that the Nat Gateway resides in.
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A map of tags, each pair of which must exactly match
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) The id of the VPC that the Nat Gateway resides in.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        state: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsNatGateway.Args(
                filter=filter,
                id=id,
                state=state,
                subnet_id=subnet_id,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        state: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
