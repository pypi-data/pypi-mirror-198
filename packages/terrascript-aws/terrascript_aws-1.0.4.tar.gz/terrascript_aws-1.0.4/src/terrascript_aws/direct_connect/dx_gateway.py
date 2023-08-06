import terrascript.core as core


@core.resource(type="aws_dx_gateway", namespace="direct_connect")
class DxGateway(core.Resource):
    """
    (Required) The ASN to be configured on the Amazon side of the connection. The ASN must be in the pri
    vate range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.
    """

    amazon_side_asn: str | core.StringOut = core.attr(str)

    """
    The ID of the gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the connection.
    """
    name: str | core.StringOut = core.attr(str)

    """
    AWS Account ID of the gateway.
    """
    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        amazon_side_asn: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxGateway.Args(
                amazon_side_asn=amazon_side_asn,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        amazon_side_asn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
