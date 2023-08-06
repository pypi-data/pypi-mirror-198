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


@core.data(type="aws_customer_gateway", namespace="vpn")
class DsCustomerGateway(core.Data):
    """
    The ARN of the customer gateway.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).
    """
    bgp_asn: int | core.IntOut = core.attr(int, computed=True)

    """
    The Amazon Resource Name (ARN) for the customer gateway certificate.
    """
    certificate_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    A name for the customer gateway device.
    """
    device_name: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) One or more [name-value pairs][dcg-filters] to filter by.
    """
    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    """
    (Optional) The ID of the gateway.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The IP address of the gateway's Internet-routable external interface.
    """
    ip_address: str | core.StringOut = core.attr(str, computed=True)

    """
    Map of key-value pairs assigned to the gateway.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The type of customer gateway. The only type AWS supports at this time is "ipsec.1".
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
        id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCustomerGateway.Args(
                filter=filter,
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
