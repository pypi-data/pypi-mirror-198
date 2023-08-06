import terrascript.core as core


@core.resource(type="aws_shield_protection_health_check_association", namespace="shield")
class ProtectionHealthCheckAssociation(core.Resource):
    """
    (Required) The ARN (Amazon Resource Name) of the Route53 Health Check resource which will be associa
    ted to the protected resource.
    """

    health_check_arn: str | core.StringOut = core.attr(str)

    """
    The unique identifier (ID) for the Protection object that is created.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the protected resource.
    """
    shield_protection_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        health_check_arn: str | core.StringOut,
        shield_protection_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProtectionHealthCheckAssociation.Args(
                health_check_arn=health_check_arn,
                shield_protection_id=shield_protection_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        health_check_arn: str | core.StringOut = core.arg()

        shield_protection_id: str | core.StringOut = core.arg()
