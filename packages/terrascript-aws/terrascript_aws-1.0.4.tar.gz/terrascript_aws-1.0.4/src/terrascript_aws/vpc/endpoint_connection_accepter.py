import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_connection_accepter", namespace="vpc")
class EndpointConnectionAccepter(core.Resource):
    """
    The ID of the VPC Endpoint Connection.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) AWS VPC Endpoint ID.
    """
    vpc_endpoint_id: str | core.StringOut = core.attr(str)

    """
    (Required) AWS VPC Endpoint Service ID.
    """
    vpc_endpoint_service_id: str | core.StringOut = core.attr(str)

    """
    State of the VPC Endpoint.
    """
    vpc_endpoint_state: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_endpoint_id: str | core.StringOut,
        vpc_endpoint_service_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointConnectionAccepter.Args(
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_endpoint_service_id=vpc_endpoint_service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        vpc_endpoint_id: str | core.StringOut = core.arg()

        vpc_endpoint_service_id: str | core.StringOut = core.arg()
