import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_config", namespace="route53_resolver")
class FirewallConfig(core.Resource):

    firewall_fail_open: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    resource_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_id: str | core.StringOut,
        firewall_fail_open: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallConfig.Args(
                resource_id=resource_id,
                firewall_fail_open=firewall_fail_open,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        firewall_fail_open: str | core.StringOut | None = core.arg(default=None)

        resource_id: str | core.StringOut = core.arg()
