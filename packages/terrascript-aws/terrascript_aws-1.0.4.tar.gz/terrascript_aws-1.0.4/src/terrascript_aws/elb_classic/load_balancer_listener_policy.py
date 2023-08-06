import terrascript.core as core


@core.resource(type="aws_load_balancer_listener_policy", namespace="elb_classic")
class LoadBalancerListenerPolicy(core.Resource):
    """
    The ID of the policy.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The load balancer to attach the policy to.
    """
    load_balancer_name: str | core.StringOut = core.attr(str)

    """
    (Required) The load balancer listener port to apply the policy to.
    """
    load_balancer_port: int | core.IntOut = core.attr(int)

    """
    (Required) List of Policy Names to apply to the backend server.
    """
    policy_names: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        load_balancer_name: str | core.StringOut,
        load_balancer_port: int | core.IntOut,
        policy_names: list[str] | core.ArrayOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoadBalancerListenerPolicy.Args(
                load_balancer_name=load_balancer_name,
                load_balancer_port=load_balancer_port,
                policy_names=policy_names,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        load_balancer_name: str | core.StringOut = core.arg()

        load_balancer_port: int | core.IntOut = core.arg()

        policy_names: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
