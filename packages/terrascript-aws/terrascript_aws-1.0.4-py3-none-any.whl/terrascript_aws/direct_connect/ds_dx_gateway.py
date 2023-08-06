import terrascript.core as core


@core.data(type="aws_dx_gateway", namespace="direct_connect")
class DsDxGateway(core.Data):
    """
    The ASN on the Amazon side of the connection.
    """

    amazon_side_asn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the gateway to retrieve.
    """
    name: str | core.StringOut = core.attr(str)

    """
    AWS Account ID of the gateway.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsDxGateway.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
