import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_subnet_association", namespace="aws_vpc")
class EndpointSubnetAssociation(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str)

    vpc_endpoint_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_id: str | core.StringOut,
        vpc_endpoint_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointSubnetAssociation.Args(
                subnet_id=subnet_id,
                vpc_endpoint_id=vpc_endpoint_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        subnet_id: str | core.StringOut = core.arg()

        vpc_endpoint_id: str | core.StringOut = core.arg()
