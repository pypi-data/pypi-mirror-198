import terrascript.core as core


@core.resource(type="aws_app_cookie_stickiness_policy", namespace="elb_classic")
class AppCookieStickinessPolicy(core.Resource):
    """
    (Required) The application cookie whose lifetime the ELB's cookie should follow.
    """

    cookie_name: str | core.StringOut = core.attr(str)

    """
    The ID of the policy.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The load balancer port to which the policy
    """
    lb_port: int | core.IntOut = core.attr(int)

    """
    (Required) The name of load balancer to which the policy
    """
    load_balancer: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the stickiness policy.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cookie_name: str | core.StringOut,
        lb_port: int | core.IntOut,
        load_balancer: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppCookieStickinessPolicy.Args(
                cookie_name=cookie_name,
                lb_port=lb_port,
                load_balancer=load_balancer,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cookie_name: str | core.StringOut = core.arg()

        lb_port: int | core.IntOut = core.arg()

        load_balancer: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
