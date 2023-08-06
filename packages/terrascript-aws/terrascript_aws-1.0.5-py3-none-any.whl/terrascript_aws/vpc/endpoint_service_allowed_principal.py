import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_service_allowed_principal", namespace="vpc")
class EndpointServiceAllowedPrincipal(core.Resource):
    """
    The ID of the association.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ARN of the principal to allow permissions.
    """
    principal_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The ID of the VPC endpoint service to allow permission.
    """
    vpc_endpoint_service_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        principal_arn: str | core.StringOut,
        vpc_endpoint_service_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointServiceAllowedPrincipal.Args(
                principal_arn=principal_arn,
                vpc_endpoint_service_id=vpc_endpoint_service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        principal_arn: str | core.StringOut = core.arg()

        vpc_endpoint_service_id: str | core.StringOut = core.arg()
