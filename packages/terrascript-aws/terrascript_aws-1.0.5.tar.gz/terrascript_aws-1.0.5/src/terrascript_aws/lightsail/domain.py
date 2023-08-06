import terrascript.core as core


@core.resource(type="aws_lightsail_domain", namespace="lightsail")
class Domain(core.Resource):
    """
    The ARN of the Lightsail domain
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Lightsail domain to manage
    """
    domain_name: str | core.StringOut = core.attr(str)

    """
    The name used for this domain
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                domain_name=domain_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: str | core.StringOut = core.arg()
