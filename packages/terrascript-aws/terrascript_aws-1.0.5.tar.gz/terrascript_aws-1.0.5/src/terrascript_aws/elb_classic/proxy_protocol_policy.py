import terrascript.core as core


@core.resource(type="aws_proxy_protocol_policy", namespace="elb_classic")
class ProxyProtocolPolicy(core.Resource):
    """
    The ID of the policy.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) List of instance ports to which the policy
    """
    instance_ports: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Required) The load balancer to which the policy
    """
    load_balancer: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_ports: list[str] | core.ArrayOut[core.StringOut],
        load_balancer: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProxyProtocolPolicy.Args(
                instance_ports=instance_ports,
                load_balancer=load_balancer,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_ports: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        load_balancer: str | core.StringOut = core.arg()
