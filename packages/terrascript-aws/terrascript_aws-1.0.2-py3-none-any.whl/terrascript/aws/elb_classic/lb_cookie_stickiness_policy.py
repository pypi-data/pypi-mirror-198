import terrascript.core as core


@core.resource(type="aws_lb_cookie_stickiness_policy", namespace="aws_elb_classic")
class LbCookieStickinessPolicy(core.Resource):

    cookie_expiration_period: int | core.IntOut | None = core.attr(int, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    lb_port: int | core.IntOut = core.attr(int)

    load_balancer: str | core.StringOut = core.attr(str)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        lb_port: int | core.IntOut,
        load_balancer: str | core.StringOut,
        name: str | core.StringOut,
        cookie_expiration_period: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbCookieStickinessPolicy.Args(
                lb_port=lb_port,
                load_balancer=load_balancer,
                name=name,
                cookie_expiration_period=cookie_expiration_period,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cookie_expiration_period: int | core.IntOut | None = core.arg(default=None)

        lb_port: int | core.IntOut = core.arg()

        load_balancer: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
