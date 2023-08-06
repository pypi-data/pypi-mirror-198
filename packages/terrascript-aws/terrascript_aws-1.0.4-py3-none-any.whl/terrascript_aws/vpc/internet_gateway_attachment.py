import terrascript.core as core


@core.resource(type="aws_internet_gateway_attachment", namespace="vpc")
class InternetGatewayAttachment(core.Resource):
    """
    The ID of the VPC and Internet Gateway separated by a colon.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the internet gateway.
    """
    internet_gateway_id: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the VPC.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        internet_gateway_id: str | core.StringOut,
        vpc_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InternetGatewayAttachment.Args(
                internet_gateway_id=internet_gateway_id,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        internet_gateway_id: str | core.StringOut = core.arg()

        vpc_id: str | core.StringOut = core.arg()
