import terrascript.core as core


@core.resource(type="aws_route53_resolver_dnssec_config", namespace="route53_resolver")
class DnssecConfig(core.Resource):
    """
    The ARN for a configuration for DNSSEC validation.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID for a configuration for DNSSEC validation.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The owner account ID of the virtual private cloud (VPC) for a configuration for DNSSEC validation.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The ID of the virtual private cloud (VPC) that you're updating the DNSSEC validation stat
    us for.
    """
    resource_id: str | core.StringOut = core.attr(str)

    """
    The validation status for a DNSSEC configuration. The status can be one of the following: `ENABLING`
    , `ENABLED`, `DISABLING` and `DISABLED`.
    """
    validation_status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_id: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DnssecConfig.Args(
                resource_id=resource_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_id: str | core.StringOut = core.arg()
